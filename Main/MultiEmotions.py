import emoji

# Diccionario de traducciones
traducciones = {
    "es": {
        "happy": "Feliz",
        "sad": "Triste",
        "angry": "Enojado",
        "surprise": "Sorprendido",
        "fear": "Miedo",
        "disgust": "Asco",
        "neutral": "Neutral",
        "no_face": "¿Dónde estás? 🙈"
    },
    "en": {
        "happy": "Happy",
        "sad": "Sad",
        "angry": "Angry",
        "surprise": "Surprised",
        "fear": "Fear",
        "disgust": "Disgusted",
        "neutral": "Neutral",
        "no_face": "Where are you? 🙈"
    },
    "fr": {
        "happy": "Heureux",
        "sad": "Triste",
        "angry": "En colère",
        "surprise": "Surpris",
        "fear": "Peur",
        "disgust": "Dégoût",
        "neutral": "Neutre",
        "no_face": "Où es-tu ? 🙈"
    },
    "eu": {
        "happy": "Pozik",
        "sad": "Triste",
        "angry": "Haserre",
        "surprise": "Harridura",
        "fear": "Beldurra",
        "disgust": "Nazka",
        "neutral": "Neutral",
        "no_face": "Non zaude? 🙈"
    },
    "zh": {
        "happy": "开心",
        "sad": "伤心",
        "angry": "生气",
        "surprise": "惊讶",
        "fear": "害怕",
        "disgust": "厌恶",
        "neutral": "中性",
        "no_face": "你在哪？🙈"
    }
}

# Emojis para cada emoción
emojis = {
    'happy': emoji.emojize(":smiley:"), #
    'sad': emoji.emojize(":cry:"), #
    'angry': emoji.emojize(":angry_face:"), #😠
    'surprise': emoji.emojize(":astonished_face:"), #😲
    'fear': emoji.emojize(":fearful_face:"), #😱
    'disgust': emoji.emojize(":nauseated_face:"), #🤢
    'neutral': emoji.emojize(":neutral_face:") #😐
}
