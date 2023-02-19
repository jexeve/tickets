from connection import connectDB

def getTicketsForMe(id):
    conexion = connectDB()
    tickets = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT "+
            "tickets.title, tickets.detail," +
            "tickets.created_at, "+
            "tickets.`status`, tickets.id "+
            "FROM "+
            "tickets "+
            "INNER JOIN "+
            "users "+
            "ON "+
		    "tickets.id_assigned = users.id "+
            "WHERE "+
            "users.id = %s",(int(id))
        )
        tickets = cursor.fetchall()
    conexion.close()
    return tickets

def getTicketsByMe(id):
    conexion = connectDB()
    tickets = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT "+
            "tickets.title, tickets.detail," +
            "tickets.created_at, "+
            "tickets.`status`, tickets.id "+
            "FROM "+
            "tickets "+
            "INNER JOIN "+
            "users "+
            "ON "+
            "tickets.id_creator = users.id "+
            "WHERE "+
            "tickets.id_creator = %s",(int(id))
        )
    tickets = cursor.fetchall()
    conexion.close()
    return tickets

def store(title, creator, assigned, detail):
    conexion = connectDB()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tickets(title, detail, id_creator, id_assigned, created_at, updated_at, status) VALUES (%s, %s, %s, %s, now(), now(),'P')",
                       (title, detail, int(creator), int(assigned))
        )
    conexion.commit()
    conexion.close()

def getTicket(id):
    conexion = connectDB()
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT "+
            "tickets.title, tickets.detail, "+
            "tickets.created_at, "+
            "tickets.`status`, tickets.id, "+
            "tickets.id, "+
            "employees.nombres, "+
            "employees.apellidos "+
            "FROM "+
            "tickets "+
            "INNER JOIN "+
            "users "+
            "ON "+
            "tickets.id_creator = users.id "+
            "INNER JOIN "+
	        "employees "+
	        "ON "+
		    "users.id_user = employees.id "+
            "WHERE "+
            "tickets.id = %s",(int(id))
        )
    ticket = cursor.fetchone()
    conexion.close()
    return ticket


def create(form, creator_id):
    title = form["titulo"]
    creator = creator_id
    assigned = form["responsable"]
    detail = form["detalles"]
    store(title,creator,assigned,detail)
