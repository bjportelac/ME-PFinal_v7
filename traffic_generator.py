import random


class TrafficGenerator:
    def __init__(self, cluster):
        self.cluster = cluster

    def simulate_traffic(self):
        # Simula el tráfico aumentando o disminuyendo la carga aleatoriamente
        for node in self.cluster.nodes:
            for pod in node.pods:
                cpu_load = random.randint(-10, 20)
                ram_load = random.randint(-20, 40)
                storage_load = random.randint(-50, 100)

                # Ajusta la carga en la instancia
                pod.cpu_request = max(0, pod.cpu_request + cpu_load)
                pod.ram_request = max(0, pod.ram_request + ram_load)
                pod.storage_request = max(0, pod.storage_request + storage_load)

                # Verifica los umbrales y escala o desescala según sea necesario
                if pod.cpu_request > node.resources['CPU'].total * 0.8:
                    node.scale_pod(pod.name, 10, 0, 0)
                elif pod.cpu_request < node.resources['CPU'].total * 0.2:
                    node.downscale_pod(pod.name, 10, 0, 0)

                if pod.ram_request > node.resources['RAM'].total * 0.8:
                    node.scale_pod(pod.name, 0, 20, 0)
                elif pod.ram_request < node.resources['RAM'].total * 0.2:
                    node.downscale_pod(pod.name, 0, 20, 0)

                if pod.storage_request > node.resources['STORAGE'].total * 0.2:
                    node.scale_pod(pod.name, 0, 0, 50)
                elif pod.storage_request < node.resources['STORAGE'].total * 0.8:
                    node.downscale_pod(pod.name, 0, 0, 50)
