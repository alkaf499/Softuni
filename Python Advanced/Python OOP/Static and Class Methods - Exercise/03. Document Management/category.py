class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __str__(self):
        return f"Category {self.id}: {self.name}"
