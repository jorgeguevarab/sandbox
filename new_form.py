import flet as ft

def main(page: ft.Page):
    
    def items(count):
        items = []
        for i in range(0, count):
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text=str(i)),
                    alignment=ft.alignment.center,
                    width=40,
                    height=40,
                    border_radius=ft.border_radius.all(0),
                )
            )
        return items

    def slider_change(e):
        row.width = float(e.control.value)
        row.update()

    width_slider = ft.Slider(
        min=0,
        max=page.window_width,
        divisions=20,
        value=page.window_width,
        label="{value}",
        on_change=slider_change,
    )

    row = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(10),
        width=page.window_width,
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Change the row width to see how child items wrap onto multiple rows:"
                ),
                width_slider,
            ]
        ),
        row,
    )

ft.app(target=main)