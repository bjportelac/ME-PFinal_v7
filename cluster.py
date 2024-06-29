class Cluster:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def scale_horizontal(self, pod, count):
        for _ in range(count):
            for node in self.nodes:
                if node.allocate_pod(pod):
                    print(f'Scaled horizontally: {pod.name} to {node.name}')
                    break

    def downscale_horizontal(self, pod_name, count):
        for _ in range(count):
            for node in self.nodes:
                if node.remove_pod(pod_name):
                    print(f'Descaled horizontally: {pod_name} to {node.name}')
                    break

    def __repr__(self):
        return f'Cluster - Nodes: {self.nodes}'

