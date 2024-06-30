class Logger:
    """
    Esta es la clase Logger que se utiliza para registrar el estado de la simulación.

    Atributos:
        logs (list): Una lista de registros de estado.

    Métodos:
        log_state(sim_time, cluster): Registra el estado actual de la simulación.
        get_logs(): Devuelve todos los registros de estado.
    """

    def __init__(self):
        """
        El constructor para la clase Logger.
        """
        self.logs = []

    def log_state(self, sim_time, cluster):
        """
        Registra el estado actual de la simulación.

        Parámetros:
            sim_time (int): El tiempo actual de la simulación.
            cluster (Cluster): El estado actual del cluster.
        """
        state = {
            "time": sim_time,
            "nodes": []
        }
        for node in cluster.nodes:
            node_state = {
                "name": node.name,
                "resources": {res_name: res.available for res_name, res in node.resources.items()},
                "instances": [
                    {
                        "name": pod.name,
                        "cpu_request": pod.cpu_request,
                        "ram_request": pod.ram_request,
                        "storage_request": pod.storage_request,
                        "traffic": pod.traffic,
                        "utility": pod.utility
                    } for pod in node.pods
                ]
            }

            state["nodes"].append(node_state)
        self.logs.append(state)

    def get_logs(self):
        """
        Crea todos los registros de estado.

        Devuelve:
            list: Una lista de todos los registros de estado.
        """
        return self.logs