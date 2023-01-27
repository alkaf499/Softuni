class Equipment:
    id = 1
    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()

        __class__.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
