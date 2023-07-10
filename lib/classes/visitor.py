class Visitor:
    name_lock = True

    def __init__(self, name):      
        self.name = name

    def get_name(self):
        return self._name
    def set_name(self, name):
        if self.name_lock:
            if isinstance(name, str) and 1 <= len(name) <= 15:
                self._name = name
                self.name_lock = False
            else:
                raise Exception("Please enter valid name")
        else:
            raise Exception("Name can't be changed.")
    name = property(get_name, set_name)  


    def trips(self, new_trip=None):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self and isinstance(trip, Trip)]
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        park_list = [trip.national_park for trip in self.trips() if isinstance(trip.national_park, NationalPark)]
        filter_list = set(park_list)
        return list(filter_list)
