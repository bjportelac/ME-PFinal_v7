from simulation import Simulation


class SimulationManager:
    """
    Esta es la clase SimulationManager que se utiliza para administrar las simulaciones en un cluster.

    Atributos:
        cluster (Cluster): El cluster en el que se ejecutan las simulaciones.
        instances (list): La lista de instancias que se deben asignar en el cluster.

    Métodos:
        assign_instances(scheduler): Asigna las instancias a los nodos en el cluster utilizando un programador.
        run_simulation(duration): Ejecuta una simulación en el cluster durante una duración especificada.
    """

    def __init__(self, cluster, instances):
        """
        El constructor para la clase SimulationManager.

        Parámetros:
            cluster (Cluster): El cluster en el que se ejecutan las simulaciones.
            instances (list): La lista de instancias que se deben asignar en el cluster.
        """
        self.cluster = cluster
        self.instances = instances

    def assign_instances(self, scheduler):
        """
        Asigna las instancias a los nodos en el cluster utilizando un programador.

        Este método recorre cada instancia y utiliza el programador para asignar la instancia a un nodo en el cluster.

        Parámetros:
            scheduler (Scheduler): El programador que se utiliza para asignar las instancias.
        """
        for instance in self.instances:
            node = scheduler.first_fit(self.cluster, instance)
            if node:
                print(f'Instance {instance.name} assigned to {node.name}')
            else:
                print(f'No node could accommodate instance {instance.name}')

    def run_simulation(self, duration):
        """
        Ejecuta una simulación en el cluster durante una duración especificada.

        Este método crea una nueva simulación y la ejecuta durante la duración especificada.

        Parámetros:
            duration (int): La duración de la simulación.

        Devuelve:
            list: Los registros de la simulación.
        """
        simulation = Simulation(self.cluster, duration=duration)
        simulation.run()
        return simulation.logger.get_logs()
