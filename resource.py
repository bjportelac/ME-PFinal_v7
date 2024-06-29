class Resource:
    def __init__(self, name, total):
        self.name = name
        self.total = total
        self.available = total

    def allocate(self, amount):
        if self.available >= amount:
            self.available -= amount
            return True
        return False

    def release(self, amount):
        self.available += amount

    def __repr__(self):
        return f'{self.name} - Total: {self.total}, Available: {self.available}'

    def to_dict(self):
        return {
            'name': self.name,
            'total': self.total,
            'available': self.available
        }
