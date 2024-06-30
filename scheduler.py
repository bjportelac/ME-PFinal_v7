class Scheduler:
    """
    Esta es la clase Scheduler que se utiliza para asignar pods a nodos en un cluster.

    Métodos:
        first_fit(cluster, instance): Asigna un pod a un nodo utilizando el algoritmo de ajuste primero.
    """

    @staticmethod
    def first_fit(cluster, instance):
        """
        Asigna un pod a un nodo utilizando el algoritmo de ajuste primero.

        Este método recorre cada nodo en el cluster y asigna el pod al primer nodo que tiene suficientes recursos disponibles.

        Parámetros:
            cluster (Cluster): El cluster en el que se deben asignar los pods.
            instance (Pod): El pod que se debe asignar.

        Devuelve:
            Node: El nodo al que se asignó el pod, o None si no se pudo asignar el pod a ningún nodo.
        """
        for node in cluster.nodes:
            if node.allocate_pod(instance):
                return node
        return None
