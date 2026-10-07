const translations = {
  en: {
    language:"Language", welcomeEyebrow:"A helping hand for every farm", welcomeSubtitle:"Tell us what is happening to your crop. We'll help you understand what to do.",
    develop:"DEVELOP", developDesc:"Understand", debate:"DEBATE", debateDesc:"Compare ideas", defend:"DEFEND", defendDesc:"Explain why",
    demoKicker:"TRY FARMAGENT", demoTitle:"See how it works", demoHelp:"Choose a sample problem to run a demo.", demoTomato:"My tomato leaves are curling", demoDry:"My crop looks dry", demoInsects:"I see insects on the leaves", demoWet:"My field has too much water", demoNote:"Demo examples use sample weather, not live farm measurements.",
    intakeKicker:"YOUR CROP", intakeTitle:"Tell us what you see", optionalNote:"You can skip anything you are not sure about.", cropQuestion:"What are you growing?", cropTomato:"Tomato", cropRice:"Rice", cropMaize:"Maize", cropPotato:"Potato", cropChilli:"Chilli", cropGroundnut:"Groundnut", cropOther:"Other", typeCrop:"Type your crop", cropPlaceholder:"For example, onion",
    problemQuestion:"What is the problem?", problemThirsty:"Plant looks thirsty", problemYellow:"Leaves are turning yellow", problemCurling:"Leaves are curling", problemInsects:"I see insects", problemDisease:"Plant may have a disease", problemGrowth:"Plant is not growing well", problemWet:"Too much water", problemHeat:"Too much heat", problemUnknown:"I don't know",
    describeLabel:"Describe the problem in your own words", describePlaceholder:"My tomato leaves are curling and the plants look weak.", voiceSoon:"Tell FarmAgent<br><small>Coming soon</small>", photoQuestion:"Take a photo (optional)", optional:"OPTIONAL", photoHelp:"A photo can help FarmAgent identify possible crop problems.", takePhoto:"Take a photo of the plant", uploadPhoto:"Upload a photo", photoNotAnalyzed:"Photo analysis is not connected yet. Your photo will not be uploaded or analyzed.",
    soilQuestion:"How does the soil look or feel?", soilVeryDry:"Very dry", soilSlightlyDry:"Slightly dry", soilNormal:"Normal", soilWet:"Wet", soilVeryWet:"Very wet", dontKnow:"I don't know", notSure:"Not sure? That's okay.",
    waterQuestion:"Has it rained recently?", yes:"Yes", no:"No", lastWatered:"When did you last water the crop?", today:"Today", yesterday:"Yesterday", twoThreeDays:"2–3 days ago", moreThreeDays:"More than 3 days ago", dontRemember:"I don't remember",
    locationQuestion:"Where is your farm? (optional)", useLocation:"Use my location", or:"or", villageTown:"Village / Town", villagePlaceholder:"Village / Town", locationOptional:"Location is optional. We only use it to look for weather.", locationGetting:"Getting your location…", locationSet:"Location added.", locationFailed:"We could not get your location. You can type your village or town instead.",
    moreDetails:"More details (optional)", advancedHelp:"Only add details you already know. None of these are needed for an analysis.", growthStage:"Growth stage", growthPlaceholder:"For example, flowering", soilType:"Soil type", soilMoisture:"Soil moisture (%)", rainfall:"Recent rainfall (mm)", temperature:"Temperature (°C)", otherInfo:"Other information", weatherDemo:"Weather example (demo only)", advancedDemoWarning:"Weather choices are sample scenarios, not live forecasts.", privacyNote:"You do not need to share exact measurements.", analyze:"ANALYZE MY CROP",
    working:"FarmAgent is looking into this…", progressUnderstand:"🔍 Understanding your problem…", progressCrop:"🌱 Checking crop health…", progressWater:"💧 Checking water needs…", progressWeather:"🌦️ Checking weather…", progressRisk:"🛡️ Checking risks…", progressDebate:"⚔️ Comparing recommendations…",
    yourResult:"YOUR FARMAGENT ADVICE", resultTitle:"Here is what we found", whatFound:"WHAT WE FOUND", whatToDo:"WHAT YOU SHOULD DO", beCareful:"BE CAREFUL", watchFor:"WATCH FOR", whyTitle:"Why FarmAgent thinks this", debateTitle:"Agent debate", tapToExpand:"Tap to see how the agents compared ideas", finalChoice:"FarmAgent's final choice", defendNote:"FarmAgent compared different advice and chose the safest next step.", weatherDemoNotice:"Weather information below is sample/demo data, not a live reading or forecast.", footer:"FarmAgent helps you make a more informed choice. Ask a local farm expert for urgent or serious crop problems.", confidenceHigh:"🟢 High confidence — your observations give a clear picture.", confidenceMedium:"🟡 Medium confidence — more details or a clear photo may help.", confidenceLow:"🔴 Low confidence — we need more information to be sure.", missingAdvice:"We don't have enough information to give a clear answer. Please describe what you see or choose a problem above."
  },
  hi: {
    language:"भाषा", welcomeEyebrow:"हर खेत के लिए मदद", welcomeSubtitle:"फसल में क्या हो रहा है, हमें बताएं। हम समझने में मदद करेंगे कि क्या करना है।", develop:"समझें", developDesc:"समस्या समझें", debate:"तुलना करें", debateDesc:"सलाह की तुलना", defend:"समझाएं", defendDesc:"कारण बताएं",
    demoKicker:"FARMAGENT आज़माएं", demoTitle:"देखें यह कैसे काम करता है", demoHelp:"डेमो देखने के लिए एक समस्या चुनें।", demoTomato:"मेरे टमाटर के पत्ते मुड़ रहे हैं", demoDry:"मेरी फसल सूखी दिखती है", demoInsects:"पत्तों पर कीड़े दिख रहे हैं", demoWet:"खेत में बहुत पानी है", demoNote:"डेमो में नमूना मौसम है, खेत का असली माप नहीं।",
    intakeKicker:"आपकी फसल", intakeTitle:"आप क्या देख रहे हैं?", optionalNote:"जिस बात का पता न हो, उसे छोड़ सकते हैं।", cropQuestion:"आप क्या उगा रहे हैं?", cropTomato:"टमाटर", cropRice:"धान", cropMaize:"मक्का", cropPotato:"आलू", cropChilli:"मिर्च", cropGroundnut:"मूंगफली", cropOther:"अन्य", typeCrop:"अपनी फसल लिखें", cropPlaceholder:"जैसे, प्याज़",
    problemQuestion:"क्या समस्या है?", problemThirsty:"पौधा मुरझाया/प्यासा लगता है", problemYellow:"पत्ते पीले हो रहे हैं", problemCurling:"पत्ते मुड़ रहे हैं", problemInsects:"कीड़े दिख रहे हैं", problemDisease:"पौधे में बीमारी हो सकती है", problemGrowth:"पौधा ठीक से नहीं बढ़ रहा", problemWet:"बहुत पानी है", problemHeat:"बहुत गर्मी है", problemUnknown:"मुझे नहीं पता", describeLabel:"समस्या अपने शब्दों में बताएं", describePlaceholder:"मेरे टमाटर के पत्ते मुड़ रहे हैं और पौधे कमजोर दिखते हैं।", voiceSoon:"FarmAgent को बताएं<br><small>जल्द आ रहा है</small>",
    photoQuestion:"फोटो लें (ज़रूरी नहीं)", optional:"ज़रूरी नहीं", photoHelp:"फोटो से FarmAgent को फसल की समस्या पहचानने में मदद मिल सकती है।", takePhoto:"पौधे की फोटो लें", uploadPhoto:"फोटो अपलोड करें", photoNotAnalyzed:"फोटो की जांच अभी उपलब्ध नहीं है। आपकी फोटो अपलोड या जांच नहीं होगी।",
    soilQuestion:"मिट्टी कैसी दिखती या लगती है?", soilVeryDry:"बहुत सूखी", soilSlightlyDry:"थोड़ी सूखी", soilNormal:"सामान्य", soilWet:"गीली", soilVeryWet:"बहुत गीली", dontKnow:"मुझे नहीं पता", notSure:"पक्का नहीं? कोई बात नहीं।", waterQuestion:"क्या हाल में बारिश हुई?", yes:"हाँ", no:"नहीं", lastWatered:"फसल को आखिरी बार पानी कब दिया?", today:"आज", yesterday:"कल", twoThreeDays:"2–3 दिन पहले", moreThreeDays:"3 दिन से पहले", dontRemember:"याद नहीं",
    locationQuestion:"आपका खेत कहाँ है? (ज़रूरी नहीं)", useLocation:"मेरी जगह इस्तेमाल करें", or:"या", villageTown:"गाँव / शहर", villagePlaceholder:"गाँव / शहर", locationOptional:"जगह देना ज़रूरी नहीं। इसका उपयोग मौसम देखने के लिए होगा।", locationGetting:"आपकी जगह देख रहे हैं…", locationSet:"जगह जोड़ दी गई।", locationFailed:"जगह नहीं मिली। आप गाँव या शहर लिख सकते हैं।",
    moreDetails:"और जानकारी (ज़रूरी नहीं)", advancedHelp:"केवल वही जानकारी दें जो आपको पहले से पता है।", growthStage:"फसल की अवस्था", growthPlaceholder:"जैसे, फूल आना", soilType:"मिट्टी का प्रकार", soilMoisture:"मिट्टी की नमी (%)", rainfall:"हाल की बारिश (मिमी)", temperature:"तापमान (°C)", otherInfo:"अन्य जानकारी", weatherDemo:"मौसम का उदाहरण (केवल डेमो)", advancedDemoWarning:"मौसम के विकल्प नमूने हैं, असली पूर्वानुमान नहीं।", privacyNote:"सटीक माप बताना ज़रूरी नहीं।", analyze:"मेरी फसल की जांच करें",
    working:"FarmAgent जानकारी देख रहा है…", progressUnderstand:"🔍 समस्या समझ रहे हैं…", progressCrop:"🌱 फसल की सेहत देख रहे हैं…", progressWater:"💧 पानी की जरूरत देख रहे हैं…", progressWeather:"🌦️ मौसम देख रहे हैं…", progressRisk:"🛡️ जोखिम देख रहे हैं…", progressDebate:"⚔️ सलाह की तुलना कर रहे हैं…",
    yourResult:"FARMAGENT की सलाह", resultTitle:"हमने यह पाया", whatFound:"क्या पता चला", whatToDo:"आप क्या करें", beCareful:"सावधान रहें", watchFor:"इन बातों पर ध्यान दें", whyTitle:"FarmAgent ऐसा क्यों सोचता है", debateTitle:"एजेंटों की चर्चा", tapToExpand:"सलाह की तुलना देखने के लिए दबाएं", finalChoice:"FarmAgent का अंतिम सुझाव", defendNote:"FarmAgent ने अलग-अलग सलाह की तुलना करके सुरक्षित कदम चुना।", weatherDemoNotice:"मौसम की जानकारी नमूना है, असली माप या पूर्वानुमान नहीं।", footer:"FarmAgent बेहतर निर्णय लेने में मदद करता है। गंभीर समस्या में स्थानीय कृषि विशेषज्ञ से पूछें।", confidenceHigh:"🟢 भरोसा अधिक — आपकी जानकारी से स्थिति स्पष्ट है।", confidenceMedium:"🟡 मध्यम भरोसा — और जानकारी या साफ फोटो से मदद मिल सकती है।", confidenceLow:"🔴 भरोसा कम — पक्का बताने के लिए और जानकारी चाहिए।", missingAdvice:"स्पष्ट सलाह देने के लिए पर्याप्त जानकारी नहीं है। कृपया समस्या बताएं या ऊपर एक विकल्प चुनें।"
  },
  te: {
    language:"భాష", welcomeEyebrow:"ప్రతి రైతుకు తోడుగా", welcomeSubtitle:"మీ పంటకు ఏమి జరుగుతోందో చెప్పండి. ఏం చేయాలో అర్థం చేసుకోవడంలో మేము సహాయం చేస్తాము.", develop:"అర్థం చేసుకోండి", developDesc:"సమస్యను తెలుసుకోండి", debate:"చర్చించండి", debateDesc:"సలహాలను పోల్చండి", defend:"వివరించండి", defendDesc:"కారణం చెప్పండి",
    demoKicker:"FARMAGENT ప్రయత్నించండి", demoTitle:"ఇది ఎలా పనిచేస్తుందో చూడండి", demoHelp:"డెమో కోసం ఒక సమస్యను ఎంచుకోండి.", demoTomato:"నా టమాటా ఆకులు ముడుచుకుంటున్నాయి", demoDry:"నా పంట ఎండిపోయినట్లు ఉంది", demoInsects:"ఆకులపై పురుగులు కనిపిస్తున్నాయి", demoWet:"నా పొలంలో నీరు ఎక్కువగా ఉంది", demoNote:"డెమోలో నమూనా వాతావరణం మాత్రమే ఉంటుంది; నిజమైన కొలతలు కావు.",
    intakeKicker:"మీ పంట", intakeTitle:"మీరు ఏమి గమనిస్తున్నారు?", optionalNote:"తెలియని విషయాలను వదిలేయవచ్చు.", cropQuestion:"మీరు ఏమి పండిస్తున్నారు?", cropTomato:"టమాటా", cropRice:"వరి", cropMaize:"మొక్కజొన్న", cropPotato:"బంగాళాదుంప", cropChilli:"మిరప", cropGroundnut:"వేరుశనగ", cropOther:"ఇతరము", typeCrop:"మీ పంట పేరు రాయండి", cropPlaceholder:"ఉదా: ఉల్లి",
    problemQuestion:"ఏ సమస్య ఉంది?", problemThirsty:"మొక్కకు నీరు కావాలి అనిపిస్తోంది", problemYellow:"ఆకులు పసుపు రంగులోకి మారుతున్నాయి", problemCurling:"ఆకులు ముడుచుకుంటున్నాయి", problemInsects:"పురుగులు కనిపిస్తున్నాయి", problemDisease:"మొక్కకు వ్యాధి ఉండవచ్చు", problemGrowth:"మొక్క సరిగా పెరగడం లేదు", problemWet:"నీరు ఎక్కువగా ఉంది", problemHeat:"ఎండ ఎక్కువగా ఉంది", problemUnknown:"నాకు తెలియదు", describeLabel:"మీ మాటల్లో సమస్యను వివరించండి", describePlaceholder:"నా టమాటా ఆకులు ముడుచుకుంటున్నాయి, మొక్కలు బలహీనంగా ఉన్నాయి.", voiceSoon:"FarmAgent‌కు చెప్పండి<br><small>త్వరలో వస్తుంది</small>",
    photoQuestion:"ఫోటో తీయండి (ఐచ్ఛికం)", optional:"ఐచ్ఛికం", photoHelp:"పంట సమస్యను గుర్తించడానికి ఫోటో FarmAgent‌కు సహాయపడవచ్చు.", takePhoto:"మొక్క ఫోటో తీయండి", uploadPhoto:"ఫోటో అప్‌లోడ్ చేయండి", photoNotAnalyzed:"ఫోటో విశ్లేషణ ఇంకా అందుబాటులో లేదు. ఫోటో అప్‌లోడ్ లేదా విశ్లేషణ చేయబడదు.",
    soilQuestion:"మట్టి ఎలా కనిపిస్తోంది లేదా అనిపిస్తోంది?", soilVeryDry:"చాలా ఎండిపోయింది", soilSlightlyDry:"కొద్దిగా ఎండిపోయింది", soilNormal:"సాధారణం", soilWet:"తడిగా ఉంది", soilVeryWet:"చాలా తడిగా ఉంది", dontKnow:"నాకు తెలియదు", notSure:"తెలియకపోయినా పరవాలేదు.", waterQuestion:"ఇటీవల వర్షం పడిందా?", yes:"అవును", no:"లేదు", lastWatered:"చివరిసారిగా పంటకు ఎప్పుడు నీరు పెట్టారు?", today:"ఈరోజు", yesterday:"నిన్న", twoThreeDays:"2–3 రోజుల క్రితం", moreThreeDays:"3 రోజుల కంటే ముందు", dontRemember:"గుర్తులేదు",
    locationQuestion:"మీ పొలం ఎక్కడ ఉంది? (ఐచ్ఛికం)", useLocation:"నా స్థానాన్ని ఉపయోగించండి", or:"లేదా", villageTown:"గ్రామం / పట్టణం", villagePlaceholder:"గ్రామం / పట్టణం", locationOptional:"స్థానం ఇవ్వడం ఐచ్ఛికం. వాతావరణం కోసం మాత్రమే ఉపయోగిస్తాము.", locationGetting:"మీ స్థానాన్ని పొందుతున్నాము…", locationSet:"స్థానం జోడించబడింది.", locationFailed:"స్థానం పొందలేకపోయాం. మీ గ్రామం లేదా పట్టణం రాయండి.",
    moreDetails:"మరిన్ని వివరాలు (ఐచ్ఛికం)", advancedHelp:"మీకు తెలిసిన వివరాలనే ఇవ్వండి. విశ్లేషణకు ఇవి అవసరం లేదు.", growthStage:"పంట దశ", growthPlaceholder:"ఉదా: పూత దశ", soilType:"మట్టి రకం", soilMoisture:"మట్టి తేమ (%)", rainfall:"ఇటీవలి వర్షపాతం (మి.మీ.)", temperature:"ఉష్ణోగ్రత (°C)", otherInfo:"ఇతర సమాచారం", weatherDemo:"వాతావరణ నమూనా (డెమో మాత్రమే)", advancedDemoWarning:"వాతావరణ ఎంపికలు నమూనాలు మాత్రమే; నిజమైన సూచన కాదు.", privacyNote:"ఖచ్చితమైన కొలతలు చెప్పాల్సిన అవసరం లేదు.", analyze:"నా పంటను విశ్లేషించండి",
    working:"FarmAgent పరిశీలిస్తోంది…", progressUnderstand:"🔍 సమస్యను అర్థం చేసుకుంటోంది…", progressCrop:"🌱 పంట ఆరోగ్యాన్ని చూస్తోంది…", progressWater:"💧 నీటి అవసరాన్ని చూస్తోంది…", progressWeather:"🌦️ వాతావరణాన్ని చూస్తోంది…", progressRisk:"🛡️ ప్రమాదాలను చూస్తోంది…", progressDebate:"⚔️ సలహాలను పోలుస్తోంది…",
    yourResult:"FARMAGENT సలహా", resultTitle:"మేము గమనించినది", whatFound:"మేము గుర్తించినది", whatToDo:"మీరు చేయవలసినది", beCareful:"జాగ్రత్త", watchFor:"గమనించండి", whyTitle:"FarmAgent ఇలా ఎందుకు భావిస్తోంది", debateTitle:"ఏజెంట్ల చర్చ", tapToExpand:"సలహాల పోలిక కోసం నొక్కండి", finalChoice:"FarmAgent తుది సూచన", defendNote:"వివిధ సలహాలను పోల్చి FarmAgent సురక్షితమైన చర్యను ఎంచుకుంది.", weatherDemoNotice:"క్రింది వాతావరణ సమాచారం నమూనా మాత్రమే; నిజమైన కొలత లేదా సూచన కాదు.", footer:"మంచి నిర్ణయం తీసుకోవడంలో FarmAgent సహాయపడుతుంది. తీవ్రమైన సమస్యకు స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.", confidenceHigh:"🟢 అధిక నమ్మకం — మీ పరిశీలనలతో పరిస్థితి స్పష్టంగా ఉంది।", confidenceMedium:"🟡 మధ్యస్థ నమ్మకం — మరిన్ని వివరాలు లేదా స్పష్టమైన ఫోటో సహాయపడవచ్చు.", confidenceLow:"🔴 తక్కువ నమ్మకం — నిర్ధారించడానికి మరింత సమాచారం అవసరం.", missingAdvice:"స్పష్టమైన సలహా ఇవ్వడానికి తగిన సమాచారం లేదు. దయచేసి సమస్యను వివరించండి లేదా పై ఎంపికను ఎంచుకోండి."
  },
  ta: {
    language:"மொழி", welcomeEyebrow:"ஒவ்வொரு விவசாயிக்கும் உதவி", welcomeSubtitle:"உங்கள் பயிரில் என்ன நடக்கிறது என்று சொல்லுங்கள். என்ன செய்ய வேண்டும் என்பதைப் புரிந்துகொள்ள உதவுகிறோம்.", develop:"புரிந்துகொள்", developDesc:"சிக்கலை அறி", debate:"ஒப்பிடு", debateDesc:"ஆலோசனைகளை ஒப்பிடு", defend:"விளக்கு", defendDesc:"காரணத்தைச் சொல்",
    demoKicker:"FARMAGENT முயற்சிக்கவும்", demoTitle:"இது எப்படி செயல்படுகிறது", demoHelp:"செயல்முறை விளக்கத்திற்கு ஒரு சிக்கலைத் தேர்ந்தெடுக்கவும்.", demoTomato:"என் தக்காளி இலைகள் சுருண்டுள்ளன", demoDry:"என் பயிர் வறண்டு தெரிகிறது", demoInsects:"இலைகளில் பூச்சிகள் தெரிகின்றன", demoWet:"என் வயலில் அதிக நீர் உள்ளது", demoNote:"செயல்முறை விளக்கத்தில் மாதிரி வானிலை மட்டுமே; உண்மையான அளவீடுகள் அல்ல.",
    intakeKicker:"உங்கள் பயிர்", intakeTitle:"நீங்கள் என்ன பார்க்கிறீர்கள்?", optionalNote:"தெரியாதவற்றைத் தவிர்க்கலாம்.", cropQuestion:"நீங்கள் என்ன பயிரிடுகிறீர்கள்?", cropTomato:"தக்காளி", cropRice:"நெல்", cropMaize:"மக்காச்சோளம்", cropPotato:"உருளைக்கிழங்கு", cropChilli:"மிளகாய்", cropGroundnut:"நிலக்கடலை", cropOther:"மற்றவை", typeCrop:"பயிரின் பெயரை எழுதுங்கள்", cropPlaceholder:"எடுத்துக்காட்டு: வெங்காயம்",
    problemQuestion:"என்ன பிரச்சினை?", problemThirsty:"செடிக்கு நீர் தேவைப்படுவது போல் உள்ளது", problemYellow:"இலைகள் மஞ்சளாகின்றன", problemCurling:"இலைகள் சுருள்கின்றன", problemInsects:"பூச்சிகள் தெரிகின்றன", problemDisease:"செடிக்கு நோய் இருக்கலாம்", problemGrowth:"செடி நன்றாக வளரவில்லை", problemWet:"அதிக நீர்", problemHeat:"அதிக வெப்பம்", problemUnknown:"தெரியவில்லை", describeLabel:"உங்கள் சொந்த வார்த்தைகளில் பிரச்சினையைச் சொல்லுங்கள்", describePlaceholder:"என் தக்காளி இலைகள் சுருண்டுள்ளன; செடிகள் பலவீனமாகத் தெரிகின்றன.", voiceSoon:"FarmAgent-இடம் சொல்லுங்கள்<br><small>விரைவில் வரும்</small>",
    photoQuestion:"புகைப்படம் எடுக்கவும் (விருப்பம்)", optional:"விருப்பம்", photoHelp:"பயிர் பிரச்சினையை அடையாளம் காண புகைப்படம் உதவலாம்.", takePhoto:"செடியின் புகைப்படம் எடுக்கவும்", uploadPhoto:"புகைப்படத்தைப் பதிவேற்றவும்", photoNotAnalyzed:"புகைப்பட ஆய்வு இன்னும் இல்லை. உங்கள் படம் பதிவேற்றப்படவோ ஆய்வு செய்யப்படவோ மாட்டாது.",
    soilQuestion:"மண் எப்படி தெரிகிறது அல்லது உணரப்படுகிறது?", soilVeryDry:"மிகவும் வறண்டு", soilSlightlyDry:"சற்று வறண்டு", soilNormal:"சாதாரணம்", soilWet:"ஈரமாக", soilVeryWet:"மிகவும் ஈரமாக", dontKnow:"தெரியவில்லை", notSure:"தெரியாவிட்டாலும் பரவாயில்லை.", waterQuestion:"சமீபத்தில் மழை பெய்ததா?", yes:"ஆம்", no:"இல்லை", lastWatered:"கடைசியாக எப்போது நீர் பாய்ச்சினீர்கள்?", today:"இன்று", yesterday:"நேற்று", twoThreeDays:"2–3 நாட்களுக்கு முன்", moreThreeDays:"3 நாட்களுக்கு மேல்", dontRemember:"நினைவில்லை",
    locationQuestion:"உங்கள் வயல் எங்கே? (விருப்பம்)", useLocation:"என் இருப்பிடத்தைப் பயன்படுத்து", or:"அல்லது", villageTown:"கிராமம் / நகரம்", villagePlaceholder:"கிராமம் / நகரம்", locationOptional:"இருப்பிடம் விருப்பம். வானிலையைப் பார்க்க மட்டுமே பயன்படுத்தப்படும்.", locationGetting:"இருப்பிடத்தைப் பெறுகிறோம்…", locationSet:"இருப்பிடம் சேர்க்கப்பட்டது.", locationFailed:"இருப்பிடத்தைப் பெற முடியவில்லை. உங்கள் ஊரை எழுதலாம்.",
    moreDetails:"மேலும் விவரங்கள் (விருப்பம்)", advancedHelp:"உங்களுக்குத் தெரிந்ததை மட்டும் நிரப்பவும். இவை அவசியமில்லை.", growthStage:"பயிர் வளர்ச்சி நிலை", growthPlaceholder:"எ.கா., பூக்கும் நிலை", soilType:"மண் வகை", soilMoisture:"மண் ஈரப்பதம் (%)", rainfall:"சமீபத்திய மழை (மி.மீ.)", temperature:"வெப்பநிலை (°C)", otherInfo:"மற்ற தகவல்", weatherDemo:"வானிலை மாதிரி (செயல்முறை விளக்கம்)", advancedDemoWarning:"வானிலைத் தேர்வுகள் மாதிரிகள்; உண்மையான முன்னறிவிப்பு அல்ல.", privacyNote:"சரியான அளவீடுகளைப் பகிர வேண்டியதில்லை.", analyze:"என் பயிரை ஆய்வு செய்",
    working:"FarmAgent இதைப் பார்க்கிறது…", progressUnderstand:"🔍 உங்கள் சிக்கலைப் புரிந்துகொள்கிறது…", progressCrop:"🌱 பயிர் நலத்தைப் பார்க்கிறது…", progressWater:"💧 நீர் தேவையைப் பார்க்கிறது…", progressWeather:"🌦️ வானிலையைப் பார்க்கிறது…", progressRisk:"🛡️ ஆபத்துகளைப் பார்க்கிறது…", progressDebate:"⚔️ ஆலோசனைகளை ஒப்பிடுகிறது…",
    yourResult:"FARMAGENT ஆலோசனை", resultTitle:"நாங்கள் கண்டறிந்தது", whatFound:"நாங்கள் கண்டறிந்தது", whatToDo:"நீங்கள் செய்ய வேண்டியது", beCareful:"கவனமாக இருங்கள்", watchFor:"கவனிக்க வேண்டியவை", whyTitle:"FarmAgent ஏன் இப்படிச் சொல்கிறது", debateTitle:"முகவர்களின் விவாதம்", tapToExpand:"ஆலோசனைகள் எப்படிப் பகிரப்பட்டன என்று அழுத்திப் பார்க்கவும்", finalChoice:"FarmAgent-இன் இறுதி தேர்வு", defendNote:"பல்வேறு ஆலோசனைகளை ஒப்பிட்டு பாதுகாப்பான அடுத்த படியை FarmAgent தேர்ந்தெடுத்தது.", weatherDemoNotice:"வானிலைத் தகவல் மாதிரி மட்டுமே; நேரடி அளவீடு அல்லது முன்னறிவிப்பு அல்ல.", footer:"சிறந்த முடிவெடுக்க FarmAgent உதவும். தீவிரப் பிரச்சினைக்கு உள்ளூர் வேளாண் நிபுணரை அணுகவும்.", confidenceHigh:"🟢 அதிக நம்பிக்கை — உங்கள் கவனிப்புகள் தெளிவான நிலையை காட்டுகின்றன.", confidenceMedium:"🟡 நடுத்தர நம்பிக்கை — கூடுதல் விவரம் அல்லது தெளிவான படம் உதவும்.", confidenceLow:"🔴 குறைந்த நம்பிக்கை — உறுதிப்படுத்த கூடுதல் தகவல் தேவை.", missingAdvice:"தெளிவான பதிலுக்கு போதிய தகவல் இல்லை. பிரச்சினையை விவரிக்கவும் அல்லது மேலே தேர்ந்தெடுக்கவும்."
  },
  ml: {
    language:"ഭാഷ", welcomeEyebrow:"ഓരോ കർഷകനും ഒരു കൈത്താങ്ങ്", welcomeSubtitle:"വിളയ്ക്ക് എന്താണ് സംഭവിക്കുന്നതെന്ന് പറയൂ. എന്ത് ചെയ്യണമെന്ന് മനസ്സിലാക്കാൻ ഞങ്ങൾ സഹായിക്കും.", develop:"മനസ്സിലാക്കുക", developDesc:"പ്രശ്നം അറിയുക", debate:"ചർച്ച ചെയ്യുക", debateDesc:"നിർദേശങ്ങൾ താരതമ്യം", defend:"വിശദീകരിക്കുക", defendDesc:"കാരണം പറയുക",
    demoKicker:"FARMAGENT പരീക്ഷിക്കൂ", demoTitle:"ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു", demoHelp:"ഡെമോ കാണാൻ ഒരു പ്രശ്നം തിരഞ്ഞെടുക്കൂ.", demoTomato:"എന്റെ തക്കാളിയിലകൾ ചുരുളുന്നു", demoDry:"എന്റെ വിള ഉണങ്ങിയിരിക്കുന്നു", demoInsects:"ഇലകളിൽ കീടങ്ങളെ കാണുന്നു", demoWet:"വയലിൽ വെള്ളം കൂടുതലാണ്", demoNote:"ഡെമോയിലെ കാലാവസ്ഥ മാതൃക മാത്രമാണ്; യഥാർത്ഥ അളവല്ല.",
    intakeKicker:"നിങ്ങളുടെ വിള", intakeTitle:"നിങ്ങൾ എന്താണ് കാണുന്നത്?", optionalNote:"അറിയാത്ത കാര്യങ്ങൾ ഒഴിവാക്കാം.", cropQuestion:"നിങ്ങൾ എന്താണ് കൃഷി ചെയ്യുന്നത്?", cropTomato:"തക്കാളി", cropRice:"നെല്ല്", cropMaize:"ചോളം", cropPotato:"ഉരുളക്കിഴങ്ങ്", cropChilli:"മുളക്", cropGroundnut:"നിലക്കടല", cropOther:"മറ്റുള്ളവ", typeCrop:"വിളയുടെ പേര് എഴുതൂ", cropPlaceholder:"ഉദാ: ഉള്ളി",
    problemQuestion:"എന്താണ് പ്രശ്നം?", problemThirsty:"ചെടിക്ക് ദാഹിക്കുന്നതുപോലെ", problemYellow:"ഇലകൾ മഞ്ഞളിക്കുന്നു", problemCurling:"ഇലകൾ ചുരുളുന്നു", problemInsects:"കീടങ്ങളെ കാണുന്നു", problemDisease:"ചെടിക്ക് രോഗമുണ്ടാകാം", problemGrowth:"ചെടി നന്നായി വളരുന്നില്ല", problemWet:"വെള്ളം കൂടുതലാണ്", problemHeat:"ചൂട് കൂടുതലാണ്", problemUnknown:"അറിയില്ല", describeLabel:"നിങ്ങളുടെ വാക്കുകളിൽ പ്രശ്നം പറയൂ", describePlaceholder:"എന്റെ തക്കാളിയിലകൾ ചുരുളുന്നു; ചെടികൾ ദുർബലമായി തോന്നുന്നു.", voiceSoon:"FarmAgent-നോട് പറയൂ<br><small>ഉടൻ വരുന്നു</small>",
    photoQuestion:"ഫോട്ടോ എടുക്കൂ (വേണമെങ്കിൽ)", optional:"ഐച്ഛികം", photoHelp:"വിളയുടെ പ്രശ്നം കണ്ടെത്താൻ ഫോട്ടോ സഹായിച്ചേക്കാം.", takePhoto:"ചെടിയുടെ ഫോട്ടോ എടുക്കൂ", uploadPhoto:"ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യൂ", photoNotAnalyzed:"ഫോട്ടോ പരിശോധിക്കുന്ന സൗകര്യം ഇപ്പോൾ ഇല്ല. ചിത്രം അപ്‌ലോഡ് ചെയ്യുകയോ പരിശോധിക്കുകയോ ചെയ്യില്ല.",
    soilQuestion:"മണ്ണ് എങ്ങനെ കാണപ്പെടുന്നു അല്ലെങ്കിൽ തോന്നുന്നു?", soilVeryDry:"വളരെ വരണ്ടത്", soilSlightlyDry:"അല്പം വരണ്ടത്", soilNormal:"സാധാരണം", soilWet:"നനഞ്ഞത്", soilVeryWet:"വളരെ നനഞ്ഞത്", dontKnow:"അറിയില്ല", notSure:"ഉറപ്പില്ലേ? കുഴപ്പമില്ല.", waterQuestion:"അടുത്തിടെ മഴ പെയ്തോ?", yes:"അതെ", no:"ഇല്ല", lastWatered:"അവസാനമായി വിളയ്ക്ക് വെള്ളം നൽകിയത് എപ്പോൾ?", today:"ഇന്ന്", yesterday:"ഇന്നലെ", twoThreeDays:"2–3 ദിവസം മുമ്പ്", moreThreeDays:"3 ദിവസത്തിലധികം മുമ്പ്", dontRemember:"ഓർമ്മയില്ല",
    locationQuestion:"നിങ്ങളുടെ കൃഷിയിടം എവിടെയാണ്? (ഐച്ഛികം)", useLocation:"എന്റെ സ്ഥലം ഉപയോഗിക്കുക", or:"അല്ലെങ്കിൽ", villageTown:"ഗ്രാമം / പട്ടണം", villagePlaceholder:"ഗ്രാമം / പട്ടണം", locationOptional:"സ്ഥലം നൽകേണ്ടതില്ല. കാലാവസ്ഥ അറിയാൻ മാത്രം ഉപയോഗിക്കും.", locationGetting:"സ്ഥലം കണ്ടെത്തുന്നു…", locationSet:"സ്ഥലം ചേർത്തു.", locationFailed:"സ്ഥലം കണ്ടെത്താനായില്ല. ഗ്രാമമോ പട്ടണമോ എഴുതാം.",
    moreDetails:"കൂടുതൽ വിവരങ്ങൾ (ഐച്ഛികം)", advancedHelp:"അറിയാവുന്ന കാര്യങ്ങൾ മാത്രം നൽകുക. ഇവ ആവശ്യമില്ല.", growthStage:"വളർച്ചാ ഘട്ടം", growthPlaceholder:"ഉദാ: പൂക്കുന്ന ഘട്ടം", soilType:"മണ്ണിന്റെ തരം", soilMoisture:"മണ്ണിലെ ഈർപ്പം (%)", rainfall:"അടുത്തിടെയുള്ള മഴ (മി.മീ.)", temperature:"താപനില (°C)", otherInfo:"മറ്റ് വിവരങ്ങൾ", weatherDemo:"കാലാവസ്ഥ മാതൃക (ഡെമോ മാത്രം)", advancedDemoWarning:"കാലാവസ്ഥാ തിരഞ്ഞെടുപ്പുകൾ മാതൃകയാണ്; യഥാർത്ഥ പ്രവചനമല്ല.", privacyNote:"കൃത്യമായ അളവുകൾ നൽകേണ്ടതില്ല.", analyze:"എന്റെ വിള പരിശോധിക്കുക",
    working:"FarmAgent പരിശോധിക്കുന്നു…", progressUnderstand:"🔍 പ്രശ്നം മനസ്സിലാക്കുന്നു…", progressCrop:"🌱 വിളയുടെ ആരോഗ്യം പരിശോധിക്കുന്നു…", progressWater:"💧 വെള്ളത്തിന്റെ ആവശ്യം പരിശോധിക്കുന്നു…", progressWeather:"🌦️ കാലാവസ്ഥ പരിശോധിക്കുന്നു…", progressRisk:"🛡️ അപകടസാധ്യത പരിശോധിക്കുന്നു…", progressDebate:"⚔️ നിർദേശങ്ങൾ താരതമ്യം ചെയ്യുന്നു…",
    yourResult:"FARMAGENT നിർദേശം", resultTitle:"ഞങ്ങൾ കണ്ടെത്തിയത്", whatFound:"ഞങ്ങൾ കണ്ടെത്തിയത്", whatToDo:"നിങ്ങൾ ചെയ്യേണ്ടത്", beCareful:"ശ്രദ്ധിക്കുക", watchFor:"ശ്രദ്ധിക്കേണ്ടത്", whyTitle:"FarmAgent ഇങ്ങനെ കരുതുന്നത് എന്തുകൊണ്ട്", debateTitle:"ഏജന്റുമാരുടെ ചർച്ച", tapToExpand:"നിർദേശങ്ങൾ എങ്ങനെ താരതമ്യം ചെയ്തെന്ന് കാണാൻ അമർത്തുക", finalChoice:"FarmAgent-ന്റെ അന്തിമ നിർദേശം", defendNote:"വ്യത്യസ്ത നിർദേശങ്ങൾ താരതമ്യം ചെയ്ത് സുരക്ഷിതമായ അടുത്ത നടപടി FarmAgent തിരഞ്ഞെടുത്തു.", weatherDemoNotice:"കാലാവസ്ഥാ വിവരം മാതൃക മാത്രമാണ്; തത്സമയ അളവോ പ്രവചനമോ അല്ല.", footer:"കൂടുതൽ അറിവോടെ തീരുമാനമെടുക്കാൻ FarmAgent സഹായിക്കുന്നു. ഗുരുതര പ്രശ്നങ്ങൾക്ക് പ്രാദേശിക കൃഷി വിദഗ്ധനോട് ചോദിക്കുക.", confidenceHigh:"🟢 ഉയർന്ന വിശ്വാസം — നിങ്ങൾ നൽകിയ വിവരം വ്യക്തമാണ്.", confidenceMedium:"🟡 മിതമായ വിശ്വാസം — കൂടുതൽ വിവരമോ വ്യക്തമായ ഫോട്ടോയോ സഹായിക്കും.", confidenceLow:"🔴 കുറഞ്ഞ വിശ്വാസം — ഉറപ്പിക്കാൻ കൂടുതൽ വിവരം ആവശ്യമാണ്.", missingAdvice:"വ്യക്തമായ മറുപടിക്ക് മതിയായ വിവരമില്ല. പ്രശ്നം വിവരിക്കുകയോ മുകളിലെ തിരഞ്ഞെടുപ്പ് എടുക്കുകയോ ചെയ്യൂ."
  },
  kn: {
    language:"ಭಾಷೆ", welcomeEyebrow:"ಪ್ರತಿ ರೈತನಿಗೆ ಸಹಾಯ", welcomeSubtitle:"ನಿಮ್ಮ ಬೆಳೆಗೆ ಏನಾಗುತ್ತಿದೆ ಎಂದು ತಿಳಿಸಿ. ಏನು ಮಾಡಬೇಕು ಎಂದು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತೇವೆ.", develop:"ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ", developDesc:"ಸಮಸ್ಯೆ ತಿಳಿಯಿರಿ", debate:"ಚರ್ಚಿಸಿ", debateDesc:"ಸಲಹೆ ಹೋಲಿಸಿ", defend:"ವಿವರಿಸಿ", defendDesc:"ಕಾರಣ ತಿಳಿಸಿ",
    demoKicker:"FARMAGENT ಪ್ರಯತ್ನಿಸಿ", demoTitle:"ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ನೋಡಿ", demoHelp:"ಡೆಮೋಗಾಗಿ ಒಂದು ಸಮಸ್ಯೆ ಆಯ್ಕೆಮಾಡಿ.", demoTomato:"ನನ್ನ ಟೊಮೇಟೊ ಎಲೆಗಳು ಮುದುಡುತ್ತಿವೆ", demoDry:"ನನ್ನ ಬೆಳೆ ಒಣಗಿದಂತೆ ಕಾಣುತ್ತದೆ", demoInsects:"ಎಲೆಗಳ ಮೇಲೆ ಕೀಟಗಳಿವೆ", demoWet:"ನನ್ನ ಹೊಲದಲ್ಲಿ ನೀರು ಹೆಚ್ಚಾಗಿದೆ", demoNote:"ಡೆಮೋದಲ್ಲಿ ಮಾದರಿ ಹವಾಮಾನವಿದೆ; ನಿಜವಾದ ಅಳತೆಗಳಿಲ್ಲ.",
    intakeKicker:"ನಿಮ್ಮ ಬೆಳೆ", intakeTitle:"ನೀವು ಏನು ಗಮನಿಸುತ್ತಿದ್ದೀರಿ?", optionalNote:"ತಿಳಿಯದಿದ್ದರೆ ಬಿಟ್ಟುಬಿಡಿ.", cropQuestion:"ನೀವು ಏನು ಬೆಳೆಯುತ್ತಿದ್ದೀರಿ?", cropTomato:"ಟೊಮೇಟೊ", cropRice:"ಭತ್ತ", cropMaize:"ಮೆಕ್ಕೆಜೋಳ", cropPotato:"ಆಲೂಗಡ್ಡೆ", cropChilli:"ಮೆಣಸಿನಕಾಯಿ", cropGroundnut:"ಕಡಲೆಕಾಯಿ", cropOther:"ಇತರೆ", typeCrop:"ನಿಮ್ಮ ಬೆಳೆಯ ಹೆಸರನ್ನು ಬರೆಯಿರಿ", cropPlaceholder:"ಉದಾ: ಈರುಳ್ಳಿ",
    problemQuestion:"ಸಮಸ್ಯೆ ಏನು?", problemThirsty:"ಗಿಡಕ್ಕೆ ನೀರು ಬೇಕೆನಿಸುತ್ತದೆ", problemYellow:"ಎಲೆಗಳು ಹಳದಿಯಾಗುತ್ತಿವೆ", problemCurling:"ಎಲೆಗಳು ಮುದುಡುತ್ತಿವೆ", problemInsects:"ಕೀಟಗಳು ಕಾಣುತ್ತಿವೆ", problemDisease:"ಗಿಡಕ್ಕೆ ರೋಗವಿರಬಹುದು", problemGrowth:"ಗಿಡ ಚೆನ್ನಾಗಿ ಬೆಳೆಯುತ್ತಿಲ್ಲ", problemWet:"ನೀರು ಹೆಚ್ಚಾಗಿದೆ", problemHeat:"ಬಿಸಿಲು ಹೆಚ್ಚಾಗಿದೆ", problemUnknown:"ಗೊತ್ತಿಲ್ಲ", describeLabel:"ನಿಮ್ಮ ಮಾತಿನಲ್ಲಿ ಸಮಸ್ಯೆ ತಿಳಿಸಿ", describePlaceholder:"ನನ್ನ ಟೊಮೇಟೊ ಎಲೆಗಳು ಮುದುಡುತ್ತಿವೆ ಮತ್ತು ಗಿಡಗಳು ದುರ್ಬಲವಾಗಿವೆ.", voiceSoon:"FarmAgent‌ಗೆ ತಿಳಿಸಿ<br><small>ಶೀಘ್ರದಲ್ಲೇ</small>",
    photoQuestion:"ಫೋಟೋ ತೆಗೆಯಿರಿ (ಐಚ್ಛಿಕ)", optional:"ಐಚ್ಛಿಕ", photoHelp:"ಬೆಳೆ ಸಮಸ್ಯೆ ಗುರುತಿಸಲು ಫೋಟೋ ಸಹಾಯ ಮಾಡಬಹುದು.", takePhoto:"ಗಿಡದ ಫೋಟೋ ತೆಗೆಯಿರಿ", uploadPhoto:"ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ", photoNotAnalyzed:"ಫೋಟೋ ಪರಿಶೀಲನೆ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ. ನಿಮ್ಮ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಅಥವಾ ವಿಶ್ಲೇಷಣೆ ಆಗುವುದಿಲ್ಲ.",
    soilQuestion:"ಮಣ್ಣು ಹೇಗೆ ಕಾಣುತ್ತದೆ ಅಥವಾ ಅನಿಸುತ್ತದೆ?", soilVeryDry:"ತುಂಬಾ ಒಣ", soilSlightlyDry:"ಸ್ವಲ್ಪ ಒಣ", soilNormal:"ಸಾಮಾನ್ಯ", soilWet:"ಒದ್ದೆ", soilVeryWet:"ತುಂಬಾ ಒದ್ದೆ", dontKnow:"ಗೊತ್ತಿಲ್ಲ", notSure:"ಖಚಿತವಿಲ್ಲವೇ? ಪರವಾಗಿಲ್ಲ.", waterQuestion:"ಇತ್ತೀಚೆಗೆ ಮಳೆ ಬಂದಿದೆಯೇ?", yes:"ಹೌದು", no:"ಇಲ್ಲ", lastWatered:"ಬೆಳೆಗೆ ಕೊನೆಯ ಬಾರಿ ನೀರು ಹಾಕಿದ್ದು ಯಾವಾಗ?", today:"ಇಂದು", yesterday:"ನಿನ್ನೆ", twoThreeDays:"2–3 ದಿನಗಳ ಹಿಂದೆ", moreThreeDays:"3 ದಿನಗಳಿಗಿಂತ ಹಿಂದೆ", dontRemember:"ನೆನಪಿಲ್ಲ",
    locationQuestion:"ನಿಮ್ಮ ಹೊಲ ಎಲ್ಲಿದೆ? (ಐಚ್ಛಿಕ)", useLocation:"ನನ್ನ ಸ್ಥಳ ಬಳಸಿ", or:"ಅಥವಾ", villageTown:"ಹಳ್ಳಿ / ಪಟ್ಟಣ", villagePlaceholder:"ಹಳ್ಳಿ / ಪಟ್ಟಣ", locationOptional:"ಸ್ಥಳ ನೀಡುವುದು ಐಚ್ಛಿಕ. ಹವಾಮಾನ ನೋಡಲು ಮಾತ್ರ ಬಳಸುತ್ತೇವೆ.", locationGetting:"ನಿಮ್ಮ ಸ್ಥಳ ಪಡೆಯುತ್ತಿದ್ದೇವೆ…", locationSet:"ಸ್ಥಳ ಸೇರಿಸಲಾಗಿದೆ.", locationFailed:"ಸ್ಥಳ ಪಡೆಯಲಾಗಲಿಲ್ಲ. ನಿಮ್ಮ ಹಳ್ಳಿ ಅಥವಾ ಪಟ್ಟಣ ಬರೆಯಿರಿ.",
    moreDetails:"ಹೆಚ್ಚಿನ ವಿವರಗಳು (ಐಚ್ಛಿಕ)", advancedHelp:"ನಿಮಗೆ ತಿಳಿದಿರುವ ವಿವರಗಳನ್ನು ಮಾತ್ರ ನೀಡಿ. ಇವು ಅಗತ್ಯವಿಲ್ಲ.", growthStage:"ಬೆಳೆಯ ಹಂತ", growthPlaceholder:"ಉದಾ: ಹೂ ಬಿಡುವ ಹಂತ", soilType:"ಮಣ್ಣಿನ ವಿಧ", soilMoisture:"ಮಣ್ಣಿನ ತೇವಾಂಶ (%)", rainfall:"ಇತ್ತೀಚಿನ ಮಳೆ (ಮಿಮೀ)", temperature:"ತಾಪಮಾನ (°C)", otherInfo:"ಇತರೆ ಮಾಹಿತಿ", weatherDemo:"ಹವಾಮಾನ ಮಾದರಿ (ಡೆಮೋ ಮಾತ್ರ)", advancedDemoWarning:"ಹವಾಮಾನ ಆಯ್ಕೆಗಳು ಮಾದರಿಗಳು; ನಿಜವಾದ ಮುನ್ಸೂಚನೆಗಳಲ್ಲ.", privacyNote:"ನಿಖರ ಅಳತೆಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳಬೇಕಾಗಿಲ್ಲ.", analyze:"ನನ್ನ ಬೆಳೆಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ",
    working:"FarmAgent ಪರಿಶೀಲಿಸುತ್ತಿದೆ…", progressUnderstand:"🔍 ಸಮಸ್ಯೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತಿದೆ…", progressCrop:"🌱 ಬೆಳೆಯ ಆರೋಗ್ಯ ನೋಡುತ್ತಿದೆ…", progressWater:"💧 ನೀರಿನ ಅಗತ್ಯ ನೋಡುತ್ತಿದೆ…", progressWeather:"🌦️ ಹವಾಮಾನ ನೋಡುತ್ತಿದೆ…", progressRisk:"🛡️ ಅಪಾಯ ಪರಿಶೀಲಿಸುತ್ತಿದೆ…", progressDebate:"⚔️ ಸಲಹೆಗಳನ್ನು ಹೋಲಿಸುತ್ತಿದೆ…",
    yourResult:"FARMAGENT ಸಲಹೆ", resultTitle:"ನಾವು ಕಂಡುಕೊಂಡದ್ದು", whatFound:"ನಾವು ಕಂಡುಕೊಂಡದ್ದು", whatToDo:"ನೀವು ಮಾಡಬೇಕಾದದ್ದು", beCareful:"ಎಚ್ಚರಿಕೆ", watchFor:"ಗಮನಿಸಬೇಕಾದದ್ದು", whyTitle:"FarmAgent ಹೀಗೆ ಯೋಚಿಸುವುದೇಕೆ", debateTitle:"ಏಜೆಂಟ್ ಚರ್ಚೆ", tapToExpand:"ಸಲಹೆಗಳನ್ನು ಹೇಗೆ ಹೋಲಿಸಲಾಗಿದೆ ಎಂದು ಒತ್ತಿ ನೋಡಿ", finalChoice:"FarmAgent ಅಂತಿಮ ಆಯ್ಕೆ", defendNote:"ವಿವಿಧ ಸಲಹೆಗಳನ್ನು ಹೋಲಿಸಿ ಸುರಕ್ಷಿತ ಮುಂದಿನ ಹೆಜ್ಜೆಯನ್ನು FarmAgent ಆಯ್ಕೆಮಾಡಿದೆ.", weatherDemoNotice:"ಹವಾಮಾನ ಮಾಹಿತಿ ಮಾದರಿ ಮಾತ್ರ; ನೇರ ಅಳತೆ ಅಥವಾ ಮುನ್ಸೂಚನೆ ಅಲ್ಲ.", footer:"ಉತ್ತಮ ನಿರ್ಧಾರಕ್ಕೆ FarmAgent ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಗಂಭೀರ ಸಮಸ್ಯೆಗೆ ಸ್ಥಳೀಯ ಕೃಷಿ ತಜ್ಞರನ್ನು ಸಂಪರ್ಕಿಸಿ.", confidenceHigh:"🟢 ಹೆಚ್ಚಿನ ವಿಶ್ವಾಸ — ನಿಮ್ಮ ಗಮನಿಸಿದ ವಿವರಗಳು ಸ್ಪಷ್ಟವಾಗಿವೆ.", confidenceMedium:"🟡 ಮಧ್ಯಮ ವಿಶ್ವಾಸ — ಹೆಚ್ಚಿನ ಮಾಹಿತಿ ಅಥವಾ ಸ್ಪಷ್ಟ ಫೋಟೋ ಸಹಾಯ ಮಾಡಬಹುದು.", confidenceLow:"🔴 ಕಡಿಮೆ ವಿಶ್ವಾಸ — ಖಚಿತಪಡಿಸಲು ಹೆಚ್ಚಿನ ಮಾಹಿತಿ ಬೇಕು.", missingAdvice:"ಸ್ಪಷ್ಟ ಉತ್ತರಕ್ಕೆ ಸಾಕಷ್ಟು ಮಾಹಿತಿ ಇಲ್ಲ. ಸಮಸ್ಯೆ ವಿವರಿಸಿ ಅಥವಾ ಮೇಲಿನ ಆಯ್ಕೆ ಆರಿಸಿ."
  },
  mr: {
    language:"भाषा", welcomeEyebrow:"प्रत्येक शेतकऱ्यासाठी मदत", welcomeSubtitle:"तुमच्या पिकाला काय होत आहे ते सांगा. काय करावे हे समजून घेण्यास आम्ही मदत करू.", develop:"समजून घ्या", developDesc:"समस्या ओळखा", debate:"तुलना करा", debateDesc:"सल्ले तपासा", defend:"समजावून सांगा", defendDesc:"कारण सांगा",
    demoKicker:"FARMAGENT वापरून पाहा", demoTitle:"हे कसे काम करते ते पाहा", demoHelp:"डेमोसाठी एक समस्या निवडा.", demoTomato:"माझ्या टोमॅटोची पाने गुंडाळत आहेत", demoDry:"माझे पीक कोरडे दिसते", demoInsects:"पानांवर कीटक दिसतात", demoWet:"माझ्या शेतात जास्त पाणी आहे", demoNote:"डेमोमध्ये नमुना हवामान वापरले आहे; शेतातील खरी मोजमापे नाहीत.",
    intakeKicker:"तुमचे पीक", intakeTitle:"तुम्हाला काय दिसत आहे?", optionalNote:"माहिती नसेल तर तो प्रश्न सोडू शकता.", cropQuestion:"तुम्ही काय पिकवत आहात?", cropTomato:"टोमॅटो", cropRice:"भात", cropMaize:"मका", cropPotato:"बटाटा", cropChilli:"मिरची", cropGroundnut:"भुईमूग", cropOther:"इतर", typeCrop:"तुमच्या पिकाचे नाव लिहा", cropPlaceholder:"उदा. कांदा",
    problemQuestion:"काय समस्या आहे?", problemThirsty:"झाडाला पाणी हवे आहे असे वाटते", problemYellow:"पाने पिवळी पडत आहेत", problemCurling:"पाने गुंडाळत आहेत", problemInsects:"कीटक दिसत आहेत", problemDisease:"झाडाला रोग असू शकतो", problemGrowth:"झाडाची वाढ चांगली नाही", problemWet:"पाणी खूप जास्त आहे", problemHeat:"उष्णता खूप आहे", problemUnknown:"माहित नाही", describeLabel:"समस्या तुमच्या शब्दांत सांगा", describePlaceholder:"माझ्या टोमॅटोची पाने गुंडाळत आहेत आणि झाडे कमकुवत दिसतात.", voiceSoon:"FarmAgent ला सांगा<br><small>लवकरच येत आहे</small>",
    photoQuestion:"फोटो काढा (ऐच्छिक)", optional:"ऐच्छिक", photoHelp:"फोटोमुळे FarmAgent ला पिकाची समस्या ओळखण्यास मदत होऊ शकते.", takePhoto:"झाडाचा फोटो काढा", uploadPhoto:"फोटो अपलोड करा", photoNotAnalyzed:"फोटो तपासण्याची सुविधा अजून नाही. तुमचा फोटो अपलोड किंवा तपासला जाणार नाही.",
    soilQuestion:"माती कशी दिसते किंवा लागते?", soilVeryDry:"खूप कोरडी", soilSlightlyDry:"थोडी कोरडी", soilNormal:"सामान्य", soilWet:"ओली", soilVeryWet:"खूप ओली", dontKnow:"माहित नाही", notSure:"खात्री नाही? काही हरकत नाही.", waterQuestion:"अलीकडे पाऊस झाला का?", yes:"हो", no:"नाही", lastWatered:"पिकाला शेवटचे पाणी कधी दिले?", today:"आज", yesterday:"काल", twoThreeDays:"2–3 दिवसांपूर्वी", moreThreeDays:"3 दिवसांपूर्वीपेक्षा जास्त", dontRemember:"आठवत नाही",
    locationQuestion:"तुमचे शेत कुठे आहे? (ऐच्छिक)", useLocation:"माझे ठिकाण वापरा", or:"किंवा", villageTown:"गाव / शहर", villagePlaceholder:"गाव / शहर", locationOptional:"ठिकाण देणे ऐच्छिक आहे. ते फक्त हवामान पाहण्यासाठी वापरले जाईल.", locationGetting:"तुमचे ठिकाण घेत आहोत…", locationSet:"ठिकाण जोडले.", locationFailed:"ठिकाण मिळाले नाही. गाव किंवा शहर लिहू शकता.",
    moreDetails:"अधिक माहिती (ऐच्छिक)", advancedHelp:"तुम्हाला आधीपासून माहीत असलेली माहितीच द्या. ही माहिती आवश्यक नाही.", growthStage:"पिकाची वाढीची अवस्था", growthPlaceholder:"उदा. फुलोरा", soilType:"मातीचा प्रकार", soilMoisture:"मातीतील ओलावा (%)", rainfall:"अलीकडील पाऊस (मिमी)", temperature:"तापमान (°C)", otherInfo:"इतर माहिती", weatherDemo:"हवामान नमुना (फक्त डेमो)", advancedDemoWarning:"हवामानाचे पर्याय नमुने आहेत; खरा अंदाज नाही.", privacyNote:"अचूक मोजमाप सांगण्याची गरज नाही.", analyze:"माझ्या पिकाचे विश्लेषण करा",
    working:"FarmAgent तपासत आहे…", progressUnderstand:"🔍 समस्या समजून घेत आहे…", progressCrop:"🌱 पिकाची तब्येत तपासत आहे…", progressWater:"💧 पाण्याची गरज तपासत आहे…", progressWeather:"🌦️ हवामान तपासत आहे…", progressRisk:"🛡️ धोके तपासत आहे…", progressDebate:"⚔️ सल्ल्यांची तुलना करत आहे…",
    yourResult:"FARMAGENT चा सल्ला", resultTitle:"आम्हाला हे आढळले", whatFound:"आम्हाला काय आढळले", whatToDo:"तुम्ही काय करावे", beCareful:"काळजी घ्या", watchFor:"कशाकडे लक्ष द्यावे", whyTitle:"FarmAgent असे का म्हणते", debateTitle:"एजंटमधील चर्चा", tapToExpand:"सल्ल्यांची तुलना पाहण्यासाठी दाबा", finalChoice:"FarmAgent ची अंतिम निवड", defendNote:"वेगवेगळ्या सल्ल्यांची तुलना करून FarmAgent ने सुरक्षित पुढचे पाऊल निवडले.", weatherDemoNotice:"हवामानाची माहिती नमुना आहे; थेट मोजमाप किंवा अंदाज नाही.", footer:"अधिक माहितीपूर्ण निर्णयासाठी FarmAgent मदत करते. गंभीर समस्येसाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.", confidenceHigh:"🟢 जास्त विश्वास — तुमच्या निरीक्षणांमुळे परिस्थिती स्पष्ट आहे.", confidenceMedium:"🟡 मध्यम विश्वास — अधिक माहिती किंवा स्पष्ट फोटो मदत करू शकतो.", confidenceLow:"🔴 कमी विश्वास — खात्रीसाठी अधिक माहिती हवी.", missingAdvice:"स्पष्ट उत्तरासाठी पुरेशी माहिती नाही. कृपया समस्या सांगा किंवा वरील पर्याय निवडा."
  }
};

