from resource import Resource


class Node:
    """
    Esta es la clase Node que representa un nodo en un cluster.

    Atributos:
        name (str): El nombre del nodo.
        resources (dict): Un diccionario de recursos disponibles en el nodo.
        pods (list): Una lista de pods en el nodo.

    Métodos:
        can_allocate(pods): Verifica si el nodo puede asignar los recursos solicitados por un pod.
        allocate_pod(pods): Asigna los recursos solicitados por un pod al nodo.
        scale_pod(pod_name, cpu_increment, ram_increment, storage_increment): Escala los recursos de un pod en el nodo.
        downscale_pod(pod_name, cpu_decrement, ram_decrement, storage_decrement): Reduce la escala de los recursos de un pod en el nodo.
        remove_pod(pod_name): Elimina un pod del nodo.
        monitor_utility(): Monitorea la utilidad de los pods en el nodo y escala o desescala los recursos según sea necesario.
        __repr__(): Devuelve una representación de cadena del nodo.
        to_dict(): Devuelve una representación de diccionario del nodo.
    """

    def __init__(self, name):
        """
        El constructor para la clase Node.

        Parámetros:
            name (str): El nombre del nodo.
        """
        self.name = name
        self.resources = {
            'CPU': Resource('CPU', 100),
            'RAM': Resource('RAM', 200),
            'STORAGE': Resource('STORAGE', 500)
        }
        self.pods = []

    def can_allocate(self, pods):
        """
        Verifica si el nodo puede asignar los recursos solicitados por un pod.

        Parámetros:
            pods (Pod): El pod para el que se deben verificar los recursos.

        Devuelve:
            bool: Verdadero si el nodo puede asignar los recursos, Falso en caso contrario.
        """
        return (self.resources['CPU'].available >= pods.cpu_request and
                self.resources['RAM'].available >= pods.ram_request and
                self.resources['STORAGE'].available >= pods.storage_request)

    def allocate_pod(self, pods):
        """
        Asigna los recursos solicitados por un pod al nodo.

        Parámetros:
            pods (Pod): El pod para el que se deben asignar los recursos.

        Devuelve:
            bool: Verdadero si los recursos se asignaron con éxito, Falso en caso contrario.
        """
        if self.can_allocate(pods):
            self.resources['CPU'].allocate(pods.cpu_request)
            self.resources['RAM'].allocate(pods.ram_request)
            self.resources['STORAGE'].allocate(pods.storage_request)
            self.pods.append(pods)
            return True
        return False

    def scale_pod(self, pod_name, cpu_increment, ram_increment, storage_increment):
        """
        Escala los recursos de un pod en el nodo.

        Parámetros:
            pod_name (str): El nombre del pod a escalar.
            cpu_increment (int): El incremento de CPU para el pod.
            ram_increment (int): El incremento de RAM para el pod.
            storage_increment (int): El incremento de almacenamiento para el pod.

        Devuelve:
            bool: Verdadero si el pod se escaló con éxito, Falso en caso contrario.
        """
        for pod in self.pods:
            if pod.name == pod_name:
                if self.resources['CPU'].available >= cpu_increment and \
                        self.resources['RAM'].available >= ram_increment and \
                        self.resources['STORAGE'].available >= storage_increment:
                    self.resources['CPU'].allocate(cpu_increment)
                    self.resources['RAM'].allocate(ram_increment)
                    self.resources['STORAGE'].allocate(storage_increment)
                    pod.scale(cpu_increment, ram_increment, storage_increment)
                    pod.calculate_utility()
                    return True
        return False

    def downscale_pod(self, pod_name, cpu_decrement, ram_decrement, storage_decrement):
        for pod in self.pods:
            if pod.name == pod_name:
                pod.scale(-cpu_decrement, -ram_decrement, -storage_decrement)
                self.resources['CPU'].release(cpu_decrement)
                self.resources['RAM'].release(ram_decrement)
                self.resources['STORAGE'].release(storage_decrement)
                pod.calculate_utility()
                return True
        return False

    def remove_pod(self, pod_name):
        for pod in self.pods:
            if pod.name == pod_name:
                self.resources['CPU'].release(pod.cpu_request)
                self.resources['RAM'].release(pod.ram_request)
                self.resources['STORAGE'].release(pod.storage_request)
                self.pods.remove(pod)
                return True
        return False

    def monitor_utility(self):
        def monitor_utility(self):
            """
            Monitorea la utilidad de los pods en el nodo y escala o desescala los recursos según sea necesario.
            """
        for pod in self.pods:
            if pod.utility < 0.5:  # Umbral de utilidad bajo
                # Intentar desescalar si la utilidad es baja
                self.downscale_pod(pod.name, 10, 10, 10)
            elif pod.utility > 1.5:  # Umbral de utilidad alto
                # Intentar escalar si la utilidad es alta
                self.scale_pod(pod.name, 10, 10, 10)

    def __repr__(self):
        """
        Crea una representación de cadena del nodo.

        Devuelve:
            str: Una representación de cadena del nodo.
        """
        return (f'Node {self.name} - Resources: {self.resources} - '
                f'Pods: {self.pods}')

    def to_dict(self):
        """
        Crea una representación de diccionario del nodo.

        Devuelve:
            dict: Una representación de diccionario del nodo.
        """
        return {
            'name': self.name,
            'resources': {k: v.to_dict() for k, v in self.resources.items()},
            'pods': [pod.to_dict() for pod in self.pods]
        }
