from logger import Logger
from traffic_generator import TrafficGenerator


class Simulation:
    def __init__(self, cluster, duration):
        self.cluster = cluster
        self.duration = duration
        self.sim_time = 0
        self.logger = Logger()

    def run(self):
        traffic_generator = TrafficGenerator(self.cluster)
        while self.sim_time < self.duration:
            traffic_generator.simulate_traffic()
            self.logger.log_state(self.sim_time, self.cluster)
            self.sim_time += 1