from flask import jsonify, request
from models.reserva_model import inserir_reserva, listar_reserva

def criar_reserva():
    dados = request.get_json()
    id_turma = dados.get('id_turma')
    sala = dados.get('sala')
    data = dados.get('data')
    horario = dados.get('horario')
    
    if not all([id_turma, sala, data, horario]):
        return jsonify({'erro': 'Dados incompletos'}), 400
    
    inserir_reserva(id_turma, sala, data, horario)
    return jsonify({"mensagem": 'Reserva criada com sucesso'}), 201

def obter_reserva():
    reservas = listar_reserva()
    return jsonify([dict(r) for r in reservas])