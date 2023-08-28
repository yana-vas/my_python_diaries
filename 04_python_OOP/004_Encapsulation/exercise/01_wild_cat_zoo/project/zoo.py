from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > 0 and self.__budget >= price:
            self.animals.append(animal)
            self.__animal_capacity -= 1
            self.__budget -= price
            name = animal.name
            return f"{name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > 0 and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity -= 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = f'You have {len(self.animals)} animals\n'
        message += self.__build_str(self.animals, 'Lion')
        message += self.__build_str(self.animals, 'Tiger')
        message += self.__build_str(self.animals, 'Cheetah')
        return message.strip()

    def __build_str(self, entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'

        return f"----- {counter} {entity_type}s:\n" + result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_str(self.workers, 'Keeper')
        result += self.__build_str(self.workers, 'Caretaker')
        result += self.__build_str(self.workers, 'Vet')
        return result.strip()


