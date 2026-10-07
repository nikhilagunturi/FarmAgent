"""
core/llm_client.py
Isolated Groq LLM integration client for FarmAgent.
Provides ultra-fast inference using models like llama-3.3-70b-versatile or llama-3.1-8b-instant.
Transparently falls back to local heuristic reasoning if GROQ_API_KEY is not configured.
"""

import os
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()

class GroqLLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY", "").strip()
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip() or "llama-3.3-70b-versatile"
        self._client = None
        self._initialized = False

        if self.api_key:
            try:
                from groq import Groq
                self._client = Groq(api_key=self.api_key)
                self._initialized = True
            except Exception as e:
                print(f"[GroqLLMClient] Failed to initialize Groq client: {e}")
                self._initialized = False

    def is_enabled(self) -> bool:
        return self._initialized and self._client is not None

    def get_model_name(self) -> str:
        return self.model if self.is_enabled() else "Offline Rule Engine"

    def set_api_key(self, api_key: str, model: Optional[str] = None) -> tuple[bool, str]:
        """Dynamically set or update the Groq API key at runtime."""
        self.api_key = api_key.strip()
        if model:
            self.model = model.strip()
        if self.api_key:
            try:
                from groq import Groq
                self._client = Groq(api_key=self.api_key)
                self._initialized = True
                # Persist to .env if desired or keep in memory
                os.environ["GROQ_API_KEY"] = self.api_key
                return True, f"Groq activated with model {self.model}"
            except Exception as e:
                self._client = None
                self._initialized = False
                return False, f"Failed to initialize Groq: {e}"
        else:
            self._client = None
            self._initialized = False
            if "GROQ_API_KEY" in os.environ:
                del os.environ["GROQ_API_KEY"]
            return True, "Reverted to offline mode"

    def chat(self, prompt: str, system_prompt: str = "", temperature: float = 0.2) -> Optional[str]:
        """
        Sends a query to Groq LLM.
        Returns the text response or None if disabled/failed.
        """
        if not self.is_enabled():
            return None

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=1024
            )
            content = response.choices[0].message.content
            return content.strip() if content else None
        except Exception as e:
            # If the model name is deprecated or unsupported, try fallback model
            if "model" in str(e).lower() and self.model != "llama-3.1-8b-instant":
                try:
                    fallback_model = "llama-3.1-8b-instant"
                    response = self._client.chat.completions.create(
                        model=fallback_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=1024
                    )
                    content = response.choices[0].message.content
                    return content.strip() if content else None
                except Exception:
                    pass
            print(f"[GroqLLMClient] LLM query failed (falling back to local engine): {e}")
            return None
