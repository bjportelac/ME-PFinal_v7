class Cluster:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return f'Cluster - Nodes: {self.nodes}'

