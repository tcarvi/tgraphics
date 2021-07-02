from enum import Enum

class EnumComandoDesenho(Enum):
    DeslocarEmX = 0
    DeslocarEmY = 1
    DeslocarEmZ = 2
    DeslocarEmXInclinado = 10
    DeslocarEmYInclinado = 11
    DeslocarEmZInclinado = 12
    DesenharRetanguloEmX = 20
    DesenharRetanguloEmY = 21
    DesenharRetanguloEmZ = 22
    DesenharRetanguloEmXInclinado = 30
    DesenharRetanguloEmYInclinado = 31
    DesenharRetanguloEmZInclinado = 32