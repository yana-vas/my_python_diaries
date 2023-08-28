from vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super(PassengerCar, self).__init__(brand, model, license_plate_number, max_milеage=450.00)

    def drive(self, mileage: float):
        percentage_use = (mileage*100)/self.max_milеage
        self.battery_level -= percentage_use
        self.battery_level = round(self.battery_level)

