class Category():
    name: str
    description: str
    __products: list

    total_category = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.total_category =+ 1
        Category.total_products =+ len(self.__products)

    def add_product(self, products):
        self.__products.append(products)

    @property
    def products(self):
        return f'{self.__products[0][0]}, {self.__products[0][2]} руб. Остаток: {self.__products[0][3]} шт'


