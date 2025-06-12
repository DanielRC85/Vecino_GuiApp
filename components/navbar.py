import flet as ft

def navbar(page, on_change):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.NEWSPAPER, label="Noticias"),
            ft.NavigationBarDestination(icon=ft.Icons.BUILD, label="Servicios"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        on_change=lambda e: on_change(e.control.selected_index)
    )
