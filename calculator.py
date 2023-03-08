import flet as ft



def main(page: ft.Page):
    
    
    def agrega_num(e):
        
        print(e.control.data)
        n.value = n.value + str(e.control.data)
        page.update()
    
    def operacion(e):
        print("Se define una operación")
    
    #LABEL AND TEXTBOX    
    t = ft.Text(value="Calculadora", color="green")
    n = ft.TextField(hint_text="Escribe un número aquí...", autofocus=True)
    page.add(t,n)
    
    #NUMBERS SECTION
    numbers = []
    
    for i in range(0,10):
        
        numbers.append(
                    ft.ElevatedButton(text=str(i), on_click=agrega_num, data=i)
                )       
        
    for j in range(0,10,3):    
        page.add(ft.Row(controls=numbers[j:(j+3)]))
                
    #OPERATORS SECTION********************************
    
    page.add(ft.Column(controls=[ft.ElevatedButton(text="+", on_click=operacion),ft.ElevatedButton(text="-", on_click=operacion)]))
    page.add(ft.Row(controls=[ft.ElevatedButton(text="*", on_click=operacion),ft.ElevatedButton(text="/", on_click=operacion)]))    
    
    page.update()            

ft.app(target=main)