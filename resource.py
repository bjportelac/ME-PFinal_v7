class Resource:
    """
    Esta es la clase Resource que representa un recurso en un nodo.

    Atributos:
        name (str): El nombre del recurso.
        total (int): La cantidad total del recurso.
        available (int): La cantidad disponible del recurso.

    Métodos:
        allocate(amount): Asigna una cantidad del recurso.
        release(amount): Libera una cantidad del recurso.
        __repr__(): Devuelve una representación de cadena del recurso.
        to_dict(): Devuelve una representación de diccionario del recurso.
    """

    def __init__(self, name, total):
        """
        El constructor para la clase Resource.

        Parámetros:
            name (str): El nombre del recurso.
            total (int): La cantidad total del recurso.
        """
        self.name = name
        self.total = total
        self.available = total

    def allocate(self, amount):
        """
        Asigna una cantidad del recurso.

        Parámetros:
            amount (int): La cantidad del recurso a asignar.

        Devuelve:
            bool: Verdadero si el recurso se asignó con éxito, Falso en caso contrario.
        """
        if self.available >= amount:
            self.available -= amount
            return True
        return False

    def release(self, amount):
        """
        Libera una cantidad del recurso.

        Parámetros:
            amount (int): La cantidad del recurso a liberar.
        """
        self.available += amount

    def __repr__(self):
        """
        Crea una representación de cadena del recurso.

        Devuelve:
            str: Una representación de cadena del recurso.
        """
        return f'{self.name} - Total: {self.total}, Available: {self.available}'

    def to_dict(self):
        """
        Crea una representación de diccionario del recurso.

        Devuelve:
            dict: Una representación de diccionario del recurso.
        """
        return {
            'name': self.name,
            'total': self.total,
            'available': self.available
        }
