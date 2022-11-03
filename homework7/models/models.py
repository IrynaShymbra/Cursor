from logging import raiseExceptions
from framework.models import Model

class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Salon(Model):
    file = "salon.json"

    def __init__(self,name,location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, plant_id, salon_name = None):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        self.salon_name = salon_name
        
        if salon_name:
            self._check_salon_name()

    def _check_salon_name(self):
        salon = Salon.get_by_name(self.salon_name)
        if not salon:
            raise Exception('Salon doesnt find')

