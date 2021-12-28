from django.shortcuts import render

# Create your views here.
def brochure(request):

    return render(request, "brochure/brochure.html")

def administracion(request):

    return render(request, "brochure/administracion.html")

def administracionplanes(request):

    return render(request, "brochure/administracion/planes.html")

def administracionfirma(request):

    return render(request, "brochure/administracion/firma_electronica.html")

def administracionEvaluacion(request):

    return render(request, "brochure/administracion/EvaluacionyDesempeno.html")

def administracionClimaorganizacional(request):

    return render(request, "brochure/administracion/Climaorganizacional.html")

def administracionSeleccionyCapacitacion(request):

    return render(request, "brochure/administracion/SeleccionyCapacitacion.html")








