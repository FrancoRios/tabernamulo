$("#formulario1").validate({

    rules: {
           "txt_nombre": {
            required: true
           
        },
        "txt_correo": {
            required: true,
            email: true
        },
        "txt_telefono": {
            required: true,
            minlength: 8
        },
        "txt_celular": {
            required: true,
            minlength: 9
        },
        "txt_mensaje": {
            required: true,
            maxlength: 150
        }
        
        
    },
    messages: {
        "txt_nombre": {
            required: "Por favor introduzca su nombre"
        },
        "txt_correo": {
            required: 'Ingrese correo',
            email: 'No cumple formato'
        },
        "txt_telefono": {
            required: 'Ingrese teléfono',
            minlength: 'Min. 8 caract'
        },
        "txt_celular": {
            required: 'Ingrese celular',
            minlength: 'Min. 9 caract'
        },
        "txt_mensaje": {
            required: 'Ingrese mensaje',
            maxlength: 'Max. 150 caract'
        }

    }
    
});


