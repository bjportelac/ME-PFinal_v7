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
    pod1 = Pod('Instance1', 50, 100, 200)
    pod2 = Pod('Instance2', 30, 50, 100)
    pod3 = Pod('Instance3', 20, 80, 150)

    # Asignar instancias usando el Scheduler
    scheduler = Scheduler()
    for instance in [pod1, pod2, pod3]:
        node = scheduler.first_fit(cluster, instance)
        if node:
            print(f'Instance {instance.name} assigned to {node.name}')
        else:
            print(f'No node could accommodate instance {instance.name}')

    # Mostrar el estado final de las instancias
    print(cluster)

    pass


if __name__ == '__main__':
    main()
