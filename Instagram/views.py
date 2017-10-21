from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'Crear_cuenta.html')

def suma(request):
    if request.method == 'GET':
        return render(reques, 'suma.html')
    else:
        numero1 = int(request.POST)
