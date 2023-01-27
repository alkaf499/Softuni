import calendar

class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
        #all of them should be numbers = day.month.year
    def from_date(cls, id, name, date: str, age_restriction):
        day, month, year = [int(x)for x in date.split('.')]

        return cls(name, id, year, calendar.month_name[month], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
