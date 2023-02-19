from connection import connectDB

def traeTecnicos():
    conexion = connectDB()
    tecnicos = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT employees.nombres, employees.apellidos, departments.department, users.id "+
            "FROM users JOIN employees ON users.id_user = employees.id JOIN departments ON departments.id = employees.id_department")
        tecnicos = cursor.fetchall()
    conexion.close()
    return tecnicos