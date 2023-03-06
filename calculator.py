import flet as ft



def main(page: ft.Page):
    
    
    def agrega_num(e):
        print(e.value)
    
    def operacion(e):
        print("Se define una operación")
        
    
    t = ft.Text(value="Calculadora", color="green")
    n = ft.TextField(hint_text="Escribe un número aquí...", autofocus=True)
    page.add(t,n)
    page.add(ft.Row(controls=[ft.ElevatedButton(text="+", on_click=operacion),ft.ElevatedButton(text="-", on_click=operacion)]))
    page.add(ft.Row(controls=[ft.ElevatedButton(text="*", on_click=operacion),ft.ElevatedButton(text="/", on_click=operacion)]))
    #page.add(t, n, btn_plus, btn_minus, btn_multiple, btn_div)
    
    controls = []
    
    for i in range(0,10):
        controls.append(ft.ElevatedButton(text=str(i), on_click=agrega_num))
    
        page.add(controls[i])   
   
    
    page.update()
    
    

ft.app(target=main)