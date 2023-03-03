def validate_number(input_prompt=""):
    while True:
        try:
            value = int(input(input_prompt)) 
            return value
        except ValueError:
            print("No es válido") 
        
        
cost = validate_number("Escribe el costo: ")
fee = validate_number("Comisión: ")
tax = validate_number("Impuesto (16 o 0) ")
revenue = validate_number("Margen de utilidad: ")

print("Por fin")


