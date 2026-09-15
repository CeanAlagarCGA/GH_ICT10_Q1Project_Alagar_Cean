from pyscript import document


def create_order(e):
    coffee = document.getElementById("coffee")
    selected_item = coffee.options[coffee.selectedIndex]

    subtotal = float(selected_item.value)
    vat = subtotal * 0.12
    total = subtotal + vat

    document.getElementById("show").textContent = selected_item.text
    document.getElementById("subtotal").textContent = subtotal
    document.getElementById("vat").textContent = vat
    document.getElementById("total").textContent =total
 








