import flet as ft

def view():
    return ft.Column(
        [
            ft.Text("📰 Noticias Recientes", size=22, weight="bold"),
            ft.Text("Aquí encontrarás las últimas novedades de tu comunidad."),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Reunión de vecinos este viernes a las 6PM.")),
                    ft.ListTile(title=ft.Text("Nuevo servicio de reciclaje inicia la próxima semana.")),
                    ft.ListTile(title=ft.Text("Se instalaron nuevas cámaras de seguridad.")),
                ],
                expand=True
            ),
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )
