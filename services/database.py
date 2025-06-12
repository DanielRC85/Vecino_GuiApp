import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                port=3306,
                password="",
                database="giapp_db"
            )
            if self.connection.is_connected():
                print("✅ Conexión exitosa a MySQL")
        except Error as e:
            print("❌ Error al conectar a MySQL:", e)
            self.connection = None

    def obtener_usuarios(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT id, username, email, full_name FROM users")
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Error as e:
            print("❌ Error al obtener usuarios:", e)
            return []

    def agregar_usuario(self, username, email, password_hash, full_name=None):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO users (username, email, password_hash, full_name)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (username, email, password_hash, full_name))
            self.connection.commit()
            cursor.close()
            print("✅ Usuario agregado correctamente")
            return True
        except Error as e:
            print("❌ Error al agregar usuario:", e)
            return False

    def verificar_usuario(self, username, password_hash):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
                SELECT * FROM users 
                WHERE username = %s AND password_hash = %s
            """
            cursor.execute(query, (username, password_hash))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Error as e:
            print("❌ Error al verificar usuario:", e)
            return None

    def verificar_existencia_usuario(self, username, email):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado is not None
        except Error as e:
            print("❌ Error verificando existencia de usuario:", e)
            return True  # Previene registros si falla

    # ✅ Obtener usuario por ID
    def get_user_by_id(self, user_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Error as e:
            print("❌ Error al obtener usuario por ID:", e)
            return None

    # ✅ Obtener usuario por nombre de usuario
    def get_user_by_username(self, username):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Error as e:
            print("❌ Error al obtener usuario por nombre de usuario:", e)
            return None

    # ✅ Actualizar usuario (email, nombre y contraseña opcional)
    def actualizar_usuario(self, user_id, nuevo_email, nuevo_nombre):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE users SET email = %s, full_name = %s WHERE id = %s",
                (nuevo_email, nuevo_nombre, user_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("❌ Error al actualizar usuario:", e)
            return False

    # ✅ Eliminar usuario
    def eliminar_usuario(self, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            self.connection.commit()
            cursor.close()
            print("🗑️ Usuario eliminado correctamente")
            return True
        except Error as e:
            print("❌ Error al eliminar usuario:", e)
            return False



# Instancia global
db = MySQLDatabase()
