import random
import string
import tkinter as tk

# Función para generar la contraseña
def generar_contraseña():
    try:
        longitud = int(entry.get())  # Obtiene la longitud desde el campo de entrada
        if longitud <= 0:
            resultado_label.config(text=mensaje_longitud_invalida)
            return
        if longitud > 20:  # Validación para limitar el máximo a 20
            resultado_label.config(text=mensaje_longitud_maxima)
            return
        
        # Generar caracteres según selección del usuario
        caracteres = ""
        if incluir_mayusculas.get():
            caracteres += string.ascii_uppercase
        if incluir_numeros.get():
            caracteres += string.digits
        if incluir_simbolos.get():
            caracteres += string.punctuation
        if not caracteres:  # Si no selecciona nada, incluir letras por defecto
            caracteres += string.ascii_letters

        password = "".join(random.choice(caracteres) for _ in range(longitud))
        resultado_label.config(text=f"{mensaje_contraseña}: {password}")
        copiar_contraseña(password)  # Copia la contraseña al portapapeles
    except ValueError:
        resultado_label.config(text=mensaje_solo_numeros)

# Función para copiar la contraseña al portapapeles
def copiar_contraseña(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    resultado_label.config(text=f"{mensaje_copiada}: {password}")

# Función para cambiar idioma
def cambiar_idioma(idioma):
    global mensaje_longitud_invalida, mensaje_longitud_maxima, mensaje_solo_numeros, mensaje_contraseña, mensaje_copiada
    if idioma == "Español":
        label.config(text="¿De qué longitud quieres tu contraseña?")
        label2.config(text="Recuerda colocar solo números.")
        button.config(text="Generar")
        incluir_mayusculas_checkbox.config(text="Incluir solo mayúsculas")
        incluir_numeros_checkbox.config(text="Incluir solo números")
        incluir_simbolos_checkbox.config(text="Incluir solo símbolos")
        mensaje_longitud_invalida = "Ingrese un número válido."
        mensaje_longitud_maxima = "La longitud máxima es de 20 caracteres."
        mensaje_solo_numeros = "Ingrese solo números."
        mensaje_contraseña = "Tu contraseña es"
        mensaje_copiada = "Contraseña copiada al portapapeles"
    elif idioma == "English":
        label.config(text="What length do you want your password?")
        label2.config(text="Remember to enter numbers only.")
        button.config(text="Generate")
        incluir_mayusculas_checkbox.config(text="Include only uppercase")
        incluir_numeros_checkbox.config(text="Include only numbers")
        incluir_simbolos_checkbox.config(text="Include only symbols")
        mensaje_longitud_invalida = "Enter a valid number."
        mensaje_longitud_maxima = "The maximum length is 20 characters."
        mensaje_solo_numeros = "Enter numbers only."
        mensaje_contraseña = "Your password is"
        mensaje_copiada = "Password copied to clipboard"

# Configuración de la ventana principal
root = tk.Tk()
root.title("Password Tools")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Variables iniciales para los mensajes
mensaje_longitud_invalida = "Ingrese un número válido."
mensaje_longitud_maxima = "La longitud máxima es de 20 caracteres."
mensaje_solo_numeros = "Ingrese solo números."
mensaje_contraseña = "Tu contraseña es"
mensaje_copiada = "Contraseña copiada al portapapeles"

# Etiquetas
label = tk.Label(root, text="¿De qué longitud quieres tu contraseña?", bg="#f0f0f0")
label.pack(pady=5)
label2 = tk.Label(root, text="Recuerda colocar solo números.", bg="#f0f0f0")
label2.pack(pady=5)

# Entrada de datos
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

# Checkboxes para opciones
incluir_mayusculas = tk.BooleanVar()
incluir_numeros = tk.BooleanVar()
incluir_simbolos = tk.BooleanVar()

incluir_mayusculas_checkbox = tk.Checkbutton(root, text="Incluir solo mayúsculas", variable=incluir_mayusculas, bg="#f0f0f0")
incluir_mayusculas_checkbox.pack()
incluir_numeros_checkbox = tk.Checkbutton(root, text="Incluir solo números", variable=incluir_numeros, bg="#f0f0f0")
incluir_numeros_checkbox.pack()
incluir_simbolos_checkbox = tk.Checkbutton(root, text="Incluir solo símbolos", variable=incluir_simbolos, bg="#f0f0f0")
incluir_simbolos_checkbox.pack()

# Botón para generar la contraseña
button = tk.Button(root, text="Generar", command=generar_contraseña, bg="#4caf50", fg="white")
button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="", fg="blue", bg="#f0f0f0", wraplength=350)
resultado_label.pack(pady=10)

# Menú para cambiar idioma
menu = tk.Menu(root)
idioma_menu = tk.Menu(menu, tearoff=0)
idioma_menu.add_command(label="Español", command=lambda: cambiar_idioma("Español"))
idioma_menu.add_command(label="English", command=lambda: cambiar_idioma("English"))
menu.add_cascade(label="Idioma", menu=idioma_menu)
root.config(menu=menu)

# Ejecutar la ventana
root.mainloop()


