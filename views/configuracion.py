import flet as ft

def configuracion_view(page: ft.Page, change_view):
    def aplicar_tema(modo: str, color: str):
        page.theme_mode = modo  # "light" o "dark"

        if color == "lavanda":
            page.theme = ft.Theme(color_scheme_seed="#cbaacb")
        elif color == "menta":
            page.theme = ft.Theme(color_scheme_seed="#a0e7e5")
        elif color == "durazno":
            page.theme = ft.Theme(color_scheme_seed="#fbc4ab")
        else:
            page.theme = ft.Theme(color_scheme_seed="blue")  # color por defecto

        page.update()

    def set_modo(modo):
        aplicar_tema(modo, color_actual.value)

    def set_color(color):
        aplicar_tema(page.theme_mode, color)
        color_actual.value = color
        page.update()

    color_actual = ft.Text(value="lavanda", visible=False)

    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        padding=30,
        content=ft.Column(
            [
                ft.Text("🎨 Personalizar Apariencia", size=24, weight="bold"),
                ft.Text("Selecciona el modo de tema:"),
                ft.Row(
                    [
                        ft.ElevatedButton("Claro", on_click=lambda e: set_modo("light")),
                        ft.ElevatedButton("Oscuro", on_click=lambda e: set_modo("dark")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text("Selecciona un color pastel:"),
                ft.Row(
                    [
                        ft.FilledButton("Lavanda", on_click=lambda e: set_color("lavanda")),
                        ft.FilledButton("Menta", on_click=lambda e: set_color("menta")),
                        ft.FilledButton("Durazno", on_click=lambda e: set_color("durazno")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.TextButton("⬅️ Volver", on_click=lambda e: change_view("main")),
                color_actual  # oculto para mantener el estado
            ],
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320
        )
    )
