from connection import connectDB

def login(username, password):
    conexion = connectDB()
    user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT username, id FROM users WHERE username = %s and password = %s", (username, password))
        user = cursor.fetchone()
    conexion.close()
    return user