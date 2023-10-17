total_price = 0
product_list = []

while True:
    product = input("Ingrese el producto que desea comprar, si ya no quiere agregar más, inserte 0: ").lower()
    if product == "0":
        break
    else:
        product_list.append(product)

print("Lista de productos:")
print(product_list)

for p in product_list:
    find_product = input(f"Ingrese si/no si encontró el producto {p}: ").lower()
    if find_product=="no":
        while True:
                replace_product=input(f"El producto {p} no esta disponible , ingrese si/no si desea remplazarlo ").lower()
                if replace_product=="si" :
                    p=input("Ingrese por que producto lo desea remplaza ")
                    find_product="si"
                    break
                elif  replace_product=="no":
                    break
    if find_product == "si" :
        product_price = float(input(f"Ingrese el precio del producto {p}: "))
        have_discount = input(f"Ingrese si/no si el precio tiene descuento para {p}: ").lower()
        if have_discount == "si":
            product_discount = float(input(f"Ingrese el descuento para {p}: "))
            if product_discount >= product_price:
                print("El descuento no puede ser mayor o igual al precio del producto.")
                while product_discount>product_price:
                    product_price=int(input(f"Ingrese nuevamente el descuento o ingrese 0 si el producto {p}no posee descuento "))
            
            product_price -= product_discount
            print(f"El valor final del producto {p} es de {product_price}")
            total_price += product_price
        elif  product_discount=="no":
            break

print(f"El precio total de la compra es de {total_price}")

payment_method = int(input("Ingrese 1 para pago en efectivo "))

if payment_method == 1:
    discount = (total_price * 0.20)
    print(f"El descuento por pagar en efectivo es de {discount}")
    total_price -= discount

print(f"El total de la compra es de: {total_price}")
