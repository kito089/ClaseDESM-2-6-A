import tkinter as tk
from tkinter import ttk

def saludar():
    resultado.config(text="Hola " + nombre.get() + "! ")

def cng_color(event):
    ventana.config(bg=col[combo.get()])

col = {
    "Rojo": "red",
    "Verde": "green",
    "Azul": "blue",
    "Amarillo": "yellow"
}

ventana = tk.Tk()
ventana.title("Interfaz grafica")
ventana.geometry("720x480")

tk.Label(ventana, text="Escribe tu nombre: ").pack()

nombre = tk.Entry(ventana)
nombre.pack()

combo = ttk.Combobox(ventana, values=list(col.keys()), state="readonly")
combo.bind("<<ComboboxSelected>>", cng_color)
combo.pack(pady=5)

resultado = tk.Label(ventana, text="")
resultado.pack()

btn_saludar = tk.Button(ventana, text="Saludar", command=saludar)
btn_saludar.pack()

ventana.mainloop()