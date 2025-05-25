from database.db import get_db_connection

def inserir_reserva(id_turma, sala, data, horario):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservas (id_turma, sala, data, horario)
        VALUES (?, ?, ?, ?)
        ''', (id_turma, sala, data, horario))
    conn.commit()
    conn.close()
    
def listar_reserva():
    conn = get_db_connection()
    cursor = conn.cursor()
    reservas = cursor.execute ('SELECT * FROM reservas').fetchall()
    conn.close()
    return reservas