const farmerResultTranslations = {
  te: {
    crops: { tomato: "టమాటా", rice: "వరి", corn: "మొక్కజొన్న", maize: "మొక్కజొన్న", potato: "బంగాళాదుంప", chilli: "మిరప", groundnut: "వేరుశనగ", other: "పంట", "general crop": "పంట" },
    findings: {
      too_wet: "{crop}కు నీరు ఎక్కువగా అందుతున్నట్లు ఉండవచ్చు. మట్టి ఎప్పుడూ తడిగా ఉంటే వేర్లు దెబ్బతినవచ్చు.",
      sample_rain: "ఈ తనిఖీలో ఉపయోగించిన నమూనా వాతావరణంలో వర్షం వచ్చే సూచన ఉంది. నీరు పెట్టే ముందు మీ ప్రాంత వాతావరణాన్ని చూడండి.",
      rain_check: "త్వరలో వర్షం రావచ్చు. {crop}కు నీరు పెట్టే ముందు మీ ప్రాంత వాతావరణం మరియు మట్టిని చూడండి.",
      needs_water: "{crop}కు నీరు అవసరం కావచ్చు. మట్టి చాలా ఎండిపోయిందని మీరు తెలిపారు.",
      yellow_leaves: "ఆకులు పసుపు రంగులోకి మారడానికి నీరు, పురుగులు, వ్యాధి లేదా మట్టి పోషకాలు కారణం కావచ్చు. ఈ సమాచారంతో ఖచ్చితమైన కారణం చెప్పలేము.",
      possible_leaf_issue: "{crop} ఆకులకు సమస్య ఉండవచ్చు. ఇది వ్యాధా లేదా పురుగు నష్టమా అనేది ఈ వివరణతో మాత్రమే నిర్ధారించలేము.",
      unclear: "{crop} సమస్యకు కారణం తెలుసుకోవడానికి ఇంకా సమాచారం అవసరం."
    },
    actions: {
      stop_water: ["మట్టి చాలా తడిగా ఉన్నప్పుడు మరింత నీరు పెట్టవద్దు.", "నీరు నిలిచివుంటే మొక్కల నుంచి బయటకు వెళ్లేలా చేయండి.", "అదనపు నీరు వెళ్లిపోయిన తర్వాత మట్టిని మళ్లీ చూడండి."],
      wait_rain: ["నీరు పెట్టే ముందు ఆగి, మీ ప్రాంత వాతావరణాన్ని చూడండి.", "పొలంలో అదనపు నీరు వెళ్లేందుకు దారి ఉందని చూసుకోండి.", "వర్షం పడితే, ఆగిన తర్వాత మట్టిని మళ్లీ చూడండి."],
      water_once: ["చల్లని ఉదయం లేదా సాయంత్రం ఒకసారి నీరు పెట్టండి.", "పైపైన కాకుండా మొక్క చుట్టూ మట్టికి నీరు పెట్టండి.", "మళ్లీ నీరు పెట్టే ముందు మట్టిని చూడండి."],
      check_yellow: ["ఆకుల రెండు వైపులా పురుగులు లేదా మచ్చలు ఉన్నాయో చూడండి.", "మట్టి చాలా ఎండిపోయిందా లేదా ఎప్పుడూ తడిగా ఉందా గమనించండి.", "ఎరువు వేయడానికి ముందు స్థానిక వ్యవసాయ నిపుణుడిని అడగండి."],
      leaf_issue: ["ప్రభావిత ఆకుల స్పష్టమైన ఫోటో తీయండి.", "ప్రభావిత మొక్కలను తాకిన తర్వాత ఆరోగ్యమైన మొక్కలను తాకవద్దు.", "రసాయన మందు వాడే ముందు స్థానిక వ్యవసాయ నిపుణుడిని అడగండి."],
      monitor: ["ప్రతి ఉదయం పైభాగంలో కొత్త ఆకులు ఆరోగ్యంగా, పచ్చగా ఉన్నాయో చూడండి.", "మంచి వెలుతురులో ఆకుల కిందివైపు పురుగులు ఉన్నాయో చూడండి."]
    },
    cautions: {
      wet_soil: "మట్టి ఇప్పటికే చాలా తడిగా ఉంటే మళ్లీ మళ్లీ నీరు పెట్టవద్దు.",
      sample_weather: "నమూనా వాతావరణాన్ని నిజమైన సూచనగా భావించవద్దు. నీరు పెట్టే ముందు స్థానిక వాతావరణాన్ని చూడండి.",
      fertilizer: "మట్టిని పరీక్షించకుండా లేదా నిపుణుడిని అడగకుండా ఎరువు వేయవద్దు.",
      spray: "సమస్యకు కారణం తెలియకముందు రసాయన మందు పిచికారీ చేయవద్దు."
    },
    watch: {
      wet_soil: ["మట్టి ఎండుతున్నప్పుడు ఆకులు మెరుగవుతున్నాయో చూడండి.", "ఆకులు పసుపు రంగులోకి మారుతున్నాయా లేదా మొక్కల దగ్గర దుర్వాసన వస్తుందా గమనించండి."],
      rain: ["మీ ప్రాంతంలో నిజంగా వర్షం పడుతుందో చూడండి.", "వర్షం పడకపోతే నీరు పెట్టే ముందు మట్టిని మళ్లీ చూడండి."],
      watering: ["నీరు పెట్టిన తర్వాత ఆకులు మెరుగవుతున్నాయో చూడండి.", "ఆకులు ముడుచుకునే ఉంటే స్పష్టమైన ఫోటో తీసి పురుగులు లేదా మచ్చలు ఉన్నాయో చూడండి."],
      general: ["పైభాగంలో కొత్త ఆకులు ఆరోగ్యంగా, పచ్చగా ఉన్నాయో చూడండి.", "మంచి వెలుతురులో ఆకుల కిందివైపు చిన్న పురుగుల కోసం చూడండి."]
    },
    why: ["మీరు తెలిపిన {crop} సమస్యను, మీరు ఎంచుకున్న మట్టి స్థితిని మేము పరిగణించాము.", "పంట, నీరు, వాతావరణం మరియు సాధ్యమైన ప్రమాదాలపై వచ్చిన సలహాలను FarmAgent పోల్చింది."],
    final: {
      stop_water: "ఇప్పుడు నీరు పెట్టవద్దు. అదనపు నీరు బయటకు వెళ్లిన తర్వాత మట్టిని మళ్లీ చూడండి.",
      wait_rain: "నీరు పెట్టే ముందు ఆగండి. మీ ప్రాంత వాతావరణం మరియు మట్టిని త్వరలో మళ్లీ చూడండి.",
      water_once: "చల్లని సమయంలో ఒకసారి నీరు పెట్టి, తర్వాత మట్టిని మళ్లీ చూడండి.",
      check_yellow: "ఎరువు వేసే ముందు మట్టిని పరీక్షించండి లేదా స్థానిక వ్యవసాయ నిపుణుడిని అడగండి.",
      leaf_issue: "ఆకుల స్పష్టమైన ఫోటో తీసి, మందు పిచికారీ చేయడానికి ముందు స్థానిక వ్యవసాయ నిపుణుడిని అడగండి.",
      monitor: "మొక్కను గమనిస్తూ ఉండండి. నీరు పెట్టే విధానాన్ని మార్చే ముందు మట్టిని చూడండి."
    },
    agents: { water: "నీటి సలహాదారు", weather: "వాతావరణ సలహాదారు", crop: "పంట సలహాదారు", risk: "ప్రమాదాల సలహాదారు" },
    debate: {
      water: {
        rain: "ఇప్పుడే నీరు పెట్టకుండా ఉండండి. ముందు మీ ప్రాంత వాతావరణాన్ని చూడండి.",
        dry: "మట్టి ఎండిపోతోంది. పంటకు త్వరలో నీరు అవసరం కావచ్చు.",
        light: "కొద్దిగా నీరు పెట్టండి; మట్టిని పూర్తిగా తడపవద్దు.",
        check: "నీరు పెట్టే ముందు మట్టి తేమను చూడండి."
      },
      weather: {
        rain: "నమూనా వాతావరణంలో వర్షం సూచిస్తోంది. నీరు పెట్టే ముందు మీ ప్రాంత వాతావరణాన్ని చూడండి.",
        hot: "నమూనా వాతావరణం వేడిగా ఉంది. చర్య తీసుకునే ముందు మీ ప్రాంత పరిస్థితులను చూడండి.",
        stable: "నమూనా వాతావరణం పెద్ద మార్పుల్లేకుండా ఉంది. స్థానిక పరిస్థితులను కూడా చూడండి."
      },
      crop: {
        wet: "మట్టి చాలా తడిగా ఉండటం వల్ల వేర్లకు ఇబ్బంది కావచ్చు; మొక్కకు నీరే కావాలని అనుకోవద్దు.",
        leaves: "ఆకుల మచ్చలకు వేర్వేరు కారణాలు ఉండవచ్చు. స్పష్టమైన ఫోటో లేదా స్థానిక నిపుణుడు సహాయపడతారు.",
        yellow: "ఆకులు పసుపు కావడానికి చాలా కారణాలు ఉండవచ్చు. ఎరువు వేసే ముందు మట్టిని చూడండి.",
        stress: "మొక్క ఒత్తిడిలో ఉన్నట్లు ఉంది. సాయంత్రం చల్లబడిన తర్వాత మార్పు ఉందో చూడండి."
      },
      risk: {
        wet: "జాగ్రత్త: మట్టి ఇప్పటికే చాలా తడిగా ఉంటే మరింత నీరు వేర్లకు హాని చేయవచ్చు.",
        rain: "నీరు పెట్టే ముందు స్థానిక వాతావరణాన్ని చూడండి. భారీ వర్షం వస్తే అదనపు నీరు సమస్య కావచ్చు.",
        fertilizer: "సమస్య తెలియకముందు ఎరువు లేదా రసాయన మందు వాడవద్దు.",
        safe: "ఈ సలహా మొక్కలకు హాని చేయదని నేను పరిశీలిస్తున్నాను."
      }
    }
  }
};

