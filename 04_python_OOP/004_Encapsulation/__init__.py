class CreditCard:
    def __init__(self, number, exp_date, cvc, name, pin):
        self.number = number
        self.exp_date = exp_date
        self.cvc = cvc
        self.name = name
        self.__pin = pin

    def __is_pin_correct(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        if self.__is_pin_correct(old_pin):
            self.__pin = new_pin
            return
        raise ValueError("Old pin is not correct")


card = CreditCard(1234, '2022-10', 256, "Test Name", 7887)
card.change_pin(7887, 1234)
print(card._CreditCard__pin)