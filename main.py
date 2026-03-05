import flet as ft
def main(page: ft.Page):
    
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20
    

    nombre_input = ft.TextField(label="Nombre completo")
    email_input = ft.TextField(label="Correo electrónico")
    
    taller_dropdown = ft.Dropdown(
        label="Taller de interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )
    
    pago_radio = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ]),
        value="Pago completo" 
    )
    
    laptop_check = ft.Checkbox(label="Requiere computadora portátil", value=False)
    
    nivel_text = ft.Text("Nivel: 1")
    def slider_changed(e):
        nivel_text.value = f"Nivel: {int(nivel_slider.value)}"
        page.update()
        
    nivel_slider = ft.Slider(
        min=1, max=5, divisions=4, value=1, 
        label="{value}", on_change=slider_changed
    )
    
    resumen_text = ft.Text(size=16,) 

    
    def mostrar_ficha(e):
        requiere_pc = "Sí" if laptop_check.value else "No"
        
        resumen_text.value = (
            f"--- FICHA DEL PARTICIPANTE ---\n\n"
            f"Nombre: {nombre_input.value}\n"
            f"Email: {email_input.value}\n"
            f"Taller: {taller_dropdown.value}\n"
            f"Pago: {pago_radio.value}\n"
            f"Requiere Portátil: {requiere_pc}\n"
            f"Nivel de Experiencia: {int(nivel_slider.value)}\n\n"
            f"--- Gracias por su registro ---"
        )
        page.update()

    page.add(
        ft.Column(
            controls=[
                
                ft.Row(
                    [ft.Text("Registro de Participantes", size=30, weight=ft.FontWeight.BOLD)],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
                nombre_input,
                email_input,

                taller_dropdown,
                
                ft.Column([
                    ft.Text("Modalidad de pago:", weight=ft.FontWeight.W_500),
                    pago_radio
                ]),
                
                laptop_check,
                
                
                ft.Column([
                    nivel_text,
                    nivel_slider
                ], spacing=0),
                
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Mostrar Ficha del Participante",
                            on_click=mostrar_ficha
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
                resumen_text
            ],
            spacing=15 
        )
    )

ft.run(main)

