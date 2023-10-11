import pandas as pd

class Database:
    def __init__(self, filename):
        self.filename = filename

    def add_product(self, product, category, quantity, cost_price, price):
        try:
            df = pd.read_excel(self.filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Produto", "Categoria", "Quantidade", "Preço de Custo", "Preço"])

        new_record = pd.DataFrame({
            "Produto": [product],
            "Categoria": [category],
            "Quantidade": [quantity],
            "Preço de Custo": [cost_price],
            "Preço": [price]  # Utilize a coluna "Preço" para a função anterior de "Preço de Venda"
        })

        df = pd.concat([df, new_record], ignore_index=True)

        df.to_excel(self.filename, index=False)

    def get_all_products(self):
        try:
            df = pd.read_excel(self.filename)
            products = df.values.tolist()
            return products
        except FileNotFoundError:
            return []

    def update_product_quantity(self, product, quantity_change):
        try:
            df = pd.read_excel(self.filename)
            index = df.index[df['Produto'] == product].tolist()[0]
            df.at[index, 'Quantidade'] += quantity_change

            # Correção: Se a quantidade após a venda for menor ou igual a zero, remover o registro
            if df.at[index, 'Quantidade'] <= 0:
                df = df.drop(index)

            df.to_excel(self.filename, index=False)
        except (FileNotFoundError, IndexError):
            pass

    def get_products_by_category(self, category):
        try:
            df = pd.read_excel(self.filename)
            products_in_category = df[df['Categoria'] == category]['Produto'].tolist()
            return products_in_category
        except FileNotFoundError:
            return []

    def delete_all_products(self):
        # Implemente a lógica para excluir todos os produtos da planilha
        # Certifique-se de usar a biblioteca pandas para realizar a exclusão

        df = pd.DataFrame(columns=["Produto", "Categoria", "Quantidade", "Preço de Custo", "Preço"])
        df.to_excel(self.filename, index=False)

    # Outros métodos da classe Database, se houver