let cachedScenarios = [];
let activeLanguage = "en";
let locationCoordinates = null;

function cleanText(value) {
  return String(value ?? "").replace(/[\p{Extended_Pictographic}\uFE0F\u200D]/gu, "").replace(/\s{2,}/g, " ").trim();
}

document.addEventListener("DOMContentLoaded", () => {
  initLanguage();
  initOptionIcons();
  initVoiceInput();
  initChoiceGroup("#crop-choices", ".crop-choice", false);
  initChoiceGroup("#problem-choices", ".problem-choice", true);
  initChoiceGroup("#soil-choices", ".soil-choice", false);
  initChoiceGroup("#rain-choices", ".rain-choice", false);
  initChoiceGroup("#watered-choices", ".watered-choice", false);
  document.getElementById("farm-form").addEventListener("submit", (event) => {
    event.preventDefault();
    submitFarmAnalysis();
  });
  document.getElementById("scenario-buttons-container").addEventListener("click", (event) => {
    const button = event.target.closest("[data-scenario]");
    if (button) runDemo(Number(button.dataset.scenario));
  });
  document.getElementById("use-location").addEventListener("click", useDeviceLocation);
  document.getElementById("plant-photo").addEventListener("change", showPhotoName);
  document.getElementById("plant-photo-upload").addEventListener("change", showPhotoName);
  document.getElementById("language-select").addEventListener("change", (event) => setLanguage(event.target.value));
  fetchScenarios();
  checkEngineStatus();
});

