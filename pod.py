class Pod:
    def __init__(self, name, cpu_request, ram_request, storage_request):
        self.name = name
        self.cpu_request = cpu_request
        self.ram_request = ram_request
        self.storage_request = storage_request

    def __repr__(self):
        return (f'Instance {self.name} - CPU: {self.cpu_request}, '
                f'RAM: {self.ram_request}, STORAGE: {self.storage_request}')

