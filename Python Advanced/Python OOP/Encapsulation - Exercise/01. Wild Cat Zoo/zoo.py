class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif self.__budget - price < 0 and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
      try:
          worker = next(filter(lambda w: w.name == worker_name, self.workers))

      except StopIteration:
          return (f"There is no {worker_name} in the zoo")

      self.workers.remove(worker)
      return f"{worker_name} fired successfully"


    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if self.__budget - salaries < 0:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"


    def tend_animals(self):
        cost_animal = sum(a.money_for_care for a in self.animals)
        if self.__budget - cost_animal < 0:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= cost_animal

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"


    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(info['Lion'])} Lions:",
            * info['Lion'],
            f"----- {len(info['Tiger'])} Tigers:",
            * info['Tiger'],
            f"----- {len(info['Cheetah'])} Cheetahs:",
            * info['Cheetah']
        ]

        return "\n".join(result)

    def workers_status(self):

        info = {"Caretaker": [], "Vet": [], "Keeper": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet']
        ]

        return "\n".join(result)




