class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

        __class__.id += 1

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours*60)

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
