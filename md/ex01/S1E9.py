from abc import ABC, abstractclassmethod

class Character(ABC):

    """ character an abstract class which can take a first_name as first parameter,
        is_alive as second non mandatory parameter set to True by default and can change the
        health state of the character with a method that passes is_alive from True to False
    """
    def __init__(self, first_name = None, is_alive = True):
        """the Constructor of the character"""
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractclassmethod
    def die(self):
        pass
        



class Stark(Character):
    """ Stack class inhirt from character """
    def __init__(self, first_name=None, is_alive=True):
        """ the constructor of the stack """
        super().__init__(first_name, is_alive)
    
    def die(self):
        """ the method for change the state the character """
        self.is_alive = False

