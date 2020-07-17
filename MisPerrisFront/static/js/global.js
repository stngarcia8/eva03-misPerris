/****
 * Archivo: global.js.js
 * Caso de uso: Contiene funciones y variables globales de Mis Perris.
 * Alumno: Daniel Garcia.
 * ---------------------------------------------------------------------------------
 ****/


/****
 *  Variable que contiene la direccion del servidor donde consumir los datos.
 ****/
var miServidor = 'http://localhost:8001/api/v1/';


/****
 *  Definiendo los valores para los filtros.
 ****/
var todos = 8;
var rescatados = 16;
var disponibles = 32;
var adoptados = 64;


/****
 *  manejador  de  errores que las llamadas a la funcion .ajax pueda causar.
 ****/
$.ajaxSetup({
    error: function(jqXHR, textStatus, errorThrown) {
        if (jqXHR.status === 0) {
            cadenaError = 'El servidor no esta conectado, verifique la red.';
        } else if (jqXHR.status == 404) {
            cadenaError = 'La página solicitada no existe [404]';
        } else if (jqXHR.status == 500) {
            cadenaError = 'Error interno del servidor [500].';
        } else if (textStatus === 'parsererror') {
            cadenaError = 'Falló la coneversión del archivo json solicitado..';
        } else if (textStatus === 'timeout') {
            cadenaError = 'Tiempo de espera excedido.';
        } else if (textStatus === 'abort') {
            cadenaError = 'Petición Ajax fue cancelada.';
        } else {
            cadenaError = 'Error desconocido: ' + jqXHR.responseText;
        }
        $("#contenedorForm").empty();
        $("#contenedorForm").append('<h1>Error al cargar los datos.</h1>');
        $("#contenedorForm").append('<hr>');
        $("#contenedorForm").append('<p>Ha ocurrido el siguiente error al intentar cargar las mascotas [' + cadenaError + '], intente nuevamente o avise al administrador de Mis Perris.<br>Gracias!</p>');
    }

});