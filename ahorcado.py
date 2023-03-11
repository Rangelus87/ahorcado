import tkinter as tk
from tkinter import ttk as tt
from funciones import select_pais
from funciones import recupero_datos
from funciones import comprobar_letras
from funciones import final


# from tkinter import messagebox as ms


class Ahorcado(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("bienvenid@")
        self.geometry("375x130")

        # Ventana de bienvenida
        self.inicio_frame = tt.Frame(self)
        self.inicio_frame.grid(column=0, row=0, padx=10, pady=15)
        self.nombre_label = tt.Label(self.inicio_frame, text="¿Cual es tu nombre?: ")
        self.nombre_label.grid(column=0, row=0, padx=10, pady=10)
        self.nombre_var = tk.StringVar()
        self.nombre_entry = tt.Entry(self.inicio_frame, width=20, textvariable=self.nombre_var)
        self.nombre_entry.grid(column=1, row=0, padx=10, pady=10)
        self.nombre_btn = tt.Button(self.inicio_frame, text="Entrar", command=self.cambio_ventana)
        self.nombre_btn.bind_all("<Return>", self.cambio_ventana)
        self.nombre_btn.grid(column=1, row=1, padx=10, pady=5)

    def cambio_ventana(self, *event):
        self.guiones = select_pais()
        self.ventana_juego()
        self.withdraw()
        self.win_toplevel.protocol("WM_DELETE_WINDOW",
                                   lambda: (self.win_toplevel.destroy(), self.destroy(), final()))

    # Ventana de juego
    def ventana_juego(self):
        self.win_toplevel = tk.Toplevel(self)

        self.juego_frame = tt.Frame(self.win_toplevel)
        self.juego_frame.grid(column=0, row=0, padx=10, pady=10)

        self.bienvenida_label = tt.Label(self.juego_frame, text=f"¡Bienvenido {self.nombre_var.get()}!")
        self.bienvenida_label.grid(column=0, row=0, padx=20, pady=5, columnspan=3)

        self.jugamos_label = tt.Label(self.juego_frame, text="juguemos al ahorcado")
        self.jugamos_label.grid(column=0, row=1, padx=10, columnspan=3)
        self.jugamos_label1 = tt.Label(self.juego_frame, text="Adivina la palabra antes que el contador llegue a 0")
        self.jugamos_label1.grid(column=0, row=2, padx=10, pady=5, columnspan=3)

        self.letras_label = tt.Label(self.juego_frame, text=self.guiones)
        self.letras_label.grid(column=0, row=3, padx=10, pady=10, columnspan=3)

        self.enunciado_lebel = tt.Label(self.juego_frame, text="Igresa una letra")
        self.enunciado_lebel.grid(column=0, row=4, padx=5, pady=5)
        self.contador_label = tt.Label(self.juego_frame, text="Contador = 10")
        self.contador_label.grid(column=0, row=5)
        self.letra_var = tk.StringVar()
        self.letra_entry = tt.Entry(self.juego_frame, width=5, textvariable=self.letra_var)
        self.letra_entry.grid(column=1, row=4, padx=5, pady=5)
        self.letra_entry.bind_all('<Return>', self.llamadas)

        self.letra_btn = tt.Button(self.juego_frame, text="Comprobar", command=self.llamadas)
        self.letra_btn.grid(column=1, row=5, padx=5)

    def llamadas(self, *event):
        char = self.letra_var.get()
        self.letra_entry.delete("0", "end")
        comprobar_letras(char)
        contador, cambio = recupero_datos()
        self.letras_label.configure(text=cambio)
        self.contador_label.configure(text=f"Contador = {contador}")


app = Ahorcado()
app.mainloop()
