/****
 * Archivo: listados.js
 * Caso de uso: Provee las funciones comunes para los listados de mascotas.
 * Alumno: Daniel Garcia.
 * ---------------------------------------------------------------------------------
 ****/


 /****
 * Funcion para cargar los perritos.
 ****/
function listarMascotas(datos, tipo) {
    titulo('#contenedorForm', 'Lista de mascotas '+ tipo + '.');
    // Verificando que existan perritos para listar.
    if (datos.length == 0) {
        $("#contenedorForm").append('<p>No hay perritos ingresados.</p>');
        return;
    }
    // listar los perritos disponibles.
    $.each(datos, function(i, items) {
        var idFila = 'fila_' + datos[i].id + datos[i].nombre;
        var idItem = 'item_' + datos[i].id + datos[i].nombre;
        $("#contenedorForm").append('<div id="' + idFila + '" class="contenedor-fila-lista">');
        idFila = '#' + idFila;
        $(idFila).append('<div id="' + idItem + '" class="contenedor-item-lista">');
        idItem = '#' + idItem;
        cargarImagen(idItem, datos[i]);
        cargarTextos(idItem, datos[i]);
        $(idFila).append('</div>');
        cargarBotones(idFila, datos[i]);
        $("#contenedorForm").append('</div>');
    });
};


/****
 * Titulos de los listados.
 ****/
function titulo(elemento, titulo) {
    $(elemento).empty();
    $(elemento).append('<h1>' + titulo + '</h1>');
    $(elemento).append('<hr>');
};


/****
 * Funcion para cargar la imagen del perrito.
 ****/
function cargarImagen(elemento, mascota) {
    $(elemento).append('<img src="' + mascota.ruta_imagen + '" alt="' + mascota.nombre + '">');
};


/****
 * Funcion que carga el texto de la informacion de los perritos.
 ****/
function cargarTextos(elemento, mascota) {
    var texto = 'Nombre: ' + mascota.nombre + '<br>';
    texto += 'Raza: ' + mascota.raza + '<br>';
    if (mascota.estado == 'r') texto += 'Estado: Rescatado<br>';
    if (mascota.estado == 'd') texto += 'Estado: Disponible<br>';
    if (mascota.estado == 'a') texto += 'Estado: Adoptado<br>';
    texto += 'Descripción: ' + mascota.descripcion + '<br>';
    $(elemento).append('<p>' + texto + '</p>');
};



/****
 *  Funcion para cargar el boton de visualizacion del perrito.
 ****/
function cargarBotones(elemento, mascota) {
    $(elemento).append('<button id="btn' + mascota.id + '" onclick="mostrarMascota(' + mascota.id + ')">Ver</button>')
};


/****
 *  Funcion para mostrar la informacion del perrito seleccionado.
 * Esta funcion es solicitada por el evento onClick de un boton.
 ****/
function mostrarMascota(id) {
    cargarDatos(miServidor + 'mascotaById/' + id, false);
};


/****
 *  Mostrando el detalle de la mascota.
 * Esta funcion es solicitada en la llamada de ajax.
 ****/
function detalleMascota(mascota) {
    $("#contenedorForm").hide();
    $("#contenedorMascota").show();
    titulo('#contenedorMascota', 'Información de mascota.');
    $("#contenedorMascota").append('<img src="' + mascota.ruta_imagen + '" alt="' + mascota.nombre + '">');
    var texto = mascota.nombre + ' es de raza ' + mascota.raza + ',<br>';
    texto += mascota.descripcion + '<br>';
    $('#contenedorMascota').append('<p class="datos-mascota">' + texto + '</p>');
    $("#contenedorMascota").append('<button onclick="volverListado()">Volver al listado de mascotas</button>')
};


/****
 * Funcion para volver a mostrar la lista de perritos.
 * Saliendo del modo mostrar detalle de mascota.
 ****/
function volverListado() {
    $("#contenedorMascota").hide();
    $("#contenedorForm").show();
};