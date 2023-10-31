class CalorieCount:
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def onTrack(self):
        if self.daily_intake <= self.daily_limit:
            return True
        else:
            return False

    def getProteinPercentage(self):
        return 4*self.protein/self.daily_intake

    def addMeal(self, cal: int, pro: int, car: int, fat: int):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat