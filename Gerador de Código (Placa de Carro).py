import tkinter as tk
import random
import string

def gerar_codigo_placa():
    # Gerar código de placa aleatório no formato AAA-00A0
    prefixo = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros1 = ''.join(random.choices(string.digits, k=1))
    sufixo = ''.join(random.choices(string.ascii_uppercase, k=1))
    numeros2 = ''.join(random.choices(string.digits, k=2))
    codigo_placa = f"{prefixo}-{numeros1}{sufixo}{numeros2}"
    label_resultado.config(text=codigo_placa)

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Código de Placa")
root.configure(bg='#2A6200')  # Fundo escuro

# Criar o botão e o label
label_resultado = tk.Label(root, text="", font=("Courier", 18, "bold"), fg="white", bg="#87005F")
label_resultado.pack(pady=20)
botao_gerar = tk.Button(root, text="Gerar Código", font=("Arial", 14), command=gerar_codigo_placa, bg="#58006E", fg="white")
botao_gerar.pack(pady=10)

# Executar a janela
root.mainloop()
