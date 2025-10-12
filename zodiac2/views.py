from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# crear una variable lista
zodiac = {
    "aries":       "Aries... próximamente",

    "tauro":       "Tauro... próximamente",

    "geminis":     "Géminis... próximamente",

    "cancer":      "Cáncer... próximamente",

    "leo":         "Leo... próximamente",

    "virgo":       "Virgo... próximamente",

    "libra":       "Libra... próximamente",

    "escorpio":    "Escorpio... próximamente",

    "sagitario":   "Sagitario... próximamente",

    "capricornio": "Capricornio... próximamente",

    "acuario":     "Acuario... próximamente",

    "piscis":      "Piscis... próximamente",

    "ofiuco":      "Ofiuco... próximamente",
}

# Create your views here.
# Crea una vista index que va a resibir una variable del navegador (cliente)
def index(request):
    # aquí voy a generar la lógica de todos los signos
    # Pasamos una lista que pueda verse del lado del cliente
    
    #list_items = ""


    """for signo in zodiac.keys():
        list_items += f"<h1>Signo: {signo + " Perrito"} </h1><br>"
        list_items += f"<p>{zodiac[signo]}</p><br>"
        """
    
    signos = list(zodiac.keys())


    #return HttpResponse(list_items)
    return render(request,'zodiac2/index.html', {
        "mensaje": "Hola desde view",
        "mensaje2": "Este es otro mensaje!!!",
        "signos": signos,
    })

def get_by_name(request, name):
    
    try:
        signo_text = zodiac[name]
        return render(
            request,
            'zodiac2/signo.html',
            {
                "signo": name,
                "signo_text": signo_text,
            }
        )
    except:
        return HttpResponseNotFound("No encontré el signo: "+name)