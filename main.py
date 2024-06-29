from cluster import Cluster
from node import Node
from pod import Pod
from scheduler import Scheduler


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

    # Escalamiento Horizontal
    cluster.scale_horizontal(Pod('Instance4', 20, 40, 50), 2)

    # Escalamiento Vertical
    node1.scale_pod('Instance1', 10, 20, 30)

    # Mostrar el estado final de las instancias
    print(cluster)

    pass


if __name__ == '__main__':
    main()
