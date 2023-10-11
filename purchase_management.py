import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import Database

class PurchaseManagement(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.db = Database("products.xlsx")

        self.create_widgets()

    def create_widgets(self):
        # Combobox para selecionar a categoria de produtos
        self.label_select_category = ttk.Label(self, text="Selecione a Categoria:")
        self.label_select_category.pack()
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

        # Combobox para selecionar um produto da categoria selecionada
        self.label_select_product = ttk.Label(self, text="Selecione o Produto:")
        self.label_select_product.pack()
        self.product_var = tk.StringVar()
        self.product_combobox = ttk.Combobox(self, textvariable=self.product_var, values=[])
        self.product_combobox.pack()

        # Entrada para quantidade
        self.label_quantity = ttk.Label(self, text="Quantidade:")
        self.label_quantity.pack()
        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.pack()

        # Botão para confirmar a compra
        self.button_confirm_purchase = ttk.Button(self, text="Confirmar Compra", command=self.confirm_purchase)
        self.button_confirm_purchase.pack()

        # Carregar produtos ao selecionar uma categoria
        self.category_combobox.bind("<<ComboboxSelected>>", self.load_products_by_category)

    def confirm_purchase(self):
        category = self.category_var.get()
        product = self.product_var.get()
        quantity = self.entry_quantity.get()

        if category and product and quantity:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    messagebox.showerror("Erro", "Quantidade inválida. Digite um número inteiro positivo.")
                else:
                    self.db.update_product_quantity(product, -quantity)
                    messagebox.showinfo("Sucesso", f"Compra de {quantity} unidades de {product} confirmada.")
                    self.entry_quantity.delete(0, "end")
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida. Digite um número inteiro positivo.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def load_products_by_category(self, event):
        selected_category = self.category_var.get()
        if selected_category:
            products_in_category = self.db.get_products_by_category(selected_category)
            self.product_combobox['values'] = products_in_category
        else:
            self.product_combobox['values'] = []

        # Limpar o campo de seleção de produto
        self.product_var.set("")

