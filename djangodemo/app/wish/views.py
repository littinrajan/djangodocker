from django.shortcuts import render
from django.http import HttpResponse
import random

# hello world view
def helloworld(request):
    return HttpResponse("Hello World..")

# wish view
def wishme(request):
    wishlist = ["Have a wonderful life", "All the best for your future", "Be awesome.."]
    return HttpResponse(str(random.choice(wishlist)))

# funfact view
def funfact(request):
    funist = ["Can you touch your tounge to your elbow?", "I swear..you cannot lick your nose...", "Bees sometimes sting other bees.."]
    return HttpResponse(str(random.choice(funist)))
    
    
