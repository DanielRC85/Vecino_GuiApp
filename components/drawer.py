import flet as ft

def navigation_drawer(page, change_view):
    def _select(view_name):
        change_view(view_name)
        if page.drawer:
            page.drawer.open = False
            page.update()

    return ft.NavigationDrawer(
        controls=[
            ft.Container(padding=16, content=ft.Text("Menú", size=18, weight="bold")),
            ft.Divider(),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.EDIT),
                title=ft.Text("Editar perfil"),
                on_click=lambda e: _select("editar_perfil")
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SETTINGS),
                title=ft.Text("Configuración"),
                on_click=lambda e: _select("configuracion")
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.LOGOUT),
                title=ft.Text("Cerrar sesión"),
                on_click=lambda e: _select("login")
            ),
        ]
    )
