
class calculator:
    """ a calculator class that is able to do calculations (addition, multiplication, subtraction, division) of vector with a scalar."""
    #your code here
    def __init__(self, l = None):
        self.l = l

    
        
    def __add__(self, object) -> None:
        if self.l == None:
            raise("list is vide")
        for i, el in enumerate(self.l):
            self.l[i] += object
        print(self.l)


    def __mul__(self, object) -> None:
        if self.l == None:
            raise("list is vide")
        for i, el in enumerate(self.l):
            self.l[i] *= object
        print(self.l)


    def __sub__(self, object) -> None:
        if self.l == None:
            raise("the list is vide")
        for i, el in enumerate(self.l):
            self.l[i] -= object
        print(self.l)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise("the number how to divse is nul")
        if self.l == None:
            raise("the list is vide")
        for i, el in enumerate(self.l):
            self.l[i] /= object
        print(self.l)
    #your code here