function initVoiceInput() {
  const button = document.getElementById("voice-button");
  const title = document.getElementById("voice-title");
  const status = document.getElementById("voice-status");
  const textarea = document.getElementById("own-words");
  const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!Recognition) {
    button.disabled = true;
    button.setAttribute("aria-label", "Voice input is not supported in this browser");
    title.textContent = "Voice input unavailable";
    status.textContent = "Try a browser that supports speech recognition";
    return;
  }

  button.addEventListener("click", () => {
    if (button.classList.contains("listening")) {
      button._recognition?.stop();
      return;
    }
    const recognition = new Recognition();
    button._recognition = recognition;
    recognition.lang = ({ en: "en-IN", hi: "hi-IN", te: "te-IN", ta: "ta-IN", ml: "ml-IN", kn: "kn-IN", mr: "mr-IN" })[activeLanguage] || "en-IN";
    recognition.interimResults = true;
    recognition.continuous = false;
    recognition.onstart = () => {
      button.classList.add("listening");
      button.setAttribute("aria-pressed", "true");
      button.setAttribute("aria-label", "Stop voice input");
      title.textContent = "Listening…";
      status.textContent = "Speak clearly, then pause to finish";
    };
    recognition.onresult = (event) => {
      let transcript = "";
      for (let i = event.resultIndex; i < event.results.length; i += 1) {
        if (event.results[i].isFinal) transcript += event.results[i][0].transcript;
      }
      if (transcript.trim()) {
        const existing = textarea.value.trim();
        textarea.value = existing ? `${existing} ${transcript.trim()}` : transcript.trim();
        textarea.dispatchEvent(new Event("input", { bubbles: true }));
        status.textContent = "Voice added. Review or edit the text.";
      }
    };
    recognition.onerror = (event) => {
      const messages = {
        "not-allowed": "Microphone access was blocked. Allow it in your browser settings.",
        "service-not-allowed": "Speech recognition is unavailable for this page.",
        "no-speech": "No speech detected. Tap to try again.",
        "audio-capture": "No microphone was found on this device."
      };
      status.textContent = messages[event.error] || "Voice input stopped. Tap to try again.";
      if (event.error === "not-allowed" || event.error === "service-not-allowed") title.textContent = "Microphone unavailable";
    };
    recognition.onend = () => {
      button.classList.remove("listening");
      button.setAttribute("aria-pressed", "false");
      button.setAttribute("aria-label", "Start voice input");
      if (title.textContent === "Listening…") title.textContent = "Voice assistant";
      if (status.textContent === "Tap to describe the problem") status.textContent = "Tap to speak";
    };
    try {
      recognition.start();
    } catch (_error) {
      status.textContent = "Could not start voice input. Please try again.";
    }
  });
}

