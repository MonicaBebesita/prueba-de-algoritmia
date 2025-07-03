#Mónica A. Castellanos
import tkinter as tk
from tkinter import font, messagebox
import bisect

def encontrar_limites_para_consultas(db, consultas):
    """
    Encuentra los límites superior e inferior para una lista de consultas
    en una base de datos de números.

    Args:
        db (list): La lista de números enteros ordenada (base de datos).
        consultas (list): La lista de números a consultar.

    Returns:
        str: Una cadena de texto con los resultados, cada uno en una nueva línea.
    """
    resultados = []

    db_unica = sorted(list(set(db)))
    
    if not db_unica:
        #Si la base de datos está vacía, todas las respuestas son 'X X'.
        return '\n'.join(['X X'] * len(consultas))

    for q in consultas:
        limite_inferior = 'X'
        limite_superior = 'X'

        #Encontrar el límite superior 
        idx_superior = bisect.bisect_right(db_unica, q)
        
        if idx_superior < len(db_unica):
            limite_superior = db_unica[idx_superior]

        #Encontrar el límite inferior
        idx_inferior_candidato = bisect.bisect_left(db_unica, q)
        
        if idx_inferior_candidato > 0:
            limite_inferior = db_unica[idx_inferior_candidato - 1]
            
        resultados.append(f"{limite_inferior} {limite_superior}")
        
    return "\n".join(resultados)

def ejecutar_algoritmo():

    #Función que se llama al presionar el botón.
   

    try:
        #Recoger los datos de la base de datos
        db_str = db_entry.get()
        if not db_str:
            messagebox.showwarning("Advertencia", "La lista de la base de datos no puede estar vacía.")
            return
        #Convertir la cadena de texto a una lista de enteros
        database = list(map(int, db_str.split()))

        #Recoger los datos de las consultas
        consultas_str = consultas_entry.get()
        if not consultas_str:
            messagebox.showwarning("Advertencia", "La lista de consultas no puede estar vacía.")
            return
        #Convertir la cadena de texto a una lista de enteros
        consultas = list(map(int, consultas_str.split()))

        #Ejecutar el algoritmo principal
        resultado = encontrar_limites_para_consultas(database, consultas)

        #Mostrar el resultado en el campo de texto
        output_text.config(state=tk.NORMAL) #Habilitar para modificar
        output_text.delete('1.0', tk.END)   #Limpiar contenido anterior
        output_text.insert(tk.END, resultado)
        output_text.config(state=tk.DISABLED) #Deshabilitar para hacerlo de solo lectura

    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, asegúrese de ingresar solo números enteros separados por espacios.")
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ha ocurrido un error: {e}")

#Interfaz Gráfica
#Ventana principal
root = tk.Tk()
root.title("Buscador de Límites Numéricos")
root.geometry("500x550")
root.resizable(False, False)

#Estilos y fuentes
main_font = font.Font(family="Arial", size=11)
label_font = font.Font(family="Arial", size=11, weight="bold")
output_font = font.Font(family="Consolas", size=12)

#Frame principal para organizar los widgets
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

#Tamaño de la lista (informativo aunque no nesesario)
tam_lista_label = tk.Label(main_frame, text="1) Tamaño de la lista:", font=label_font)
tam_lista_label.pack(anchor="w", pady=(0, 2))
tam_lista_entry = tk.Entry(main_frame, font=main_font, width=50)
tam_lista_entry.pack(fill="x", pady=(0, 10))

#Lista de Base de Datos
db_label = tk.Label(main_frame, text="2) Lista de Base de Datos (ordenada y separada por espacios):", font=label_font)
db_label.pack(anchor="w", pady=(0, 2))
db_entry = tk.Entry(main_frame, font=main_font, width=50)
db_entry.pack(fill="x", pady=(0, 10))

#Número de Consultas (informativo tmbn)
num_consultas_label = tk.Label(main_frame, text="3) Número de consultas:", font=label_font)
num_consultas_label.pack(anchor="w", pady=(0, 2))
num_consultas_entry = tk.Entry(main_frame, font=main_font, width=50)
num_consultas_entry.pack(fill="x", pady=(0, 10))

#Lista de Números a Consultar
consultas_label = tk.Label(main_frame, text="4) Números a consultar (separados por espacios):", font=label_font)
consultas_label.pack(anchor="w", pady=(0, 2))
consultas_entry = tk.Entry(main_frame, font=main_font, width=50)
consultas_entry.pack(fill="x", pady=(0, 20))

#Botón de Ejecución
exec_button = tk.Button(
    main_frame,
    text="Ejecutar Algoritmo",
    font=label_font,
    bg="#4CAF50",
    fg="white",
    relief=tk.FLAT,
    command=ejecutar_algoritmo
)
exec_button.pack(fill="x", ipady=5, pady=(0, 20))

#Campo de Salida
output_label = tk.Label(main_frame, text="Respuesta del Algoritmo:", font=label_font)
output_label.pack(anchor="w", pady=(0, 5))

output_text = tk.Text(
    main_frame,
    height=8,
    width=50,
    font=output_font,
    state=tk.DISABLED, # Solo lectura
    bg="#f0f0f0",
    borderwidth=1,
    relief="solid"
)
output_text.pack(fill="both", expand=True)

# datos quemados para prueba
"""""
tam_lista_entry.insert(0, "5")
db_entry.insert(0, "2 4 5 7 9")
num_consultas_entry.insert(0, "4")
consultas_entry.insert(0, "2 5 6 10")
"""
# Iniciar
root.mainloop()