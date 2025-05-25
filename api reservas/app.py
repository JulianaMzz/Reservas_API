from flask import Flask
from routes.reserva_route import reserva_bp
from database.db import init_db

app = Flask(__name__)
app.register_blueprint(reserva_bp)

init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)