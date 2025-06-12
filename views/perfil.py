import flet as ft
from services.database import db

def view(page: ft.Page, change_view):
    user_id = page.session.get("user_id")
    user = db.get_user_by_id(user_id)

    if not user:
        return ft.Text("❌ Usuario no encontrado")

    avatar = ft.Image(
        src=user.get("avatar_url", "assets/default_avatar.png"),
        width=120,
        height=120
    )

    username = ft.Text(f"👤 Usuario: {user['username']}")
    email = ft.Text(f"📧 Email: {user['email']}")
    full_name = ft.Text(f"📛 Nombre: {user['full_name'] or 'No especificado'}")

    mensaje = ft.Text("")

    def editar(e):
        change_view("editar_perfil")

    return ft.Column(
        controls=[
            ft.Text("👤 Perfil de Usuario", size=24, weight="bold"),
            avatar,
            username,
            email,
            full_name,
            ft.Row(
                [ft.ElevatedButton("Editar perfil", on_click=editar)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            mensaje
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
