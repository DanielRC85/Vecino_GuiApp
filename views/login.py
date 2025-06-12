import flet as ft
from services.database import db
import hashlib

def view(change_view):
    username_input = ft.TextField(label="Usuario", autofocus=True, width=300)
    password_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje_error = ft.Text(value="", color=ft.Colors.RED_500)

    def ir_a_registro(e):
        change_view("register")

    def iniciar_sesion(e):
        username = username_input.value.strip()
        password = password_input.value.strip()

        if not username or not password:
            mensaje_error.value = "❗ Debes llenar todos los campos."
            e.page.update()
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        usuario = db.verificar_usuario(username, password_hash)

        if usuario:
            mensaje_error.value = ""
            e.page.session.set("user_id", usuario["id"])
            e.page.session.set("username", usuario["username"])
            change_view("main")
        else:
            mensaje_error.value = "❌ Usuario o contraseña incorrectos."
        e.page.update()

    return ft.Container(
        content=ft.Column(
            [
                # LOGO
                ft.Image(
                    src="assets/logo.png",  # Asegúrate que exista en esa ruta
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN
                ),

                # ESLOGAN
                ft.Text(
                    "Tu comunidad conectada, más cerca que nunca.",
                    size=16,
                    text_align="center"
                ),

                # TÍTULO
                ft.Text("Iniciar Sesión", size=26, weight="bold", text_align=ft.TextAlign.CENTER),

                # CAMPOS Y BOTONES
                username_input,
                password_input,
                mensaje_error,
                ft.FilledButton("Entrar", on_click=iniciar_sesion),
                ft.TextButton("¿No tienes cuenta? Regístrate", on_click=ir_a_registro)
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        expand=True,
        padding=40
    )
