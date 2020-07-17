from .models import Mascota, Persona, Adopcion
from .serializers import MascotaSerializer, PersonaSerializer, AdopcionSerializer


#  getMascotaSerializer: Retorna el serializador de una lista de mascotas. 
# filtro: Filtro aplicado al resultado del serializador.
#       None -> Devuelve la lista completa de mascotas.
#       valor -> Filtra por el valor indicado, la forma de buscar es la siguiente.
#               "estado='d'" -> Busca todoas las mascotas con estado disponible.
# retorna los datos serializados y filtrados.
def getMascotasSerializer(filtro):
    miSerializador = MascotaSerializer(__getObjeto(Mascota, filtro), many=True)
    return miSerializador.data


#  getMascotaByIdSerializer: Retorna el objeto mascota serializado.
# filtro: Filtro aplicado al resultado del serializador.
# retorna La mascota serializada.
def getMascotaByIdSerializer(pk):
    miMascota = Mascota.objects.get(id=pk)
    miSerializador = MascotaSerializer(miMascota, many=False)
    return miSerializador.data


#  getMascotaByStatusSerializer: Retorna el objeto mascota serializado.
# filtro: Filtro aplicado al resultado del serializador.
# retorna La mascota serializada.
def getMascotaByStatusSerializer(estado):
    todos = int('00001000',2)
    rescatados = int('00010000',2)
    disponibles = int('00100000',2)
    adoptados = int('01000000',2)
    total =(todos + rescatados + disponibles + adoptados)
    miOpcion = int(estado)
    if (total & miOpcion) == 0:
        # es un estado invalido, se devuelbe vacio.
        miSerializador = MascotaSerializer({},many=True )
        return miSerializador.data
    if (miOpcion & todos) >0:
        # Devolbiendo los perritos con cualquier estado.
        miSerializador = MascotaSerializer(__getObjeto(Mascota, None), many=True)
        return miSerializador.data
    # Procesar los distintos filtros y sus combinaciones.
    miFiltro = []
    if (rescatados & miOpcion) > 0:
        # perritos rescatados.
        miFiltro.append('r')
    if (disponibles & miOpcion) > 0:
        # perritos disponibles.
        miFiltro.append('d')
    if (adoptados & miOpcion) > 0:
        # perritos adoptados.
        miFiltro.append('a')
    miMascota = Mascota.objects.filter(estado__in=miFiltro)
    miSerializador = MascotaSerializer(miMascota,many=True )
    return miSerializador.data




#  getPersonasSerializer: Retorna el serializador de las personas.
# filtro: Filtro aplicado al resultado del serializador.
# retorna los datos serializados y filtrados.
def getPersonasSerializer(filtro):
    miSerializador = PersonaSerializer(__getObjeto(Persona, filtro), many=True)
    return miSerializador.data


#  getAdopcionesSerializer: Retorna el serializador de las adopciones.
# filtro: Filtro aplicado al resultado del serializador.
# retorna los datos serializados y filtrados.
def getAdopcionesSerializer(filtro):
    miSerializador = AdopcionSerializer(
        __getObjeto(Adopcion, filtro), many=True)
    return miSerializador.data


# __getObjeto: Obtiene los objetos solicitados con filtro si es necesario.
# RetornaUn queryset con los resultados.
def __getObjeto(miObjeto, filtro):
    if not filtro:
        misObjetos = miObjeto.objects.all()
    else:
        misObjetos = miObjeto.objects.filter(filtro)
    return misObjetos
