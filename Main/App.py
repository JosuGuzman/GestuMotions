import cv2
from deepface import DeepFace
from MultiEmotions import (
    traducir_emocion, color_emocion, emoji_emocion
)

def iniciar_gestumotions(idioma="Español"):
    print(f"Iniciando en idioma: {idioma}")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error con la cámara.")
            break

        try:
            results = DeepFace.analyze(
                frame,
                actions=['emotion'],  # Solo emoción
                detector_backend='mtcnn',
                enforce_detection=False,
                silent=True
            )

            # Siempre lista
            if not isinstance(results, list):
                results = [results]

            # Tomar primer rostro
            face = results[0]

            # Validar región
            if isinstance(face.get('region', {}), dict) and all(k in face['region'] for k in ('x', 'y', 'w', 'h')):
                x = face['region']['x']
                y = face['region']['y']
                w = face['region']['w']
                h = face['region']['h']

                emocion_orig = face['dominant_emotion']

                emocion_es = traducir_emocion(emocion_orig, idioma)
                color = color_emocion(emocion_orig)
                emoji = emoji_emocion(emocion_orig)

                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                texto = f"{emoji} {emocion_es}"

                cv2.putText(frame, texto, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        except Exception as e:
            print(f"Error: {e}")

        cv2.imshow("GestuMotions", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
