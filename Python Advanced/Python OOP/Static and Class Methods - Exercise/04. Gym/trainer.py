class Trainer:
    id = 1
    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()

        __class__.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id


    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
