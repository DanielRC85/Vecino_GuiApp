import flet as ft
from services.database import db

def view(page: ft.Page, change_view):
    user_id = page.session.get("user_id")
    user = db.get_user_by_id(user_id)

    if not user:
        return ft.Text("❌ Usuario no encontrado")

    nombre_input = ft.TextField(label="Nombre completo", value=user.get("full_name", ""))
    email_input = ft.TextField(label="Correo electrónico", value=user["email"])
    mensaje = ft.Text("")

    def guardar(e):
        nuevo_nombre = nombre_input.value.strip()
        nuevo_email = email_input.value.strip()

        if not nuevo_nombre or not nuevo_email:
            mensaje.value = "⚠️ Todos los campos son obligatorios."
            mensaje.color = "red"
            page.update()
            return

        ok = db.actualizar_usuario(user_id, nuevo_email, nuevo_nombre)

        if ok:
            mensaje.value = "✅ Perfil actualizado correctamente."
            mensaje.color = "green"
        else:
            mensaje.value = "❌ Error al actualizar perfil."
            mensaje.color = "red"
        page.update()

    def cancelar(e):
        change_view("main")

    return ft.Container(
        alignment=ft.alignment.center,
        padding=30,
        expand=True,
        content=ft.Column(
            controls=[
                ft.Text("✏️ Editar Perfil", size=24, weight="bold"),
                ft.Text(f"👤 Usuario: {user['username']}", color="purple"),
                email_input,
                nombre_input,
                ft.Row(
                    [
                        ft.ElevatedButton("Guardar cambios", on_click=guardar),
                        ft.OutlinedButton("Regresar", on_click=cancelar)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensaje
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=300  # esto limita el ancho del formulario como en login
        )
    )
