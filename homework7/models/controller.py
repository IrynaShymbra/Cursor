from .models import Plant, Employee

class Controller:

    @classmethod
    def add_new_plant(cls, name, location):
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print(plant.id)
            print(plant.name)
            print(plant.location)


    @classmethod
    def get_plant_by_id(cls, id):
        plant = Plant.get_plant_by_id(id)
        print(plant.id)
        print(plant.name)
        print(plant.location)

    @classmethod
    def delete_plant_by_id(cls, id):
        Plant.delete(id)

    @classmethod
    def add_new_employee(cls, name, email, plant_id, salon = None):
        employee = Employee(name, email, plant_id, salon)
        employee.save()      


    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print(employee.id)
            print(employee.name)
            print(employee.email)

    @classmethod
    def get_employee_by_id(cls, id):
        employee = Employee.get_by_id(id)
        print(employee.id)
        print(employee.name)
        print(employee.email)


    @classmethod
    def delete_employee_by_id(cls, id):
        Employee.delete(id)
