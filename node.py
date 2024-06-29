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

    def allocate_instance(self, pods):
        if self.can_allocate(pods):
            self.resources['CPU'].allocate(pods.cpu_request)
            self.resources['RAM'].allocate(pods.ram_request)
            self.resources['STORAGE'].allocate(pods.storage_request)
            self.pods.append(pods)
            return True
        return False

    def __repr__(self):
        return (f'Node {self.name} - Resources: {self.resources} - '
                f'Pods: {self.pods}')

