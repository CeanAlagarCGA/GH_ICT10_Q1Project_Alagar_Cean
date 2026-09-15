from pyscript import document


def generate_sku(e):

    category = document.getElementById("category")
    product = document.getElementById("product")
    stock = document.getElementById("stock")

    category_code = category.value
    product_name = product.value
    stock_quantity = stock.value

    product_code = product_name.upper()
    product_code = product_code.replace(" ", "")
    product_code = product_code[:4]

    sku = category_code + "-" + product_code + "-" + stock_quantity

    document.getElementById("sku").textContent = sku