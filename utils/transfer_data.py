import re


class TransferData:
    def __init__(self, date, description, to_whom, moneys, currency):
        self.moneys = moneys
        self.date = date
        self.description = description
        self.to_whom = to_whom
        self.currency = currency

    def data_date_and_description(self):
        """
        Получение данных по дате и описанию операции.
        """
        return f"{'-'.join(reversed(self.date[:10].split('-')))} {self.description}"

    def data_from_whom(self, from_whom):
        """
        Получение данных по отправителю.
        """
        if len(from_whom.split()[-1]) == 20:
            encrypted_card_20 = re.sub(r"(\d{4})\d{12}(\d{4})",
                                       fr"\1 {from_whom.split()[-1][5:7]}** **** **** \2",
                                       from_whom.split()[-1])
            return f"{' '.join(from_whom.split(' ')[:-1])} {encrypted_card_20}"
        else:
            encrypted_card_16 = re.sub(r'(\d{4})\d{8}(\d{4})', fr"\1 {from_whom.split()[-1][5:7]}** **** \2",
                                       from_whom.split()[-1])
            return f"{' '.join(from_whom.split(' ')[:-1])} {encrypted_card_16}"

    def data_to_whom(self):
        """
        Получение данных по получателю.
        """
        return f'{self.to_whom.split()[0]} **{self.to_whom.split()[1][-4:]}'

    def data_moneys(self):
        """
        Получение данных по переведённым средствам.
        """
        return f'{self.moneys} {self.currency}'
