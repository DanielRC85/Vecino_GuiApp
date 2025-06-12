import flet as ft
from views import login, register, home, noticias, servicios, perfil, editar_perfil, configuracion
from components.navbar import navbar
from components.drawer import navigation_drawer

def main(page: ft.Page):
    page.title = "Vecino GuiApp"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 360
    page.window_height = 640
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    content = ft.Container(expand=True)

    def change_view(name):
        if name == "login":
            content.content = login.view(change_view)
            page.appbar = None
            page.drawer = None
        elif name == "register":
            content.content = register.view(change_view)
            page.appbar = None
            page.drawer = None
        elif name == "main":
            cargar_layout_principal()
        elif name == "editar_perfil":
            content.content = editar_perfil.view(page, change_view)
        elif name == "configuracion":
            content.content = configuracion.configuracion_view(page, change_view)
        page.update()

    def cambiar_pestaña(index):
        vistas = [
            home.view(),
            noticias.view(),
            servicios.view(),
            perfil.view(page, change_view),
        ]
        layout = page.data.get("layout")
        if layout:
            layout.controls[0].content = vistas[index]
            page.update()

    def cargar_layout_principal():
        def toggle_drawer(_):
            if page.drawer:
                page.drawer.open = True
                page.update()

        page.appbar = ft.AppBar(
            title=ft.Text("Vecino GuiApp"),
            leading=ft.IconButton(icon=ft.Icons.MENU, on_click=toggle_drawer),
            center_title=True
        )
        page.drawer = navigation_drawer(page, change_view)

        layout = ft.Column([
            ft.Container(content=home.view(), expand=True),
            navbar(page, cambiar_pestaña)
        ])
        page.data["layout"] = layout
        content.content = layout

    page.data = {}
    change_view("login")
    page.add(content)

if __name__ == "__main__":
    ft.app(target=main)
