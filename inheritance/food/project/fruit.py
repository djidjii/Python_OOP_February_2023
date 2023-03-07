from project.food import Food


class Fruit:
    def __int__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
