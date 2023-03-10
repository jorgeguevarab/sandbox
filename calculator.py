import flet as ft

on_calc = False
eval_string = ""

def main(page: ft.Page):
    
    page.title = "Calculadora Flet"
    
    def agrega_num(e):
        global eval_string, on_calc        
                
        if on_calc == True:
            n.value = ""
            n.value = n.value + str(e.control.data)
            
            on_calc = False
            
        else:
            n.value = n.value + str(e.control.data)
            
        #prueba.value =  n.value
    
        page.update()
    
    def operacion(e):
        
        global eval_string, on_calc
        
        on_calc = True
        operador = e.control.data
        
        prueba.value = prueba.value + n.value + operador
        
        if operador == "=":
            resultado = eval(str.removesuffix(prueba.value,"="))
            print(resultado)
            n.value = resultado
            prueba.value = ""
        
            
            
        page.update()
        
        
    def limpiar(e):
        global on_calc
        
        n.value = ""
        prueba.value = ""
        on_calc = False
        page.update()
        
        
            
    
    
    #LABEL AND TEXTBOX    
    
    t = ft.Text(value="Calculadora", color="green")
    n = ft.TextField(hint_text="Escribe un número aquí...", autofocus=True, text_align="right", read_only=True)
    prueba = ft.TextField(visible=False)
    
    page.add(t,n,prueba)
    
    #NUMBERS SECTION
    numbers = []
    
    for i in range(0,10):
        
        numbers.append(
                    ft.ElevatedButton(text=str(i), on_click=agrega_num, data=i)
                )
    numbers.append(ft.ElevatedButton(text=",", on_click=agrega_num, data=","))       
     
    for j in range(0,10,3):    
        page.add(
            ft.Column(controls=[
            ft.Container(
                content=ft.Row(controls=numbers[j:(j+3)]),
                width=200
                )]
            )
            )
                
    #OPERATORS SECTION********************************
    
    
    btn_operators=[
        ft.ElevatedButton(text="+", on_click=operacion, data="+"),
        ft.ElevatedButton(text="-", on_click=operacion, data="-"),
        ft.ElevatedButton(text="*", on_click=operacion, data="*"),
        ft.ElevatedButton(text="/", on_click=operacion, data="/"),
        ft.ElevatedButton(text="=", on_click=operacion, data="=")
        ]
    
    
    page.add(
        
        ft.Column(
            controls=[
        ft.Container(

        content=   
        ft.Row(
            controls=btn_operators,
            wrap=True,
            spacing=10,
            run_spacing=20,
            width=160
            
        )
    
        ), ft.ElevatedButton(text="Limpiar",on_click=limpiar)
        ])
        
    )

        
    
    page.update()     
         

ft.app(target=main)