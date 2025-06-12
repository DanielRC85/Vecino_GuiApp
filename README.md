# Vecino GuiApp 🏡

Aplicación desarrollada con Flet en Python para ofrecer una interfaz móvil adaptativa centrada en la gestión de usuarios y servicios vecinales.

---

## 🚀 Características principales

- Login y registro de usuarios con interfaz adaptada a dispositivos móviles.
- Gestión de perfiles: ver y editar datos personales.
- Navegación fluida con barra inferior (`NavigationBar`) y menú lateral (`NavigationDrawer`).
- Imagen de logo responsiva en el login (`assets/logo.png`).
- Conexión a base de datos MySQL para manejo de autenticación y perfiles.
- Estilos organizados, diseño centrado y compatible con pantallas pequeñas (modo SafeArea).

---

## 📱 Mejora visual aplicada

- ✅ Implementación de `SafeArea` para evitar solapamiento con zonas inseguras del dispositivo móvil.
- ✅ `padding` uniforme y `spacing` en todos los controles.
- ✅ Adaptación del formulario de login con logo responsivo.
- ✅ Controles `TextField`, `FilledButton` y `TextButton` dispuestos verticalmente y centrados.
- ✅ Compatible con pantallas 360x640 y diseño no redimensionable para estética uniforme.
- ✅ Preparado para futuros temas claros, oscuros y colores pastel configurables.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- MySQL Server
- Paquetes Python:
  ```bash
  pip install flet mysql-connector-python
  ```

---

## 💠 Estructura del proyecto

```
vecino_guiapp/
├── assets/              # Imágenes como logo.png
├── views/               # login.py, register.py, perfil.py, etc.
├── components/          # navbar.py, drawer.py
├── services/            # database.py
├── main.py
└── README.md
```

---

## 🌐 Cómo subir el proyecto a GitHub

1. **Inicializa el repositorio**
   ```bash
   git init
   ```

2. **Conecta con tu repositorio remoto (ya creado en GitHub)**
   ```bash
   git remote add origin https://github.com/tu_usuario/vecino_guiapp.git
   ```

3. **Agrega tus archivos**
   ```bash
   git add .
   git commit -m "Primera versión con interfaz móvil adaptada y login con logo"
   ```

4. **Haz push al repositorio**
   ```bash
   git branch -M main
   git push -u origin main
   ```

---

## 🔒 Notas de seguridad

- Las contraseñas están protegidas mediante hashing SHA-256 antes de almacenarse o verificarse.
- Asegúrate de no subir tu archivo `config` con credenciales de tu base de datos.

---

## 📷 Captura de login adaptado

![image](https://github.com/user-attachments/assets/0d8cc4af-331b-4ae3-96a7-eed2907dfd8b)

---

## ✨ Proximas mejoras
- Integración de notificaciones vecinales.
- Interfaz para administrar servicios comunitarios.

---

Nombre: Daniel Romero
Email: romerocortesdaniel9@gmail.com
GitHub: https://github.com/DanielRC85

Desarrollado con ❤️ en Python + Flet
