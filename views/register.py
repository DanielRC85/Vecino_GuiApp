import flet as ft
import hashlib
import time
from services.database import db

def view(change_view):
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Campos de entrada
    nombre = ft.TextField(label="Nombre completo", width=300)
    username = ft.TextField(label="Nombre de usuario", width=300)
    email = ft.TextField(label="Correo electrónico", width=300)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text("", color=ft.Colors.RED_500)

    def registrar(e):
        if not all([nombre.value.strip(), username.value.strip(), email.value.strip(), password.value.strip()]):
            mensaje.value = "⚠️ Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED_500
            e.page.update()
            return

        if db.verificar_existencia_usuario(username.value.strip(), email.value.strip()):
            mensaje.value = "❌ El usuario o correo ya existe"
            mensaje.color = ft.Colors.RED_500
            e.page.update()
            return

        hash_pass = hash_password(password.value.strip())
        ok = db.agregar_usuario(username.value.strip(), email.value.strip(), hash_pass, nombre.value.strip())

        if ok:
            mensaje.value = "✅ Usuario agregado correctamente"
            mensaje.color = ft.Colors.GREEN_600
            e.page.update()
            time.sleep(1.5)
            change_view("login")
        else:
            mensaje.value = "❌ Error al registrar usuario"
            mensaje.color = ft.Colors.RED_500
            e.page.update()

    def volver_al_login(e):
        change_view("login")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Registro de Usuario", size=26, weight="bold", text_align=ft.TextAlign.CENTER),
                nombre,
                username,
                email,
                password,
                ft.FilledButton("Registrarse", on_click=registrar),
                ft.TextButton("¿Ya tienes cuenta? Inicia sesión", on_click=volver_al_login),
                mensaje
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        expand=True,
        padding=40
    )
