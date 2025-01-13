product_name, product_code = input().split()
product_code = int(product_code)

class market:
    def __init__(self, product_name = "codetree", product_code = "50"):
        self.product_name = product_name
        self.product_code = product_code

product1 = market()
print("product", product1.product_code, "is", product1.product_name)
product2 = market(product_name, product_code)
print("product", product2.product_code, "is", product2.product_name)