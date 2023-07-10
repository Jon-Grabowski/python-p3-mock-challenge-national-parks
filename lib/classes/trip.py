from .national_park import NationalPark
from .visitor import Visitor
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    def set_visitor (self, visitor) :
        if isinstance(visitor, Visitor) :
            self._visitor = visitor
        else :
            raise Exception("not a Visitor class")
    
    def get_visitor (self):
        return self._visitor
    
    visitor = property(get_visitor, set_visitor)

    def set_national_park (self, national_park) :
        if isinstance(national_park, NationalPark) :
            self._national_park = national_park
        else :
            raise Exception("not a NationalPark class")
    
    def get_national_park (self):
        return self._national_park
    
    national_park = property(get_national_park, set_national_park)