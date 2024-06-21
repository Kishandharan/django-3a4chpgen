from django.shortcuts import render
from random import choice, shuffle

def home(request):
	upper_lets = []
	lower_lets = []
	numbers = ["0","1","2","3","4","5","6","7","8","9"]
	for i in range(65, 90):
		upper_lets.append(chr(i))
	for i in range(97, 122):
		lower_lets.append(chr(i))
	rand1 = choice(upper_lets)
	rand2 = choice(lower_lets)
	rand3 = choice(numbers)
	result = list(rand1+rand2+rand3)
	shuffle(result)
	pwd = ""
	for i in result:
		pwd += i
	return render(request, "app1/index.html", {"param1":pwd})

