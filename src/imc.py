import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        # Passo 3: Criando a Interface Gráfica
        # Rótulo para Altura
        self.height_label = tk.Label(root, text="Altura (m):")
        self.height_label.grid(row=0, column=0, padx=10, pady=10)

        # Entrada para Altura
        self.height_entry = tk.Entry(root, text="Favor colocar em cm")
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        # Rótulo para Peso
        self.weight_label = tk.Label(root, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)

        # Entrada para Peso
        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botão para Calcular IMC
        self.calculate_button = tk.Button(root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Rótulo para Resultado
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Passo 4: Criando as Funções da Calculadora de IMC
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Categoria: {category}")

# Passo 5: Executando o Programa Principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
