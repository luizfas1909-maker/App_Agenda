import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

import agenda_db as db


class AppAgenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Compromissos")
        self.root.geometry("860x520")
        self.item_selecionado_id = None

        self.criar_formulario()
        self.criar_tabela()
        self.carregar_compromissos()

    def criar_formulario(self):
        frame = ttk.LabelFrame(self.root, text="Dados do compromisso", padding=12)
        frame.pack(fill="x", padx=12, pady=10)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w", pady=4)
        self.nome_entry = ttk.Entry(frame, width=40)
        self.nome_entry.grid(row=0, column=1, sticky="we", padx=8, pady=4)

        ttk.Label(frame, text="Data limite (AAAA-MM-DD):").grid(
            row=0, column=2, sticky="w", pady=4
        )
        self.data_entry = ttk.Entry(frame, width=20)
        self.data_entry.grid(row=0, column=3, sticky="we", padx=8, pady=4)

        ttk.Label(frame, text="Descricao:").grid(row=1, column=0, sticky="nw", pady=4)
        self.descricao_text = tk.Text(frame, width=70, height=4)
        self.descricao_text.grid(
            row=1, column=1, columnspan=3, sticky="we", padx=8, pady=4
        )

        botoes = ttk.Frame(frame)
        botoes.grid(row=2, column=0, columnspan=4, sticky="w", pady=(10, 0))
        ttk.Button(botoes, text="Adicionar", command=self.adicionar).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(botoes, text="Atualizar", command=self.atualizar).pack(
            side="left", padx=6
        )
        ttk.Button(botoes, text="Remover", command=self.remover).pack(side="left", padx=6)
        ttk.Button(
            botoes, text="Limpar selecao", command=self.limpar_formulario
        ).pack(side="left", padx=6)
        ttk.Button(botoes, text="Recarregar", command=self.carregar_compromissos).pack(
            side="left", padx=6
        )

        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

    def criar_tabela(self):
        container = ttk.LabelFrame(self.root, text="Compromissos", padding=12)
        container.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        colunas = ("id", "nome", "descricao", "data_limite")
        self.tree = ttk.Treeview(container, columns=colunas, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("descricao", text="Descricao")
        self.tree.heading("data_limite", text="Data limite")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nome", width=220, anchor="w")
        self.tree.column("descricao", width=410, anchor="w")
        self.tree.column("data_limite", width=130, anchor="center")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        scroll = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def validar_campos(self):
        nome = self.nome_entry.get().strip()
        descricao = self.descricao_text.get("1.0", "end").strip()
        data_texto = self.data_entry.get().strip()

        if not nome:
            messagebox.showwarning("Validacao", "Informe o nome do compromisso.")
            return None

        try:
            data_limite = datetime.strptime(data_texto, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning(
                "Validacao",
                "Data invalida. Use AAAA-MM-DD, por exemplo: 2026-05-01.",
            )
            return None

        return nome, descricao, data_limite

    def carregar_compromissos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for compromisso in db.listar_compromissos():
            self.tree.insert("", "end", values=compromisso)

    def adicionar(self):
        dados = self.validar_campos()
        if not dados:
            return
        nome, descricao, data_limite = dados
        db.adicionar_compromisso(nome, descricao, data_limite)
        self.carregar_compromissos()
        self.limpar_formulario()
        messagebox.showinfo("Sucesso", "Compromisso adicionado com sucesso.")

    def atualizar(self):
        if self.item_selecionado_id is None:
            messagebox.showwarning("Atualizacao", "Selecione um compromisso na lista.")
            return
        dados = self.validar_campos()
        if not dados:
            return
        nome, descricao, data_limite = dados
        db.atualizar_compromisso(self.item_selecionado_id, nome, descricao, data_limite)
        self.carregar_compromissos()
        self.limpar_formulario()
        messagebox.showinfo("Sucesso", "Compromisso atualizado com sucesso.")

    def remover(self):
        if self.item_selecionado_id is None:
            messagebox.showwarning("Remocao", "Selecione um compromisso para remover.")
            return
        if not messagebox.askyesno("Confirmacao", "Deseja remover o compromisso selecionado?"):
            return
        db.remover_compromisso(self.item_selecionado_id)
        self.carregar_compromissos()
        self.limpar_formulario()
        messagebox.showinfo("Sucesso", "Compromisso removido com sucesso.")

    def on_select(self, _event):
        selecionado = self.tree.selection()
        if not selecionado:
            return

        valores = self.tree.item(selecionado[0], "values")
        self.item_selecionado_id = int(valores[0])
        self.nome_entry.delete(0, "end")
        self.nome_entry.insert(0, valores[1])
        self.descricao_text.delete("1.0", "end")
        self.descricao_text.insert("1.0", valores[2] if valores[2] is not None else "")
        self.data_entry.delete(0, "end")
        self.data_entry.insert(0, str(valores[3]))

    def limpar_formulario(self):
        self.item_selecionado_id = None
        self.nome_entry.delete(0, "end")
        self.data_entry.delete(0, "end")
        self.descricao_text.delete("1.0", "end")
        self.tree.selection_remove(self.tree.selection())


def main():
    root = tk.Tk()
    AppAgenda(root)
    root.mainloop()
