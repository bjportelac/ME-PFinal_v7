class Logger:

    def __init__(self):
        self.logs = []

    def log_state(self, sim_time, cluster):
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
        return self.logs
