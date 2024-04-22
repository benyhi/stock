    // Función para abrir la ventana agregar artículo
function abrirAgregar() {
    var ventanaAgregar = document.querySelector('.agregar_articulo');
    ventanaAgregar.style.display = "flex";
}

    // Función para cerrar la ventana agregar artículo
function cerrarAgregar() {
    var ventanaAgregar = document.querySelector('.agregar_articulo');
    ventanaAgregar.style.display = 'none';
}

// Función para abrir la ventana agregar artículo
function abrirBuscador() {
    var ventanaBuscar = document.querySelector('.buscar_articulo');
    ventanaBuscar.style.display = "flex";
}

// Función para cerrar la ventana agregar artículo
function cerrarBuscador() {
    var ventanaBuscar = document.querySelector('.buscar_articulo');
    ventanaBuscar.style.display = 'none';
}



// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Define el número de ítems por página
    var itemsPorPagina = 15;
    var currentPage = 1;

    // Función para mostrar los ítems correspondientes a la página actual
    function mostrarPagina(page) {
        var filas = document.getElementsByClassName("tabla_filas");

        // Calcula el rango de índices de los ítems a mostrar
        var startIndex = (page - 1) * itemsPorPagina;
        var endIndex = startIndex + itemsPorPagina;

        // Oculta todas las filas de la tabla
        for (var i = 0; i < filas.length; i++) {
            filas[i].style.display = "none";
        }

        // Muestra solo las filas correspondientes a la página actual
        for (var i = startIndex; i < endIndex && i < filas.length; i++) {
            filas[i].style.display = "";
        }
    }

    // Función para actualizar los controles de paginación
    function actualizarPaginacion() {
        var totalPaginas = Math.ceil(filas.length / itemsPorPagina);
        var paginasSpan = document.getElementById("paginas");
        paginasSpan.textContent = "Página " + currentPage + " de " + totalPaginas;
        document.getElementById("anterior").disabled = currentPage === 1;
        document.getElementById("siguiente").disabled = currentPage === totalPaginas;
    }

    // Obtener todas las filas de la tabla
    var filas = document.querySelectorAll(".tabla_filas");

    // Mostrar la primera página al cargar la página
    mostrarPagina(currentPage);
    actualizarPaginacion();

    // Evento de clic para el botón "Anterior"
    document.getElementById("anterior").addEventListener("click", function() {
        if (currentPage > 1) {
            currentPage--;
            mostrarPagina(currentPage);
            actualizarPaginacion();
        }
    });

    // Evento de clic para el botón "Siguiente"
    document.getElementById("siguiente").addEventListener("click", function() {
        var totalPaginas = Math.ceil(filas.length / itemsPorPagina);
        if (currentPage < totalPaginas) {
            currentPage++;
            mostrarPagina(currentPage);
            actualizarPaginacion();
        }
    });
});



function buscarArticulo(){
    var filasTabla = document.getElementsByClassName('tabla_filas');
    var codigo = document.getElementById('codigo_buscar').value.trim();
    var codigointerno = document.getElementById('codinterno_buscar').value.trim();
    var descripcion = document.getElementById('descrip_buscar').value.trim();

    if (codigo !== "" || codigointerno !== "" ||  descripcion !== ""){
        for(i = 0; i < filasTabla.length; i++) {
            var celdas = filasTabla[i].cells;
            var valorCodigo = celdas[0].textContent.trim();
            var valorCodigointerno = celdas[1].textContent.trim();
            var valorDescripcion = celdas[2].textContent.trim(); 
        
            if (valorCodigo.includes(codigo) || valorCodigointerno.includes(codigointerno) || valorDescripcion.includes(descripcion)){
                datosArticulo = filasTabla[i].textContent;
                console.log(datosArticulo)
            }
}
    }
        }
