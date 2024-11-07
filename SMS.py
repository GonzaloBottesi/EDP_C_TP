from Aplicacion import Aplicacion
from Stack import Stack
class SMS (Aplicacion):
    def __init__(self, peso) -> None:
        super().__init__(peso)
        self.bandeja = Stack()
        
test = SMS('0 K')