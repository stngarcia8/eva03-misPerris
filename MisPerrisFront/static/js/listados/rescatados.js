/****
 * Archivo: rescatados.js
 * Caso de uso: Lista de perritos rescatados.
 * Alumno: Daniel Garcia.
 * ---------------------------------------------------------------------------------
 ****/



/****
 * Preparando el contenedor de los perritos rescatados.
 ****/
$(document).ready(function() {
    $("#contenedorForm").show();
    $("#contenedorMascota").hide();
    miFiltro= rescatados + disponibles;
    var miUrl = miServidor + 'mascotaByStatus/' + miFiltro;
    cargarDatos(miUrl, true);
});


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


