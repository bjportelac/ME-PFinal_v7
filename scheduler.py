class Scheduler:
    @staticmethod
    def first_fit(cluster, instance):
        for node in cluster.nodes:
            if node.allocate_instance(instance):
                return node
        return None