function initOptionIcons() {
  const icons = {
    leaf: '<path d="M20 4C11 4 5 7.8 5 14a6 6 0 0 0 6 6c6.2 0 9-7 9-16Z"/><path d="M4 21c3-5 7-8 12-11"/>',
    drop: '<path d="M12 3s-6 7-6 11a6 6 0 0 0 12 0c0-4-6-11-6-11Z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
    bug: '<path d="M12 8a4 4 0 0 0-4 4v5a4 4 0 0 0 8 0v-5a4 4 0 0 0-4-4Z"/><path d="M9 8 7 5m8 3 2-3M8 12H5m11 0h3M8 16H5m11 0h3M12 8V5"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/>',
    cloud: '<path d="M7 18h10a4 4 0 0 0 .4-8A6 6 0 0 0 6 9a4.5 4.5 0 0 0 1 9Z"/><path d="m9 20-1 2m6-2-1 2m6-2-1 2"/>',
    search: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4 4m-9.5-12v5m-2.5-2.5h5"/>',
    calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18m-13 4h2m4 0h2m-8 4h2"/>',
    sprout: '<path d="M12 21v-9m0 2c-5 0-8-3-8-8 5 0 8 3 8 8Zm0-3c0-5 3-8 8-8 0 5-3 8-8 8Z"/>',
    fruit: '<circle cx="12" cy="13" r="7"/><path d="M12 6c0-2 1-3 3-4M10 7 8 5m4 2c2-2 4-2 6-1"/>'
  };
  document.querySelectorAll(".choice-card, .demo-chip").forEach((button) => {
    button.querySelectorAll(":scope > span").forEach((span) => {
      if (!span.classList.contains("scenario-number") && !span.classList.contains("scenario-copy") && !span.hasAttribute("data-i18n") && !span.classList.contains("option-icon")) {
        if (!cleanText(span.textContent)) span.remove();
      }
    });
    if (button.querySelector(":scope > .option-icon")) return;
    const value = button.dataset.value || "";
    let icon = "leaf";
    if (button.classList.contains("demo-chip")) icon = ["drop", "cloud", "leaf", "bug", "drop"][Number(button.dataset.scenario)] || "leaf";
    else if (button.classList.contains("crop-choice")) icon = value === "tomato" ? "fruit" : "leaf";
    else if (value.includes("thirst") || value.includes("water") || value.includes("wet") || value === "yes") icon = value.includes("water") || value.includes("wet") || value === "yes" ? "drop" : "drop";
    else if (value.includes("heat")) icon = "sun";
    else if (value.includes("insect") || value.includes("disease")) icon = "bug";
    else if (value.includes("unknown")) icon = "search";
    else if (button.classList.contains("watered-choice")) icon = "calendar";
    else if (value.includes("growth") || value.includes("curl") || value.includes("yellow")) icon = "leaf";
    const node = document.createElement("span");
    node.className = "option-icon";
    node.setAttribute("aria-hidden", "true");
    node.innerHTML = `<svg viewBox="0 0 24 24">${icons[icon]}</svg>`;
    button.prepend(node);
  });
}

