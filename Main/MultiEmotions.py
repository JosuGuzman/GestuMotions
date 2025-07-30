def traducir_genero(genero, idioma):
    genero_map = {
        'Man': {
            'Español': 'Hombre', 'Inglés': 'Male', 'Euskera': 'Gizona',
            'Chino': '男性 (Nánxìng)', 'Francés': 'Homme'
        },
        'Woman': {
            'Español': 'Mujer', 'Inglés': 'Female', 'Euskera': 'Emakumea',
            'Chino': '女性 (Nǚxìng)', 'Francés': 'Femme'
        }
    }
    return genero_map.get(genero, {}).get(idioma, genero)

def etiqueta_genero(idioma):
    return {
        'Español': 'Género',
        'Inglés': 'Gender',
        'Euskera': 'Generoa',
        'Chino': '性别',
        'Francés': 'Genre'
    }.get(idioma, 'Género')

def etiqueta_edad(idioma):
    return {
        'Español': 'Edad',
        'Inglés': 'Age',
        'Euskera': 'Adina',
        'Chino': '年龄',
        'Francés': 'Âge'
    }.get(idioma, 'Edad')

def etiqueta_anios(idioma):
    return {
        'Español': 'años',
        'Inglés': 'years old',
        'Euskera': 'urte',
        'Chino': '岁',
        'Francés': 'ans'
    }.get(idioma, 'años')

def traducir_emocion(emocion, idioma):
    traducciones = {
        "happy": {"Español": "Feliz", "Inglés": "Happy", "Euskera": "Pozik", "Chino": "高兴", "Francés": "Heureux"},
        "sad": {"Español": "Triste", "Inglés": "Sad", "Euskera": "Triste", "Chino": "伤心", "Francés": "Triste"},
        "angry": {"Español": "Enojado", "Inglés": "Angry", "Euskera": "Haserre", "Chino": "生气", "Francés": "Fâché"},
        "surprise": {"Español": "Sorprendido", "Inglés": "Surprised", "Euskera": "Harrituta", "Chino": "惊讶", "Francés": "Surpris"},
        "fear": {"Español": "Asustado", "Inglés": "Afraid", "Euskera": "Beldurtuta", "Chino": "害怕", "Francés": "Effrayé"},
        "disgust": {"Español": "Disgustado", "Inglés": "Disgusted", "Euskera": "Nazkatuta", "Chino": "恶心", "Francés": "Dégoûté"},
        "neutral": {"Español": "Neutral", "Inglés": "Neutral", "Euskera": "Neutrala", "Chino": "中性", "Francés": "Neutre"},
    }
    return traducciones.get(emocion, {}).get(idioma, emocion)

def color_emocion(emocion):
    colores = {
        'happy': (255, 255, 0),
        'sad': (92, 182, 255),
        'angry': (255, 46, 46),
        'surprise': (255, 174, 0),
        'fear': (128, 0, 128),
        'disgust': (0, 128, 0),
        'neutral': (200, 200, 200)
    }
    return colores.get(emocion, (0, 0, 0))

def emoji_emocion(emocion):
    emojis = {
        'happy': '😄',
        'sad': '😢',
        'angry': '😠',
        'surprise': '😲',
        'fear': '😱',
        'disgust': '🤢',
        'neutral': '😐'
    }
    return emojis.get(emocion, '')
