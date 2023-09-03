from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        for c in self.customers:
            if c.name == customer.name:
                return

        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for t in self.trainers:
            if t.name == trainer.name:
                return

        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for e in self.equipment:
            if e.name == equipment.name:
                return

        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        for p in self.plans:
            if p.trainer_id == plan.trainer_id and plan.equipment_id == p.equipment_id and plan.duration == p.duration:
                return

        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        for s in self.subscriptions:
            if subscription.trainer_id == s.trainer_id and subscription.exercise_id == s.exercise_id and subscription.customer_id == s.customer_id:
                return

        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        message = []

        for s in self.subscriptions:
            message.append(str(s))

        for c in self.customers:
            message.append(str(c))

        for t in self.trainers:
            message.append(str(t))

        for e in self.equipment:
            message.append(str(e))

        for p in self.plans:
            message.append(str(p))

        return '\n'.join(message)

