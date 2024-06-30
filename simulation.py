from logger import Logger
from traffic_generator import TrafficGenerator


class Simulation:
    """
    Esta es la clase Simulation que se utiliza para simular el tráfico en un cluster.

    Atributos:
        cluster (Cluster): El cluster en el que se simula el tráfico.
        duration (int): La duración de la simulación.
        sim_time (int): El tiempo actual de la simulación.
        logger (Logger): El logger que se utiliza para registrar el estado de la simulación.

    Métodos:
        run(): Ejecuta la simulación.
    """

    def __init__(self, cluster, duration):
        """
        El constructor para la clase Simulation.

        Parámetros:
            cluster (Cluster): El cluster en el que se simula el tráfico.
            duration (int): La duración de la simulación.
        """
        self.cluster = cluster
        self.duration = duration
        self.sim_time = 0
        self.logger = Logger()

    def run(self):
        """
        Ejecuta la simulación.

        Este método simula el tráfico en el cluster y registra el estado de la simulación a intervalos regulares.
        """
        traffic_generator = TrafficGenerator(self.cluster)
        while self.sim_time < self.duration:
            traffic_generator.simulate_traffic()
            self.logger.log_state(self.sim_time, self.cluster)
            self.sim_time += 1
