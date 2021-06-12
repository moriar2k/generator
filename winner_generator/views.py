import random
from django.shortcuts import render
from winner_generator.models import Winner

# Create your views here.
def home(request):
	return render(
		request,
		'home.html',
		{}
		)

def losuj(request):
	lista = Winner.objects.all()
	winner = random.choice(lista)
	return render(
		request,
		'winner.html',
		{'winner': winner}
		)