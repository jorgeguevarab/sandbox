import flet as ft



def main(page: ft.Page):
    
    
    def agrega_num(e):
        
        print(e.control.data)
        n.value = n.value + str(e.control.data)
        page.update()
    
    def operacion(e):
        print("Se define una operación")
        
    
    t = ft.Text(value="Calculadora", color="green")
    n = ft.TextField(hint_text="Escribe un número aquí...", autofocus=True)
    page.add(t,n)
    page.add(ft.Row(controls=[ft.ElevatedButton(text="+", on_click=operacion),ft.ElevatedButton(text="-", on_click=operacion)]))
    page.add(ft.Row(controls=[ft.ElevatedButton(text="*", on_click=operacion),ft.ElevatedButton(text="/", on_click=operacion)]))
    #page.add(t, n, btn_plus, btn_minus, btn_multiple, btn_div)
    
    numbers = []
    
    
    for i in range(0,10,3):
        for j in range(3):
            
            numbers.append(
                    ft.ElevatedButton(text=str(i + j), on_click=agrega_num, data=i+j)
                )
            
            if i + j == 9:
                break
            
    for k in range(0,10,3):    
        page.add(ft.Row(controls=numbers[k:(k+3)]))
                
        page.update()    
                    
    
    #INICIO NUMBERS
   
    #END NUMBERS
    
    page.update()
    
    

ft.app(target=main)