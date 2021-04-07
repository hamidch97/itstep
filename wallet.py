class Wallet:
    def __init__(self, name, amount, currency_code):
        self.__name = name
        self.__amount = amount
        self.__currency_code = currency_code

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self):
        if isinstance(self.__amount, float):
            return self.__amount
        else:
            raise ValueError("amount must be integer")

    @amount.getter
    def amount(self):
        return self.__amount

    @amount.deleter
    def amount(self):
        del w.__amount

    @property
    def currency(self):
        return self.__currency_code

    @currency.setter
    def currency(self):
        code = ["UAH", "USD", "EUR"]
        if self.__currency_code in code:
            return self.__currency_code
        else:
            raise ValueError("currency code isn't valide")

    @currency.getter
    def currency(self):
        return self.__currency_code

    @currency.deleter
    def currency(self):
        del w.__currency_code


w = Wallet("hamid", 250, "uah")
print(w.amount)
