from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.brochure, name="brochure"),
    path('planes', views.administracionplanes, name="planes"),
   path('firma', views.administracionfirma, name="firma_electronica"),
   path('Evaluacion', views.administracionEvaluacion, name="Evaluacion"),
   path('Climaorganizacional', views.administracionClimaorganizacional, name="Climaorganizacional"),
   path('SeleccionyCapacitacion', views.administracionSeleccionyCapacitacion, name="SeleccionyCapacitacion"),

]
