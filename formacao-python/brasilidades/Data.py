from datetime import datetime, timedelta


class Data:

    def __init__(self, momento=datetime.today()):
        self._momento_cadastro = momento

    def __str__(self):
        return self.format_data()

    def format_data(self):
        return self._momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastro(self):
        return datetime.today() - self._momento_cadastro
