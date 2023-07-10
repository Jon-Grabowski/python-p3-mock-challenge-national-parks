class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    def get_name(self):
        return self._name
    def set_name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str):
                self._name = name
            else:
                raise Exception("Please enter valid name")
        else:
            raise Exception("Name can't be changed.")
    name = property(get_name, set_name)
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self and isinstance(trip, Trip)]
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        visitor_list = [trip.visitor for trip in self.trips() if isinstance(trip.visitor, Visitor)]
        self._visitors = visitor_list
        return list(set(visitor_list))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        from classes.visitor import Visitor
        most_trips = 0
        top_visitor = Visitor
        for visitor in self.visitors() :
            count = 0
            for trips in visitor.trips() :
                if trips.national_park == self :
                    count += 1
            if most_trips < count :
                most_trips = count
                top_visitor = visitor
        return top_visitor
