/****
 * Archivo: sinConexion.js
 * Caso de uso: Redirige a la pagina de aviso de trabajo sin conexion.
 * Alumno: Daniel Garcia.
 * ---------------------------------------------------------------------------------
 ****/


/****
 * Preparando el contenedor de los perritos rescatados.
 ****/
window.onload = function() {
    if (navigator.onLine) {
        //console.log('Aqui estoy!');
    } else {
        window.location.replace("http://localhost:8000/sinConexion/");
    }
};