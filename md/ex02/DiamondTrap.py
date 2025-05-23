from S1E7 import Baratheon, Lannister



class King(Baratheon, Lannister):
    """ King uses multiple inheritance from Baratheon and Lannister."""

    def __init__(self, first_name=None, is_alive=True, family_name=None, eyes=None, hairs=None):
        "the constructor King"
        super().__init__(first_name, is_alive, family_name = "Baratheon", eyes = 'brown', hairs = 'dark')

    def set_first_name(self, new_first_name):
        """ change first name"""
        self.first_name = new_first_name

    def set_family_name(self, new_family_name):
        """ the change family name of the king"""
        self.family_name = new_family_name

    def set_eyes(self, eyes):
        """ change the eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """ change the hairs"""
        self.hairs = hairs

    def get_first_name(self):
        """ return first name"""
        return self.first_name

    def get_family_name(self, new_family_name):
        """ return family name of the king"""
        return self.family_name

    def get_eyes(self):
        """ return the eyes"""
        return self.eyes

    def get_hairs(self):
        """ return the hairs"""
        return self.hairs

    

