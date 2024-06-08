import tkinter as tk
from tkinter import messagebox

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            return f"Contato '{nome}' já existe."
        else:
            self.contatos[nome] = telefone
            return f"Contato '{nome}' adicionado com sucesso."

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            return f"Contato '{nome}' removido com sucesso."
        else:
            return f"Contato '{nome}' não encontrado."

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            return f"Contato '{nome}': {self.contatos[nome]}"
        else:
            return f"Contato '{nome}' não encontrado."

    def listar_contatos(self):
        if not self.contatos:
            return "A agenda está vazia."
        else:
            return "\n".join([f"Nome: {nome}, Telefone: {telefone}" for nome, telefone in self.contatos.items()])

class InterfaceAgenda:
    def __init__(self, root):
        self.agenda = AgendaTelefonica()
        self.root = root
        self.root.title("Agenda Telefônica")
        self.root.geometry("400x400")
        self.root.configure(bg="#e6f7ff")

        # Adicionando elementos da interface
        self.label_nome = tk.Label(root, text="Nome:", bg="#e6f7ff")
        self.label_nome.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        self.label_telefone = tk.Label(root, text="Telefone:", bg="#e6f7ff")
        self.label_telefone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_telefone = tk.Entry(root, width=30)
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=5)

        self.btn_adicionar = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato, bg="#b3e0ff")
        self.btn_adicionar.grid(row=2, column=0, columnspan=2, pady=5)

        self.btn_remover = tk.Button(root, text="Remover Contato", command=self.remover_contato, bg="#b3e0ff")
        self.btn_remover.grid(row=3, column=0, columnspan=2, pady=5)

        self.btn_pesquisar = tk.Button(root, text="Pesquisar Contato", command=self.pesquisar_contato, bg="#b3e0ff")
        self.btn_pesquisar.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_listar = tk.Button(root, text="Listar Contatos", command=self.listar_contatos, bg="#b3e0ff")
        self.btn_listar.grid(row=5, column=0, columnspan=2, pady=5)

        self.text_area = tk.Text(root, height=10, width=50, state='disabled', bg="#e6f7ff")
        self.text_area.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        resultado = self.agenda.adicionar_contato(nome, telefone)
        messagebox.showinfo("Resultado", resultado)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

    def remover_contato(self):
        nome = self.entry_nome.get()
        resultado = self.agenda.remover_contato(nome)
        messagebox.showinfo("Resultado", resultado)
        self.entry_nome.delete(0, tk.END)

    def pesquisar_contato(self):
        nome = self.entry_nome.get()
        resultado = self.agenda.pesquisar_contato(nome)
        self.text_area.config(state='normal')
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, resultado)
        self.text_area.config(state='disabled')
        self.entry_nome.delete(0, tk.END)

    def listar_contatos(self):
        resultado = self.agenda.listar_contatos()
        self.text_area.config(state='normal')
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, resultado)
        self.text_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    interface = InterfaceAgenda(root)
    root.mainloop()
