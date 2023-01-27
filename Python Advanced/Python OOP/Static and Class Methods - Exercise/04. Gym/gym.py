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
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if sub.customer_id == c.id][0]
        trainer = [t for t in self.trainers if sub.trainer_id == t.id][0]
        plan = [e for e in self.plans if trainer.id == e.trainer_id][0]
        equipment = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]
        result = '\n'.join([
            f"{str(sub)}",
            f"{str(customer)}",
            f"{str(trainer)}",
            f"{str(equipment)}",
            f"{str(plan)}",

        ])

        return result
