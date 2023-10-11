import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import Database

class ProductManagement(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.db = Database("products.xlsx")
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para o nome do produto
        self.label_product = ttk.Label(self, text="Nome do Produto:")
        self.label_product.pack()
        self.entry_product = ttk.Entry(self)
        self.entry_product.pack()

        # Label e Combobox para a categoria do produto
        self.label_category = ttk.Label(self, text="Categoria:")
        self.label_category.pack()
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self, textvariable=self.category_var, values=[
            "Alimentos Perecíveis",
            "Produtos Secos e Enlatados",
            "Bebidas",
            "Produtos de Limpeza",
            "Produtos de Higiene Pessoal",
            "Produtos de Cuidados com o Lar",
            "Produtos de Bebê e Criança",
            "Produtos de Saúde",
            "Produtos de Confeitaria",
            "Produtos de Limpeza Doméstica"
        ])
        self.category_combobox.pack()

        # Entrada para quantidade
        self.label_quantity = ttk.Label(self, text="Quantidade:")
        self.label_quantity.pack()
        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.pack()

        # Entrada para o preço de custo
        self.label_cost_price = ttk.Label(self, text="Preço de Custo:")
        self.label_cost_price.pack()
        self.entry_cost_price = ttk.Entry(self)
        self.entry_cost_price.pack()

        # Adicione um novo Label e Entry para o preço de venda
        self.label_selling_price = ttk.Label(self, text="Preço de Venda:")
        self.label_selling_price.pack()
        self.entry_selling_price = ttk.Entry(self)
        self.entry_selling_price.pack()

        # Botão para adicionar produto
        self.button_add_product = ttk.Button(self, text="Adicionar Produto", command=self.add_product)
        self.button_add_product.pack()

    def add_product(self):
        product = self.entry_product.get()
        category = self.category_var.get()
        quantity = self.entry_quantity.get()
        cost_price = self.entry_cost_price.get()
        selling_price = self.entry_selling_price.get()  # Obtenha o preço de venda

        if product and category and quantity and cost_price and selling_price:
            try:
                quantity = int(quantity)
                cost_price = float(cost_price)
                selling_price = float(selling_price)  # Converta o preço de venda para float

                if quantity <= 0 or cost_price <= 0 or selling_price <= 0:
                    messagebox.showerror("Erro", "Quantidade e preços devem ser maiores que zero.")
                else:
                    self.db.add_product(product, category, quantity, cost_price, selling_price)  # Passe o preço de venda
                    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso.")
                    self.clear_entries()
            except ValueError:
                messagebox.showerror("Erro", "Valores inválidos. Certifique-se de usar números válidos.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def clear_entries(self):
        self.entry_product.delete(0, "end")
        self.category_combobox.set("")
        self.entry_quantity.delete(0, "end")
        self.entry_cost_price.delete(0, "end")
        self.entry_selling_price.delete(0, "end")  # Limpe o campo do preço de venda
