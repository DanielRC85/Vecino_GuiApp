import flet as ft

def view():
    return ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            [
                ft.Text(
                    "Bienvenido a Vecino GuiApp 👋",
                    size=22,
                    weight="bold",
                    text_align="center"
                ),
                ft.Image(
                    src="assets/logo.png",  # Asegúrate que el archivo exista
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN
                ),

                ft.Text(
                    "Tu comunidad conectada, más cerca que nunca.",
                    size=16,
                    text_align="center"
                ),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=320
        )
    )
