from S1E9 import Character


class Baratheon(Character):
    """ Representing the Baratheon family. """
    def __init__(self, first_name=None, is_alive=True, family_name = None, eyes = None, hairs = None ):
        """ the constructor the Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def __str__(self):
        """ User-friendly representation """
        return f"<bound method Baratheon.__str__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
    
    def __repr__(self):
        """  Devloper-friendly representation """
        return f"<bound method Baratheon.__repr__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
    
    def die(self):
        self.is_alive = False



class Lannister(Character):
    """ Represnting the Lannister family"""
    def __init__(self, first_name=None, is_alive=True, family_name = None, eyes = None, hairs = None):
        """  the constructor of the Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        """ change the state for the Lannister """
        self.is_alive = False


    def __str__(self):
        """ User-friendly representation """
        return f"<bound method Lannister.__str__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
    
    def __repr__(self):
        """  Devloper-friendly representation """
        return f"<bound method Lannister.__repr__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"
    

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ create new object"""
        return cls(first_name=first_name, is_alive=is_alive)
        