function initLanguage() {
  const stored = localStorage.getItem("farmagent-language");
  setLanguage(translations[stored] ? stored : "en");
}

function setLanguage(code) {
  activeLanguage = translations[code] ? code : "en";
  localStorage.setItem("farmagent-language", activeLanguage);
  document.documentElement.lang = activeLanguage;
  document.getElementById("language-select").value = activeLanguage;
  const words = translations[activeLanguage];
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const translated = words[element.dataset.i18n];
    if (translated && element.matches("button") && element.querySelector(":scope > .option-icon")) {
      let label = element.querySelector(":scope > .choice-label");
      if (!label) {
        label = document.createElement("span");
        label.className = "choice-label";
        element.appendChild(label);
      }
      label.textContent = cleanText(translated);
    } else if (translated) element.innerHTML = cleanText(translated);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
    const translated = words[element.dataset.i18nPlaceholder];
    if (translated) element.placeholder = cleanText(translated);
  });
  if (document.getElementById("results-container").hidden === false && window.lastFarmerView) {
    renderFarmerView(window.lastFarmerView, window.lastReport);
  }
}

function initChoiceGroup(containerSelector, buttonSelector, multiple) {
  const container = document.querySelector(containerSelector);
  container.addEventListener("click", (event) => {
    const button = event.target.closest(buttonSelector);
    if (!button) return;
    if (!multiple) {
      container.querySelectorAll(buttonSelector).forEach((choice) => {
        choice.classList.remove("selected");
        choice.setAttribute("aria-pressed", "false");
      });
    }
    const selected = !button.classList.contains("selected");
    button.classList.toggle("selected", selected);
    button.setAttribute("aria-pressed", String(selected));
    if (button.matches(".crop-choice")) {
      const isOther = button.dataset.value === "other";
      document.getElementById("custom-crop-wrap").hidden = !isOther;
      if (!isOther) document.getElementById("custom-crop").value = "";
    }
  });
}

