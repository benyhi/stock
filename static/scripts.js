$(document).ready(function() {
    $('#tabla').DataTable();
  });


function abrirAgregar(){
  $('.contenedor_agregar').css({
    'display': 'flex'
  })
}

function cerrarAgregar(){
  $('.contenedor_agregar').css({
    'display': 'none'
  })
}


function abrirEditar(){
  $('a[id^="editar-"]').click(function(event){
    $('.contenedor_editar').css({
      'display':'flex'
    })
  })
}

function cerrarEditar(){
  $('.contenedor_editar').css({
    'display': 'none'
  })
}
