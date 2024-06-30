class Pod:
    """
        Esta es la clase Pod que representa una instancia de pod en un nodo.

        Atributos:
            name (str): El nombre del pod.
            cpu_request (int): La cantidad de CPU solicitada por el pod.
            ram_request (int): La cantidad de RAM solicitada por el pod.
            storage_request (int): La cantidad de almacenamiento solicitada por el pod.
            traffic (int): El tráfico de la instancia.
            utility (float): La utilidad de la instancia.

        Métodos:
            scale(cpu_increment, ram_increment, storage_increment): Escala los recursos solicitados por el pod.
            __repr__(): Devuelve una representación de cadena del pod.
            calculate_utility(): Calcula la utilidad del pod.
            to_dict(): Devuelve una representación de diccionario del pod.
        """

    def __init__(self, name, cpu_request, ram_request, storage_request):
        """
        El constructor para la clase Pod.

        Parámetros:
            name (str): El nombre del pod.
            cpu_request (int): La cantidad de CPU solicitada por el pod.
            ram_request (int): La cantidad de RAM solicitada por el pod.
            storage_request (int): La cantidad de almacenamiento solicitada por el pod.
        """
        self.name = name
        self.cpu_request = cpu_request
        self.ram_request = ram_request
        self.storage_request = storage_request
        self.traffic = 0  # Atributo para el tráfico de la instancia
        self.utility = 0  # Atributo para la utilidad de la instancia

    def scale(self, cpu_increment, ram_increment, storage_increment):
        """
        Escala los recursos solicitados por el pod.

        Parámetros:
            cpu_increment (int): El incremento de CPU para el pod.
            ram_increment (int): El incremento de RAM para el pod.
            storage_increment (int): El incremento de almacenamiento para el pod.
        """
        self.cpu_request += cpu_increment
        self.ram_request += ram_increment
        self.storage_request += storage_increment

    def __repr__(self):
        """
        Devuelve una representación de cadena del pod.

        Devuelve:
            str: Una representación de cadena del pod.
        """
        return (f'Instance {self.name} - CPU: {self.cpu_request}, '
                f'RAM: {self.ram_request}, STORAGE: {self.storage_request}, '
                f'Utility: {self.utility}, Traffic: {self.traffic}')

    def calculate_utility(self):
        """
        Calcula la utilidad del pod.

        La utilidad se calcula como el tráfico dividido por el factor de recursos, que es el promedio de los recursos solicitados.
        """
        # Función de utilidad que considera el tráfico y los recursos asignados
        if self.cpu_request > 0 and self.ram_request > 0 and self.storage_request > 0:
            resource_factor = (self.cpu_request + self.ram_request + self.storage_request) / 3
            self.utility = self.traffic / resource_factor
        else:
            self.utility = 0.5

    def to_dict(self):
        """
        Devuelve una representación de diccionario del pod.

        Devuelve:
            dict: Una representación de diccionario del pod.
        """
        return {
            'name': self.name,
            'cpu_request': self.cpu_request,
            'ram_request': self.ram_request,
            'storage_request': self.storage_request,
            'utility': self.utility,
            'traffic': self.traffic
        }
