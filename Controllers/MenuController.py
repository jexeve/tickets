from connection import connectDB

def getMenu():
    conexion = connectDB()
    menus = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT menu, link FROM menus ORDER BY 'order' ASC")
        menus = cursor.fetchall()
    conexion.close()
    return menus