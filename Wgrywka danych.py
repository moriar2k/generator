# import requests
from winner_generator.models import Winner
# import random

# uruchamianie z manage.py shell za pomocą komendy exec(open('Wgrywka danych.py').read())



str_= '''Patrycja
Marcin
Robert
Damian 
Rafał
Antoni
Zbigniew
Adam'''

list_ = str_.splitlines()

for name in list_:
    Winner.objects.create(name=name)

