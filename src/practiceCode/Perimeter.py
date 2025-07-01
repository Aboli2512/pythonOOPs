from src.practiceCode import Area
import math
class Perimeter(Area): #imprting area in perimeter

    def CalculayePerimeter(self):
        match self.shape:
            case 'circle':
                return 2 * math.pi * self.side1
            case 'Square':
                return 4*self.side1
            case 'Rectangle':
                return 2*(self.side1 + self.side2)
            case _:
                pass


