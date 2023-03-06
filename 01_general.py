
#Declarations
cost, fee, tax, revenue, shipping = 0,0,0,0,0
RT_ICA = 0.002
RT_FTE = 0.015

#Basic Functions here

#This functions validate the input, making sure the inputs match the data type expected 
def validate_number(input_prompt=""):
    while True:
        try:
            value = int(input(input_prompt)) 
            return value
        except ValueError:
            print("No válido, vuelva a intentarlo") 
            
def calculate():
    #Gathering user data
    cost = validate_number("Costo del producto (Antes de IVA): ")
    tax = validate_number("Impuesto: ")
    fee = validate_number("Comisión MELI: ")
    revenue = validate_number("Márgen de ganancia: ")
    shipping = validate_number("Costo de envío: ")
    
    # Calculating basics
    
    total_cost = cost * (1 + (tax/100))
    print(f"Costo IVA incluido: {total_cost} \n")
    
    pvp = total_cost / (1-(revenue/100))

    pvp_meli = pvp / (1-(fee/100))
    print(f"Precio sugerido: {round(pvp_meli,0)} \n")
    
    
    discounts_rt = (pvp_meli * RT_FTE) + (pvp_meli * RT_ICA)
    print(f"Se descontarán: {round(discounts_rt,2)} en retenciones.\n")
    
    total_revenue = total_cost - (shipping + discounts_rt + (pvp_meli * (fee/100)))
    print(f"Total ingreso bruto: $ {total_revenue :,.0f} \n")
    
    return total_revenue

    
       


#Run function
def run():
    calculate()


    while True:
        res = input("¿Deseas realizar un nuevo cálculo? \n(Presiona 'S' para sí y cualquier tecla para cancelar.) ")
        if res.lower() == "s":
            calculate()
        else:
            break
   
#Code here

#Entry point 
if __name__ == '__main__':
    run()
    