async function fetchScenarios() {
  try {
    const response = await fetch("/api/scenarios");
    if (!response.ok) throw new Error(`Scenario request failed (${response.status})`);
    const data = await response.json();
    cachedScenarios = data.status === "success" ? data.scenarios || [] : [];
  } catch (error) {
    console.warn("Demo scenarios are unavailable:", error);
  }
}

function runDemo(index) {
  const scenario = cachedScenarios[index];
  if (!scenario) {
    showError(translations[activeLanguage].missingAdvice);
    return;
  }
  const input = scenario.input;
  resetChoices();
  setSelected(".crop-choice", input.crop.toLowerCase() === "corn" ? "maize" : input.crop.toLowerCase());
  document.getElementById("own-words").value = input.symptoms || "";
  document.getElementById("input-location").value = input.location || "";
  document.getElementById("input-growth-stage").value = input.growth_stage || "";
  document.getElementById("input-soil-type").value = input.soil_type || "";
  document.getElementById("input-soil-moisture").value = input.soil_moisture ?? "";
  document.getElementById("input-recent-rainfall").value = input.recent_rainfall ?? "";
  document.getElementById("input-weather-preset").value = input.weather_preset || "default";
  document.getElementById("input-additional-info").value = input.additional_info || "";
  document.querySelector(".advanced-details").open = true;
  document.querySelectorAll(".demo-chip").forEach((chip) => chip.classList.toggle("selected", Number(chip.dataset.scenario) === index));
  submitFarmAnalysis(input);
}

