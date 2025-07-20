from datetime import datetime


class Player:
    def __init__(self, player_id, name, number, position, dob, performance_score=0.0):
        self.player_id = player_id
        self.name = name
        self.number = number
        self.position = position
        self.dob = dob
        self.performance_score = performance_score

    def update_performance(self, score):
        self.performance_score = score

    def get_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
