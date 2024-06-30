from cluster import Cluster
from node import Node
from pod import Pod
from report_generator import ReportGenerator
from scheduler import Scheduler
from simulation_manager import SimulationManager


def main():
    # Crear el cluster y los nodos
    # Se crea un objeto de la clase Cluster y tres objetos de la clase Node con los nombres 'Node1', 'Node2' y 'Node3'.
    # Los nodos se añaden al cluster.
    cluster = Cluster()
    node1 = Node('Node1')
    node2 = Node('Node2')
    node3 = Node('Node3')
    cluster.add_node(node1)
    cluster.add_node(node2)
    cluster.add_node(node3)

    # Crear instancias (pods)
    # Se crean cinco objetos de la clase Pod con diferentes recursos solicitados.
    # Estos objetos se almacenan en una lista.
    instances = [
        Pod('Instance1', 50, 100, 200),
        Pod('Instance2', 30, 50, 100),
        Pod('Instance3', 20, 80, 150),
        Pod('Instance4', 32, 64, 500),
        Pod('Instance5', 16, 32, 200)
    ]

    # Asignar instancias usando el Scheduler
    # Se crea un objeto de la clase Scheduler y un objeto de la clase SimulationManager con el cluster y las instancias.
    # Se utiliza el método assign_instances del SimulationManager para asignar las instancias a los nodos del cluster.
    scheduler = Scheduler()
    simulation_manager = SimulationManager(cluster, instances)
    simulation_manager.assign_instances(scheduler)

    # Configurar y ejecutar la simulación
    # Se ejecuta la simulación con una duración de 100 unidades de tiempo.
    # Los registros de la simulación se almacenan en la variable logs.
    logs = simulation_manager.run_simulation(duration=100)

    # Generar reportes
    # Se crea un objeto de la clase ReportGenerator con los registros de la simulación.
    # Se procesan los registros y se generan gráficos y un informe en formato PDF.
    report_generator = ReportGenerator(logs)
    report_generator.process_logs()
    report_generator.generate_plots()
    report_generator.generate_pdf()


if __name__ == '__main__':
    main()
