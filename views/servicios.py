import flet as ft

def view():
    return ft.Column(
        [
            ft.Text("🔧 Servicios Disponibles", size=22, weight="bold"),
            ft.Text("Accede a los servicios que ofrece tu comunidad."),
            ft.ListView(
                controls=[
                    ft.ListTile(
                        title=ft.Text("Pago de administración"),
                        subtitle=ft.Text("Realiza el pago de forma rápida y segura.")
                    ),
                    ft.ListTile(
                        title=ft.Text("Reserva de zonas comunes"),
                        subtitle=ft.Text("Salón social, BBQ, parque infantil, etc.")
                    ),
                    ft.ListTile(
                        title=ft.Text("Reporte de incidencias"),
                        subtitle=ft.Text("Informa sobre problemas o daños en el conjunto.")
                    ),
                ],
                expand=True
            ),
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )
