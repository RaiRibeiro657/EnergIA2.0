from flask import jsonify, request
from app import app
from app.energy_manager import EnergyManager

manager = EnergyManager()

@app.route("/status", methods=["GET"])
def get_status():
    manager.update_battery()
    return jsonify(manager.get_status())

@app.route("/toggle", methods=["POST"])
def toggle_device():
    data = request.get_json()
    room = data.get("room")
    state = data.get("state")
    if room and state is not None:
        manager.toggle_room(room, state)
        return jsonify({"message": f"{room} atualizado com sucesso"}), 200
    return jsonify({"error": "Dados inválidos"}), 400
