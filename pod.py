class Pod:
    def __init__(self, name, cpu_request, ram_request, storage_request):
        self.name = name
        self.cpu_request = cpu_request
        self.ram_request = ram_request
        self.storage_request = storage_request
        self.traffic = 0  # Atributo para el tráfico de la instancia
        self.utility = 0  # Atributo para la utilidad de la instancia

    def scale(self, cpu_increment, ram_increment, storage_increment):
        self.cpu_request += cpu_increment
        self.ram_request += ram_increment
        self.storage_request += storage_increment

    def __repr__(self):
        return (f'Instance {self.name} - CPU: {self.cpu_request}, '
                f'RAM: {self.ram_request}, STORAGE: {self.storage_request}, '
                f'Utility: {self.utility}, Traffic: {self.traffic}')

    def calculate_utility(self):
        # Función de utilidad que considera el tráfico y los recursos asignados
        if self.cpu_request > 0 and self.ram_request > 0 and self.storage_request > 0:
            resource_factor = (self.cpu_request + self.ram_request + self.storage_request) / 3
            self.utility = self.traffic / resource_factor
        else:
            self.utility = 0

    def to_dict(self):
        return {
            'name': self.name,
            'cpu_request': self.cpu_request,
            'ram_request': self.ram_request,
            'storage_request': self.storage_request,
            'utility': self.utility,
            'traffic': self.traffic
        }
