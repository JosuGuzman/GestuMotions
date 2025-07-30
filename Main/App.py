import cv2
from deepface import DeepFace
from MultiEmotions import (
    traducir_emocion, color_emocion, emoji_emocion,
    traducir_genero, etiqueta_genero, etiqueta_edad, etiqueta_anios
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
                actions=['emotion', 'age', 'gender'],
                detector_backend='mtcnn',
                enforce_detection=False,
                silent=True
            )

            if not isinstance(results, list):
                results = [results]

            def rostro_mas_grande(x):
                x1, y1, w, h = x['region'].values()
                return w * h

            results = sorted(results, key=rostro_mas_grande, reverse=True)[:3]

            for face in results:
                x, y, w, h = face['region'].values()
                emocion_orig = face['dominant_emotion']
                genero = face['gender']
                edad = int(face['age'])

                emocion_es = traducir_emocion(emocion_orig, idioma)
                color = color_emocion(emocion_orig)
                emoji = emoji_emocion(emocion_orig)

                genero_traducido = traducir_genero(genero, idioma)
                etq_gen = etiqueta_genero(idioma)
                etq_age = etiqueta_edad(idioma)
                sufijo_anios = etiqueta_anios(idioma)

                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

                texto = f"{emoji} {emocion_es} | {etq_gen}: {genero_traducido} | {etq_age}: {edad} {sufijo_anios}"

                cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        except Exception as e:
            print(f"Error: {e}")

        cv2.imshow("GestuMotions", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()