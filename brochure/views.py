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




def finanzas(request):

    return render(request, "brochure/finanzas.html")

def finanzasCuenta(request):

    return render(request, "brochure/finanzas/Cuenta_a_pagar.html")

def finanzasCobrar(request):

    return render(request, "brochure/finanzas/Cuentas_por_cobrar.html")

def finanzasfacturacion(request):

    return render(request, "brochure/finanzas/facturacion.html")

def finanzasReportes_faltantes(request):

    return render(request, "brochure/finanzas/Reportes_faltantes.html")




def logistica(request):

    return render(request, "brochure/logistica.html")

def logisticaBodega(request):

    return render(request, "brochure/logistica/Bodegas.html")

def logisticaInventarios(request):

    return render(request, "brochure/logistica/Inventarios.html")


def logisticaRepuestos(request):

     return render(request, "brochure/logistica/Repuestos.html")


def logisticaSolicitudes_por_pedido(request):

     return render(request, "brochure/logistica/Solicitudes_por_pedido.html")




def comercial(request):

    return render(request, "brochure/comercial.html")

def comercialCotizaciones(request):

    return render(request, "brochure/comercial/Cotizaciones.html")

def comercialCMR(request):

    return render(request, "brochure/comercial/CMR.html")

def comercialprospección_de_Clientes(request):

    return render(request, "brochure/comercial/prospección_de_Clientes.html")

def comercialFidelizacion_y_Post_Venta(request):

    return render(request, "brochure/comercial/Fidelizacion_y_Post_Venta.html")





def proyectos(request):

    return render(request, "brochure/proyectos.html")

def proyectosControl_de_tiempos_y_costos(request):

    return render(request, "brochure/proyectos/Control_de_tiempos_y_costos.html")


def proyectosControl_documentario(request):

    return render(request, "brochure/proyectos/Control_documentario.html")


def proyectosGestion_de_riesgo(request):

    return render(request, "brochure/proyectos/Gestion_de_riesgo.html")


def proyectosGestion_de_valor_ganado(request):

    return render(request, "brochure/proyectos/Gestion_de_valor_ganado.html")


def proyectosPlanificación_de_poryectos(request):

    return render(request, "brochure/proyectos/Planificación_de_poryectos.html")


def proyectosTareas_de_personal(request):

    return render(request, "brochure/proyectos/Tareas_de_personal.html")


def seguridad(request):

    return render(request, "brochure/seguridad.html")


def seguridadHabilitacion_de_personal(request):

    return render(request, "brochure/seguridad/Habilitacion_de_personal.html")


def seguridadInspecciones(request):

    return render(request, "brochure/seguridad/Inspecciones.html")

def seguridadProcedimientos(request):

    return render(request, "brochure/seguridad/Procedimientos.html")


