import tkinter as tk
from tkinter import ttk
from purchase_management import PurchaseManagement
from product_management import ProductManagement
from database import Database

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Supermercado")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Abas
        self.purchase_management_tab = PurchaseManagement(self.notebook)
        self.notebook.add(self.purchase_management_tab, text="Compras")

        self.product_management_tab = ProductManagement(self.notebook)
        self.notebook.add(self.product_management_tab, text="Gerenciar Produtos")

        # Crie um frame para exibir os produtos na mesma aba
        self.product_display_frame = ttk.Frame(self.product_management_tab)
        self.product_display_frame.pack(fill=tk.BOTH, expand=True)

        # Crie um botão para exibir os produtos
        self.display_products_button = ttk.Button(self.product_management_tab, text="Exibir Produtos", command=self.display_products)
        self.display_products_button.pack()

        # Crie um botão para excluir todos os produtos
        self.delete_all_button = ttk.Button(self.product_management_tab, text="Excluir Todos os Produtos", command=self.delete_all_products)
        self.delete_all_button.pack()

        # Crie uma Treeview para exibir os produtos (inicialmente vazia)
        self.treeview = ttk.Treeview(self.product_display_frame, columns=("Produto", "Categoria", "Quantidade", "Preço de Custo", "Preço"), show="headings")
        self.treeview.heading("#1", text="Produto")
        self.treeview.heading("#2", text="Categoria")
        self.treeview.heading("#3", text="Quantidade")
        self.treeview.heading("#4", text="Preço de Custo")
        self.treeview.heading("#5", text="Preço")

        # Centralize as informações na Treeview
        for col in ("Produto", "Categoria", "Quantidade", "Preço de Custo", "Preço"):
            self.treeview.column(col, anchor="center")

        # Adicione barras de rolagem horizontal e vertical
        y_scrollbar = ttk.Scrollbar(self.product_display_frame, orient="vertical", command=self.treeview.yview)
        x_scrollbar = ttk.Scrollbar(self.product_display_frame, orient="horizontal", command=self.treeview.xview)

        self.treeview.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        self.treeview.pack(fill=tk.BOTH, expand=True)
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar.pack(side="bottom", fill="x")

    def display_products(self):
        # Limpe a Treeview antes de carregar os produtos
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Carregue dados da planilha
        db = Database("products.xlsx")
        products = db.get_all_products()
        for product in products:
            self.treeview.insert("", "end", values=product)   

    def delete_all_products(self):
        # Excluir todos os produtos da planilha
        db = Database("products.xlsx")
        db.delete_all_products()

        # Limpe a Treeview após a exclusão
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    

    # Métodos para a planilha de vendas
    def add_sale(self, product, quantity, total_price):
        try:
            df = pd.read_excel(self.sales_filename)
        
            df = pd.read_excel(self.sales_filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Produto Vendido", "Quantidade Vendida", "Preço Total"])

        new_record = pd.DataFrame({
            "Produto Vendido": [product],
            "Quantidade Vendida": [quantity],
            "Preço Total": [total_price]
        })

        df = pd.concat([df, new_record], ignore_index=True)

        df.to_excel(self.sales_filename, index=False)

    def get_all_sales(self):
        try:
            df = pd.read_excel(self.sales_filename)
            sales = df.values.tolist()
            
            df = pd.read_excel(self.sales_filename)
            sales 

            df = pd.read_excel(self.sales_filename)
            sales
            return sales
        except FileNotFoundError:
            return []



if __name__ == "__main__":
    app = Application()
    app.mainloop()



