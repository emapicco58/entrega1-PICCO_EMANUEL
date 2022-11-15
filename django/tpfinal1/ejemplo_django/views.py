
from django.http import HttpResponse

def vista_saludo(request):
    
    return HttpResponse("Hola coders! :) ")



def vista_saludo(request):
    
    return HttpResponse("""<h1>Hola coders! :) </h1><p style='color:red' >Esto es una prueba</p>""")

def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y tu password por WhatsApp ;) ")


def dia_hoy(request):
    
    hoy=datetime.now()
    respuesta = f'hoy es {hoy}'
    return HttpResponse(respuesta)



def nacimiento(request, edad):
    
    hoy = datetime.now()n¿
    nacimiento = 
    hoy.year - int(edad)
    respuesta = f"Tu año de nacimiento es: {nacimiento}"
    return HttpResponse(respuesta)



