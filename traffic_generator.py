import random


class TrafficGenerator:
    """
    Esta es la clase TrafficGenerator que se utiliza para simular el tráfico en un cluster.

    Atributos:
        cluster (Cluster): El cluster en el que se simula el tráfico.

    Métodos:
        simulate_traffic(): Simula el tráfico en el cluster.
    """

    def __init__(self, cluster):
        """
        El constructor para la clase TrafficGenerator.

        Parámetros:
            cluster (Cluster): El cluster en el que se simula el tráfico.
        """
        self.cluster = cluster

    def simulate_traffic(self):
        """
        Simula el tráfico en el cluster.

        Este método simula el tráfico en el cluster aumentando o disminuyendo la carga de los pods de manera aleatoria.
        """
        for node in self.cluster.nodes:
            for pod in node.pods:
                cpu_load = random.randint(-5, 15)
                ram_load = random.randint(-2, 10)
                storage_load = int(random.expovariate(25))
                traffic_load = random.expovariate(100)  # Simula el tráfico

                # Ajusta la carga y el tráfico en la instancia
                pod.cpu_request = max(0, pod.cpu_request + cpu_load)
                pod.ram_request = max(0, pod.ram_request + ram_load)
                pod.storage_request = max(0, pod.storage_request + storage_load)
                pod.traffic = traffic_load

                # Recalcula la utilidad de la instancia
                pod.calculate_utility()

            node.monitor_utility()

                # Verifica los umbrales y escala o desescala según sea necesario
                #if pod.cpu_request > node.resources['CPU'].total * 0.8:
                #    node.scale_pod(pod.name, 10, 0, 0)
                #elif pod.cpu_request < node.resources['CPU'].total * 0.2:
                #    node.downscale_pod(pod.name, 10, 0, 0)

                #if pod.ram_request > node.resources['RAM'].total * 0.8:
                #    node.scale_pod(pod.name, 0, 20, 0)
                #elif pod.ram_request < node.resources['RAM'].total * 0.2:
                #    node.downscale_pod(pod.name, 0, 20, 0)

                #if pod.storage_request > node.resources['STORAGE'].total * 0.8:
                #    node.scale_pod(pod.name, 0, 0, 50)
                #elif pod.storage_request < node.resources['STORAGE'].total * 0.2:
                #    node.downscale_pod(pod.name, 0, 0, 50)

