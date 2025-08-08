import tkinter as tk
from tkinter import ttk
from App import iniciar_gestumotions

def seleccionar_idioma(idioma):
    idioma_seleccionado.set(idioma)

def comenzar_app():
    ventana.destroy()
    iniciar_gestumotions(idioma_seleccionado.get())

# Primero creamos la ventana principal
ventana = tk.Tk()
ventana.title("GestuMotions - Inicio")
ventana.geometry("400x200")
ventana.resizable(False, False)

# Ahora sí podemos crear variables de Tkinter
idioma_seleccionado = tk.StringVar(value="Español")  # Valor por defecto

# Estilo
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)

# Título
tk.Label(ventana, text="Bienvenido a GestuMotions", font=("Helvetica", 16)).pack(pady=10)

# Botón de idioma
def mostrar_idiomas():
    menu_idiomas = tk.Toplevel(ventana)
    menu_idiomas.title("Elegí un idioma")
    idiomas = ["Español", "Inglés", "Euskera", "Chino", "Francés"]
    for idioma in idiomas:
        ttk.Button(menu_idiomas, text=idioma, command=lambda i=idioma: [seleccionar_idioma(i), menu_idiomas.destroy()]).pack(pady=3)

ttk.Button(ventana, text="🌐 Language", command=mostrar_idiomas).pack(pady=5)

# Botón de iniciar
ttk.Button(ventana, text="▶ Start", command=comenzar_app).pack(pady=5)

# Mostrar idioma seleccionado
tk.Label(ventana, textvariable=idioma_seleccionado, font=("Helvetica", 10, "italic")).pack(pady=10)

ventana.mainloop()