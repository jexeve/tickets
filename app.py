from flask import Flask, render_template, redirect, url_for, flash, request, session
import Controllers.user as user
from flask_session import Session
import Controllers.MenuController as menu
import Controllers.TecnicosController as tecnicos
import Controllers.TicketsController as ticketsTecnicos

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        flag = user.login(request.form["username"],request.form["password"])
        session["username"] = flag[0]
        session["id"] = flag[1]
        session["menus"] = menu.getMenu()
        if flag:
            return redirect('/tickets')
        else:
            return render_template('./auth/login.html')    
    else:
        return render_template('./auth/login.html')

@app.route('/tickets', methods=['GET'])
def tickets():
    tickets = ticketsTecnicos.getTicketsForMe( session["username"])
    data = {
            'tickets': {'data' : tickets, 'total': len(tickets) },
            'tecnicos': tecnicos.traeTecnicos()
        }
    return render_template('./tickets/index.html',data=data)

@app.route('/crea/ticket', methods=['POST'])
def creaTickets():
    ticketsTecnicos.create(request.form, session["id"])
    return redirect('/my/tickets')    

@app.route('/my/tickets', methods=['GET'])
def mytickets():
    data = {'tecnicos': tecnicos.traeTecnicos()}
    tickets = ticketsTecnicos.getTicketsByMe( session["id"] )
    data = {'tickets': {'data' : tickets, 'total': len(tickets) } }
    return render_template('./tickets/my.html',data=data)

@app.route('/ticket/<id>', methods=['GET'])
def verTicket(id):
    data = {'tecnicos': tecnicos.traeTecnicos()}
    ticket = ticketsTecnicos.getTicket(id)
    data = {'ticket': ticket}
    return render_template('./tickets/ticket.html', data=data)

@app.route('/logout', methods=['POST'])
def logout():
    session["username"] = None
    session["id"] = None
    session["menus"] = None
    return redirect('/login')

if __name__ == "__main__":
    app.run()