function setSelected(selector, value) {
  const button = [...document.querySelectorAll(selector)].find((choice) => choice.dataset.value === value);
  if (button) {
    button.classList.add("selected");
    button.setAttribute("aria-pressed", "true");
  }
}

function resetChoices() {
  document.querySelectorAll(".choice-card, .demo-chip").forEach((button) => {
    button.classList.remove("selected");
    button.setAttribute("aria-pressed", "false");
  });
}

function getChoice(selector) {
  return document.querySelector(`${selector}.selected`)?.dataset.value || "";
}

function getSelectedProblems() {
  return [...document.querySelectorAll(".problem-choice.selected")].map((button) => button.dataset.value);
}

function showPhotoName(event) {
  const file = event.target.files[0];
  document.getElementById("photo-name").textContent = file ? cleanText(`${file.name} — ${translations[activeLanguage].photoNotAnalyzed}`) : "";
}

function useDeviceLocation() {
  const status = document.getElementById("location-status");
  if (!navigator.geolocation) {
    status.textContent = cleanText(translations[activeLanguage].locationFailed);
    return;
  }
  status.textContent = cleanText(translations[activeLanguage].locationGetting);
  navigator.geolocation.getCurrentPosition(
    (position) => {
      locationCoordinates = { latitude: position.coords.latitude, longitude: position.coords.longitude };
      document.getElementById("input-location").value = `${position.coords.latitude.toFixed(5)}, ${position.coords.longitude.toFixed(5)}`;
      status.textContent = cleanText(translations[activeLanguage].locationSet);
    },
    () => {
      status.textContent = cleanText(translations[activeLanguage].locationFailed);
    },
    { enableHighAccuracy: false, timeout: 10000, maximumAge: 300000 }
  );
}

function numberOrEmpty(id) {
  const value = document.getElementById(id).value;
  return value === "" ? "" : Number(value);
}

function collectPayload() {
  const cropChoice = getChoice(".crop-choice");
  const data = {
    crop_choice: cropChoice,
    custom_crop: cropChoice === "other" ? document.getElementById("custom-crop").value.trim() : "",
    crop: cropChoice && cropChoice !== "other" ? cropChoice : "Other",
    problem_tags: getSelectedProblems(),
    own_words: document.getElementById("own-words").value.trim(),
    soil_feel: getChoice(".soil-choice") || "unknown",
    rained_recently: getChoice(".rain-choice") || "unknown",
    last_watered: getChoice(".watered-choice") || "",
    location: document.getElementById("input-location").value.trim(),
    growth_stage: document.getElementById("input-growth-stage").value.trim(),
    soil_type: document.getElementById("input-soil-type").value,
    soil_moisture: numberOrEmpty("input-soil-moisture"),
    recent_rainfall: numberOrEmpty("input-recent-rainfall"),
    temperature: numberOrEmpty("input-temperature"),
    weather_preset: document.getElementById("input-weather-preset").value,
    additional_info: document.getElementById("input-additional-info").value.trim()
  };
  if (locationCoordinates) Object.assign(data, locationCoordinates);
  return data;
}

async function submitFarmAnalysis(demoInput = null) {
  const payload = demoInput || collectPayload();
  if (!payload.crop && !payload.custom_crop && !payload.crop_choice) {
    showError(translations[activeLanguage].missingAdvice);
    return;
  }
  document.getElementById("error-message").hidden = true;
  document.getElementById("results-container").hidden = true;
  document.getElementById("loading-panel").hidden = false;
  document.getElementById("btn-analyze").disabled = true;
  const steps = [...document.querySelectorAll(".progress-list li")];
  let activeStep = 0;
  steps.forEach((step, index) => step.classList.toggle("progress-active", index === 0));
  const progressTimer = window.setInterval(() => {
    activeStep = Math.min(activeStep + 1, steps.length - 1);
    steps.forEach((step, index) => step.classList.toggle("progress-active", index === activeStep));
  }, 1000);

  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok || result.status !== "success" || !result.report) {
      throw new Error(result.message || `Analysis failed (${response.status})`);
    }
    window.lastCropName = (payload.custom_crop || payload.crop || "crop").trim();
    window.lastReport = result.report;
    window.lastFarmerView = result.farmer_view || {};
    renderFarmerView(window.lastFarmerView, result.report);
    document.getElementById("results-container").hidden = false;
    document.getElementById("demo-data-note").hidden = !isDemoWeather(result.report);
    document.getElementById("results-container").scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (error) {
    showError(error.message || "FarmAgent could not complete the analysis. Please try again.");
  } finally {
    window.clearInterval(progressTimer);
    document.getElementById("loading-panel").hidden = true;
    document.getElementById("btn-analyze").disabled = false;
  }
}

function isDemoWeather(report) {
  const findings = report.agent_opinions?.["Weather Agent"]?.key_findings || [];
  return findings.some((line) => /mock|demo/i.test(line));
}

function setText(id, value, fallback = "") {
  document.getElementById(id).textContent = cleanText(value || fallback);
}

function appendList(id, items, fallback = "") {
  const list = document.getElementById(id);
  list.replaceChildren();
  (items && items.length ? items : fallback ? [fallback] : []).forEach((item) => {
    const li = document.createElement("li");
    li.textContent = cleanText(item);
    list.appendChild(li);
  });
}

function renderFarmerView(view, report) {
  const words = translations[activeLanguage];
  const resultWords = farmerResultTranslations[activeLanguage];
  if (resultWords) {
    const crop = resultWords.crops[window.lastCropName.toLowerCase()] || window.lastCropName || "పంట";
    const fillCrop = (text) => text.replaceAll("{crop}", crop);
    setText("what-we-found", fillCrop(resultWords.findings[view.finding_key] || words.missingAdvice));
    appendList("what-to-do", resultWords.actions[view.action_key]);
    appendList("be-careful", [resultWords.cautions[view.careful_key]]);
    appendList("watch-for", resultWords.watch[view.watch_key]);
    appendList("why-list", resultWords.why.map(fillCrop));
    setText("final-choice", resultWords.final[view.final_decision_key]);
  } else {
    setText("what-we-found", view.what_we_found, words.missingAdvice);
    appendList("what-to-do", view.what_to_do);
    appendList("be-careful", view.be_careful);
    appendList("watch-for", view.watch_for);
    appendList("why-list", view.why_farmagent_thinks_this);
    setText("final-choice", view.final_decision_simple);
  }

  const confidence = String(view.confidence_level || report.confidence || "medium").toLowerCase();
  const confidenceKey = confidence === "high" ? "confidenceHigh" : confidence === "low" ? "confidenceLow" : "confidenceMedium";
  setText("confidence-text", words[confidenceKey]);
  document.querySelector(".confidence-icon").textContent = "";

  const debate = document.getElementById("debate-dialogue");
  debate.replaceChildren();
  (view.simplified_debate || []).forEach((entry) => {
    const line = document.createElement("article");
    line.className = "debate-line";
    const icon = document.createElement("span");
    icon.className = "debate-agent-icon";
    icon.textContent = ({ crop: "C", water: "W", weather: "M", soil: "S", risk: "R" })[entry.domain] || "A";
    const text = document.createElement("p");
    const name = document.createElement("strong");
    name.textContent = cleanText(resultWords ? resultWords.agents[entry.domain] : entry.agent || "FarmAgent");
    const quote = document.createElement("span");
    quote.textContent = cleanText(resultWords ? translateDebate(entry.domain, entry.dialogue, resultWords) : entry.dialogue || "");
    text.append(name, quote);
    line.append(icon, text);
    debate.appendChild(line);
  });
  document.getElementById("demo-data-note").textContent = cleanText(words.weatherDemoNotice);
}

function translateDebate(domain, dialogue, words) {
  const text = (dialogue || "").toLowerCase();
  if (domain === "water") {
    if (text.includes("hold the water")) return words.debate.water.rain;
    if (text.includes("soil is running dry")) return words.debate.water.dry;
    if (text.includes("light watering")) return words.debate.water.light;
    return words.debate.water.check;
  }
  if (domain === "weather") {
    if (text.includes("rain")) return words.debate.weather.rain;
    if (text.includes("hot") || text.includes("scorching")) return words.debate.weather.hot;
    return words.debate.weather.stable;
  }
  if (domain === "crop") {
    if (text.includes("waterlogging") || text.includes("root trouble")) return words.debate.crop.wet;
    if (text.includes("leaf marks") || text.includes("description alone")) return words.debate.crop.leaves;
    if (text.includes("yellowing")) return words.debate.crop.yellow;
    return words.debate.crop.stress;
  }
  if (domain === "risk") {
    if (text.includes("waterlogged") || text.includes("very wet")) return words.debate.risk.wet;
    if (text.includes("downpour") || text.includes("heavy rain")) return words.debate.risk.rain;
    if (text.includes("fertilizer") || text.includes("chemical spray")) return words.debate.risk.fertilizer;
    return words.debate.risk.safe;
  }
  return dialogue || "";
}

function showError(message) {
  const error = document.getElementById("error-message");
  error.textContent = cleanText(message);
  error.hidden = false;
  document.getElementById("loading-panel").hidden = true;
}

async function checkEngineStatus() {
  try {
    const response = await fetch("/api/status");
    const result = await response.json();
    if (result.status === "success") {
      document.getElementById("engine-status-text").textContent = result.groq_enabled ? "AI analysis ready" : "Offline analysis ready";
    }
  } catch (error) {
    document.getElementById("engine-status-text").textContent = "FarmAgent ready";
  }
}
