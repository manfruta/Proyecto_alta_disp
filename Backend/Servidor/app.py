from flask import Flask
import MySQLdb

app = Flask(__name__)

# Conecta a la base de datos
db = MySQLdb.connect(host="mysqldb", user="root", passwd="root", db="datab")

# Crea un cursor para ejecutar consultas SQL
cursor = db.cursor()


@app.route('/')
def index():
    return 'Bienvenido a mi aplicación Flask'

@app.route('/uf')
def show_users():
    # Ejecuta una consulta SQL para obtener todos los usuarios de la base de datos
    cursor.execute("SELECT * FROM uf")

    # Obtiene los resultados de la consulta
    results = cursor.fetchall()

    # Crea una cadena HTML para mostrar los resultados en la página web
    output = '<html><body><h1>Usuarios</h1><table><tr><th>ID</th><th>Nombre</th></tr>'
    for row in results:
        output += '<tr><td>' + str(row[0]) + '</td><td>' + row[1] + '</td></tr>'
    output += '</table></body></html>'

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
