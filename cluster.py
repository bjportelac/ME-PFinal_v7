class Cluster:
    """
    Esta es la clase Cluster que representa un conjunto de nodos.

    Atributos:
        nodes (list): Una lista de nodos en el cluster.

    Métodos:
        add_node(node): Añade un nodo al cluster.
        scale_horizontal(pod, count): Escala horizontalmente un pod en el cluster.
        downscale_horizontal(pod_name, count): Reduce la escala horizontal de un pod en el cluster.
        __repr__(): Devuelve una representación de cadena del cluster.
        to_dict(): Devuelve una representación de diccionario del cluster.
    """

    def __init__(self):
        """
        El constructor para la clase Cluster.
        """
        self.nodes = []

    def add_node(self, node):
        """
        Añade un nodo al cluster.

        Parámetros:
            node (Node): El nodo a añadir.
        """
        self.nodes.append(node)

    def scale_horizontal(self, pod, count):
        """
        Escala horizontalmente un pod en el cluster.

        Parámetros:
            pod (Pod): El pod a escalar.
            count (int): El número de pods a añadir.
        """
        for _ in range(count):
            for node in self.nodes:
                if node.allocate_pod(pod):
                    print(f'Scaled horizontally: {pod.name} to {node.name}')
                    break

    def downscale_horizontal(self, pod_name, count):
        """
        Reduce la escala horizontal de un pod en el cluster.

        Parámetros:
            pod_name (str): El nombre del pod a reducir.
            count (int): El número de pods a eliminar.
        """
        for _ in range(count):
            for node in self.nodes:
                if node.remove_pod(pod_name):
                    print(f'Descaled horizontally: {pod_name} to {node.name}')
                    break

    def __repr__(self):
        """
        Crea una representación de cadena del cluster.

        Devuelve:
            str: Una representación de cadena del cluster.
        """
        return f'Cluster - Nodes: {self.nodes}'

    def to_dict(self):
        """
        Crea una representación de diccionario del cluster.

        Devuelve:
            dict: Una representación de diccionario del cluster.
        """
        return {
            'nodes': [node.to_dict() for node in self.nodes]
        }