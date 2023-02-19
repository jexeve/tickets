from connection import connectDB

def store(id_ticket, id_user, comment):
    conexion = connectDB()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO comments(id_ticket, id_user, comment) VALUES (%s, %s, %s)",
                       (int(id_ticket), int(id_user), comment)
        )
    conexion.commit()
    conexion.close()
    
def get(id_ticket):
    conexion = connectDB()
    comentarios = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT "+
        "employees.nombres,  "+
        "employees.apellidos,  "+
        "comments.`comment`,  "+
        "comments.created_at "+
        "FROM "+
        "comments "+
        "INNER JOIN "+
        "users "+
        "ON  "+
		"comments.id_user = users.id "+
	    "INNER JOIN "+
	    "employees "+
	    "ON  "+
		"users.id_user = employees.id "+
        "WHERE "+
	    "comments.id_ticket = %s ORDER BY created_at DESC", (int(id_ticket))
        )
        comentarios = cursor.fetchall()
    conexion.close()
    return comentarios