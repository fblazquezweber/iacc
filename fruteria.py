#precios de las frutas (variable global - tipo diccionario)
precios = {
    'mandarina': 5.00,
    'manzana': 8.00,
    'pera': 9.00
}

class fruteria:
    
    def __init__(self, precios):
        self.precios = precios
        
    def fruta_disponible_precio(self):
        print("Frutas disponibles y sus precios:")
        for fruta, precio in self.precios.items():
            print(f"{fruta}: ${precio:.2f}")
    
    def fruta_seleccionada(self, fruta):
        return self.precios.get(fruta, None)

    def descuento(self, kilos):
        if kilos <= 2:
            return 0.90
        elif 2.01<= kilos <=5:
            return 0.80
        elif 5.01<= kilos <=10:
            return 0.70
        else:
            return 0.60
    
    def total_general(self, fruta, kilos):
        total = self.fruta_seleccionada(fruta)*kilos
        return total

    def total_con_descuento(self, fruta, kilos):
        total_general = self.total_general(fruta, kilos)
        print("El total es de: ", total_general)
        descuento_aplicado = self.descuento(kilos)
        print(f"Usted tiene un desceunto de: {((1-descuento_aplicado)*100):.0f} %")
        total_pagar = total_general*descuento_aplicado
        print("El total a pagar es de: ", total_pagar)

fruta = fruteria(precios)
fruta.fruta_disponible_precio()
fruta_user = input("Ingrese el nombre de la fruta que desea ").lower()
kilos_user = float(input("Ingrese la cantidad de kilos: "))
fruta.total_con_descuento(fruta_user, kilos_user)

