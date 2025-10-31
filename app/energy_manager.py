class EnergyManager:
    def __init__(self):
        self.battery_capacity = 10000  
        self.battery_level = 10000    

        self.rooms = {
            "sala": {"on": False, "consumo": 300},
            "cozinha": {"on": False, "consumo": 500},
            "banheiro": {"on": False, "consumo": 200},
            "quarto": {"on": False, "consumo": 400},
        }

    def toggle_room(self, room, state):
        if room in self.rooms:
            self.rooms[room]["on"] = state
            self.update_battery()

    def update_battery(self):
        total_consumo = sum(
            data["consumo"] for data in self.rooms.values() if data["on"]
        )
        self.battery_level -= total_consumo * 0.001  
        if self.battery_level < 0:
            self.battery_level = 0

    def get_status(self):
        return {
            "bateria_restante": round(self.battery_level, 2),
            "bateria_total": self.battery_capacity,
            "comodos": self.rooms,
        }
