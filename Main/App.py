import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from fer import FER
from MultiEmotions import traducciones, emojis

class DetectorEmocionesApp:
    def __init__(self):
        self.idioma_seleccionado = "es"
        self.cam = None
        self.detector = FER(mtcnn=True)

        self.menu_idioma()

    def menu_idioma(self):
        self.root = tk.Tk()
        self.root.title("Selecciona un idioma")
        self.root.configure(bg="#cce7ff")

        tk.Label(self.root, text="Elige el idioma de las emociones:", font=("Arial", 16), bg="#cce7ff").pack(pady=10)

        # Mostrar nombres completos de idiomas para que sea amigable para los niños
        idiomas_completos = {
            "es": "Español",
            "en": "Inglés",
            "fr": "Francés",
            "eu": "Euskera",
            "zh": "Chino"
        }
        self.combo_idioma = ttk.Combobox(self.root, values=list(idiomas_completos.values()), state="readonly", font=("Arial", 14))
        self.combo_idioma.set(idiomas_completos[self.idioma_seleccionado])
        self.combo_idioma.pack(pady=10)

        btn_iniciar = tk.Button(self.root, text="Iniciar Detector", command=self.seleccionar_idioma, font=("Arial", 14), bg="#66cc66")
        btn_iniciar.pack(pady=20)

        # Mapeo inverso para traducción al código idioma
        self.idiomas_completos = idiomas_completos

        self.root.mainloop()

    def seleccionar_idioma(self):
        valor = self.combo_idioma.get()
        # Buscar clave según valor
        for k, v in self.idiomas_completos.items():
            if v == valor:
                self.idioma_seleccionado = k
                break
        self.root.destroy()
        self.iniciar_detector()

    def iniciar_detector(self):
        self.ventana_detector = tk.Tk()
        self.ventana_detector.title("Detector de Emociones")
        self.ventana_detector.configure(bg="#ffeb99")

        self.cam = cv2.VideoCapture(0)

        self.lbl_video = tk.Label(self.ventana_detector)
        self.lbl_video.pack()

        self.lbl_emocion = tk.Label(self.ventana_detector, text="Esperando...", font=("Arial", 28, "bold"), bg="#ffeb99", fg="#333")
        self.lbl_emocion.pack()

        self.lbl_emoji = tk.Label(self.ventana_detector, text="", font=("Arial", 100))
        self.lbl_emoji.pack()

        self.actualizar_video()

        self.ventana_detector.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.ventana_detector.mainloop()

    def actualizar_video(self):
        ret, frame = self.cam.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resultado = self.detector.detect_emotions(rgb)

            if resultado:
                emocion = max(resultado[0]['emotions'], key=resultado[0]['emotions'].get)
                traduccion = traducciones[self.idioma_seleccionado][emocion]
                self.lbl_emocion.config(text=traduccion, fg="green")
                self.lbl_emoji.config(text=emojis.get(emocion, ""))
            else:
                self.lbl_emocion.config(text=traducciones[self.idioma_seleccionado]["no_face"], fg="red")
                self.lbl_emoji.config(text="")

            img = Image.fromarray(rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lbl_video.imgtk = imgtk
            self.lbl_video.configure(image=imgtk)

        self.lbl_video.after(20, self.actualizar_video)

    def cerrar(self):
        self.cam.release()
        self.ventana_detector.destroy()
