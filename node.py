from resource import Resource


class Node:
    def __init__(self, name):
        self.name = name
        self.resources = {
            'CPU': Resource('CPU', 100),
            'RAM': Resource('RAM', 200),
            'STORAGE': Resource('STORAGE', 500)
        }
        self.pods = []

    def can_allocate(self, pods):
        return (self.resources['CPU'].available >= pods.cpu_request and
                self.resources['RAM'].available >= pods.ram_request and
                self.resources['STORAGE'].available >= pods.storage_request)

    def allocate_pod(self, pods):
        if self.can_allocate(pods):
            self.resources['CPU'].allocate(pods.cpu_request)
            self.resources['RAM'].allocate(pods.ram_request)
            self.resources['STORAGE'].allocate(pods.storage_request)
            self.pods.append(pods)
            return True
        return False

    def scale_pod(self, instance_name, cpu_increment, ram_increment, storage_increment):
        for instance in self.pods:
            if instance.name == instance_name:
                if self.resources['CPU'].available >= cpu_increment and \
                        self.resources['RAM'].available >= ram_increment and \
                        self.resources['STORAGE'].available >= storage_increment:
                    self.resources['CPU'].allocate(cpu_increment)
                    self.resources['RAM'].allocate(ram_increment)
                    self.resources['STORAGE'].allocate(storage_increment)
                    instance.scale(cpu_increment, ram_increment, storage_increment)
                    return True
        return False

    def __repr__(self):
        return (f'Node {self.name} - Resources: {self.resources} - '
                f'Pods: {self.pods}')

