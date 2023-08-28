from user import User
from vehicles.base_vehicle import BaseVehicle
from vehicles.cargo_van import CargoVan
from vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users  = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            new_vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == "CargoVan":
            new_vehicle = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        new_route = Route(start_point, end_point, length)
        new_route.route_id = len(self.routes) + 1
        self.routes.append(new_route)
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        mileage = 0
        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                mileage = route.length

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                if is_accident_happened:
                    user.decrease_rating()
                else:
                    user.increase_rating()

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                if vehicle.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                vehicle.drive(mileage)
                if is_accident_happened:
                    vehicle.is_damaged = True
                return str(vehicle)











# from route import Route
# from user import User
# from vehicles.cargo_van import CargoVan
# from vehicles.passenger_car import PassengerCar
#
#
# class ManagingApp:
#     def __init__(self):
#         self.users = []  # all users (objects) that are created
#         self.vehicles = []  # all vehicles (objects) that are created
#         self.routes = []  # all routes (objects) that are created
#
#     def register_user(self, first_name: str, last_name: str, driving_license_number: str):
#         for user in self.users:
#             if user.driving_license_number == driving_license_number:
#                 return f"{driving_license_number} has already been registered to our platform."
#
#         new_user = User(first_name, last_name, driving_license_number)
#         self.users.append(new_user)
#         return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
#
#     def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
#         if vehicle_type != "PassengerCar" and vehicle_type != "CargoVan":
#             return f"Vehicle type {vehicle_type} is inaccessible."
#
#         for vehicle in self.vehicles:
#             if vehicle.license_plate_number == license_plate_number:
#                 return f"{license_plate_number} belongs to another vehicle."
#
#         if vehicle_type == "PassengerCar":
#             new_vehicle = PassengerCar(brand, model, license_plate_number)
#         elif vehicle_type == "CargoVan":
#             new_vehicle = CargoVan(brand, model, license_plate_number)
#         self.vehicles.append(new_vehicle)
#         return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
#
#     def allow_route(self, start_point: str, end_point: str, length: float):
#         for route in self.routes:
#             if route.start_point == start_point and route.end_point == end_point and route.length == length:
#                 return f"{start_point}/{end_point} - {length} km had already been added to our platform."
#             elif route.start_point == start_point and route.end_point == end_point and route.length < length:
#                 return f"{start_point}/{end_point} shorter route had already been added to our platform."
#             elif route.start_point == start_point and route.end_point == end_point and route.length > length:
#                 route.is_locked = True
#
#         new_route = Route(start_point, end_point, length, len(self.routes) + 1)
#         self.routes.append(new_route)
#         return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
#
#     def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
#                   is_accident_happened: bool):
#         mileage = 0
#         for route in self.routes:
#             if route.route_id == route_id:
#                 if route.is_locked:
#                     return f"Route {route_id} is locked! This trip is not allowed."
#                 mileage = route.length
#
#         for user in self.users:
#             if user.driving_license_number == driving_license_number:
#                 if user.is_blocked:
#                     return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
#                 if is_accident_happened:
#                     user.decrease_rating()
#                 else:
#                     user.increase_rating()
#
#         for vehicle in self.vehicles:
#             if vehicle.license_plate_number == license_plate_number:
#                 if vehicle.is_damaged:
#                     return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
#                 vehicle.drive(mileage)
#                 if is_accident_happened:
#                     vehicle.is_damaged = True
#                 return str(vehicle)
#
#     def repair_vehicles(self, count: int):
#         # damaged_vehicles = []
#         # for vehicle in self.vehicles:
#         #     if vehicle.is_damaged:
#         #         damaged_vehicles.append(vehicle)
#         count_of_repaired_vehicles = 0
#         for i in range(count):
#             for v in self.vehicles:
#                 if v.is_damaged:
#                     v.is_damaged = False
#                     v.battery_level = 100
#                     count_of_repaired_vehicles += 1
#         return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"
#
#     def users_report(self):
#         users_rating = {}
#         for user in self.users:
#             users_rating[user.rating] = user
#         sort_values = dict(sorted(users_rating.items(),key=lambda item:item[0]))
#         result = f"*** E-Drive-Rent ***\n"
#         for user_rating in users_rating:
#             user = users_rating[user_rating]
#             result += str(user) + f"\n"
#         return result
#
#
#
#
#
#
#
#
#
