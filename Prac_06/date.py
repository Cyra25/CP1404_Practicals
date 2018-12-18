class Date:
    def __init__(self, day=0, month=0):
        self.day = day
        self.month = month

    def __str__(self):
        return "{}{}{}"
