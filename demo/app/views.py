from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hello world")

def puri(request):
    return HttpResponse("Puri meri jaan kyun khati hai")

def second(request):
    return HttpResponse("My second view!")
