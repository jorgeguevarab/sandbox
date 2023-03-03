from tkinter import *

# Declarations
cost, fee, tax, revenue, shipping = 0,0,0,0,0
RT_ICA = 0.002
RT_FTE = 0.015

# Basic Functions here

# This functions validate the input, making sure the inputs match the data type expected 
def validate_number(input_prompt="", label=None):
    while True:
        try:
            value = int(label.get()) 
            return value
        except ValueError:
            print("No válido, vuelva a intentarlo") 

def calculate(label_cost, label_tax, label_fee, label_revenue, label_shipping):
    # Gathering user data
    cost = validate_number(label=label_cost)
    tax = validate_number(label=label_tax)
    fee = validate_number(label=label_fee)
    revenue = validate_number(label=label_revenue)
    shipping = validate_number(label=label_shipping)

    # Calculating basics
    total_cost = cost * (1 + (tax/100))
    label_total_cost.config(text=f"Costo IVA incluido: {total_cost}")
    
    pvp = total_cost / (1-(revenue/100))
    pvp_meli = pvp / (1-(fee/100))
    label_pvp_meli.config(text=f"Precio sugerido: {round(pvp_meli,0)}")
    
    discounts_rt = (pvp_meli * RT_FTE) + (pvp_meli * RT_ICA)
    label_discounts.config(text=f"Se descontarán: {round(discounts_rt,2)} en retenciones.")
    
    total_revenue = total_cost - (shipping + discounts_rt + (pvp_meli * (fee/100)))
    label_total_revenue.config(text=f"Total ingreso bruto: $ {total_revenue :,.0f}")

def recalculate():
    calculate(label_cost, label_tax, label_fee, label_revenue, label_shipping)

# GUI
root = Tk()

# Labels
label_cost = Entry(root)
label_tax = Entry(root)
label_fee = Entry(root)
label_revenue = Entry(root)
label_shipping = Entry(root)
label_total_cost = Label(root)
label_pvp_meli = Label(root)
label_discounts = Label(root)
label_total_revenue = Label(root)

# Buttons
button_calculate = Button(root, text="Calcular", command=recalculate)

# Grid
label_cost.grid(row=0, column=1)
label_tax.grid(row=1, column=1)
label_fee.grid(row=2, column=1)
label_revenue.grid(row=3, column=1)
label_shipping.grid(row=4, column=1)
label_total_cost.grid(row=5, column=1)
label_pvp_meli.grid(row=6, column=1)
label_discounts.grid(row=7, column=1)
label_total_revenue.grid(row=8, column=1)
button_calculate.grid(row=9, column=1)

# Labels descriptions
Label(root, text="Costo del producto (Antes de IVA): ").grid(row=0, column=0)
Label(root, text="Impuesto: ").grid(row=1, column=0)
Label(root, text="Comisión MELI: ").grid(row=2, column=0)
Label(root, text="Márgen de ganancia: ").grid(row=3, column=0)
Label(root, text="Costo de envío: ").grid(row=4, column=0)

root.mainloop()
