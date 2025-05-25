from flask import Blueprint
from controllers.reserva_controller import criar_reserva, obter_reserva

reserva_bp = Blueprint('reserva_bp', __name__)

reserva_bp.route('/reserva', methods=['GET'])(obter_reserva)
reserva_bp.route('/reserva', methods=['POST'])(criar_reserva)