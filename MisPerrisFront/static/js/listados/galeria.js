/****
 * Archivo: galeria.js
 * Caso de uso: Lista las imagenes de la galeria en la pagina de inicio.
 * Alumno: Daniel Garcia.
 * ---------------------------------------------------------------------------------
 ****/


/****
 * Preparando el contenedor de los perritos de la galeria.
 ****/
$(document).ready(function() {
    ejecutarFiltro();
});


/****
 * Preparando el contenedor de los perritos rescatados.
 ****/
$("#filtrar").click(function() {
    ejecutarFiltro();
});


/***
 * Ejecuta el filtro seleccionado.
 ****/
function ejecutarFiltro() {
    miFiltro = $("#id_estado").val();
    var miUrl = miServidor + 'mascotaByStatus/' + miFiltro;
    cargarDatos(miUrl, true);
};


/****
 * Funcion para cargar los elementos desde la api de mascotas.
 ****/
function cargarDatos(miUrl, listarTodo) {
    $.ajax({
        url: miUrl,
        type: "GET",
        dataType: "json",
        crossDomain: true,
        success: function(resultados) {
            (listarTodo ? listarMascotas(resultados, 'rescatadas') : detalleMascota(resultados))
        }
    });
};



/****
 * Funcion para cargar los perritos en la galeria.
 ****/
function listarMascotas(datos) {
    $("#contenedorGaleria").empty()
        // Verificando que existan perritos para listar.
    if (datos.length == 0) {
        $("#contenedorGaleria").append('<p>No hay perritos disponibles.</p>');
        return;
    }
    // listar los perritos disponibles.
    $.each(datos, function(i, items) {
        cargarImagen(datos[i]);
    });
};


/****
 *  Carga la imagen en la galeria.
 ****/
function cargarImagen(mascota) {
    var texto = mascota.nombre + ' es de raza ' + mascota.raza + ', ';
    texto += mascota.descripcion + '.';
    $("#contenedorGaleria").append('<img src="' + mascota.ruta_imagen + '" title="' + texto + '">');
};