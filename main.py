from cluster import Cluster
from node import Node
from pod import Pod
from scheduler import Scheduler
from traffic_generator import TrafficGenerator


def main():
    # Crear el cluster y los nodos
    cluster = Cluster()
    node1 = Node('Node1')
    node2 = Node('Node2')
    cluster.add_node(node1)
    cluster.add_node(node2)

    # Crear instancias (pods)
    instance1 = Pod('Instance1', 50, 100, 200)
    instance2 = Pod('Instance2', 30, 50, 100)
    instance3 = Pod('Instance3', 20, 80, 150)

    # Asignar instancias usando el Scheduler
    scheduler = Scheduler()
    for instance in [instance1, instance2, instance3]:
        node = scheduler.first_fit(cluster, instance)
        if node:
            print(f'Instance {instance.name} assigned to {node.name}')
        else:
            print(f'No node could accommodate instance {instance.name}')

    # Generador de Tráfico
    traffic_generator = TrafficGenerator(cluster)
    for _ in range(10):  # Simula 10 ciclos de tráfico
        traffic_generator.simulate_traffic()

    # Mostrar el estado final de las instancias
    print(cluster)

    pass


if __name__ == '__main__':
    main()
