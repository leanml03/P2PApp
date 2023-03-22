var registerform = document.getElementById("reg_form");
registerform.addEventListener("submit", function(event) {
    event.preventDefault(); // previene que el formulario se envíe automáticamente

    // obtener los valores de los campos de entrada
    var name = document.getElementById("name").value;
    var token = document.getElementById("token").value;

    // crear el objeto JSON utilizando los valores de los campos de entrada
    var data = {
        "name": name,
        "token": token,
    };

    // imprimir el objeto JSON en la consola para verificar que se ha creado correctamente
    ///console.log(data);

    // agregar el token CSRF al encabezado de la solicitud POST
    //var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    //var csrftoken = getCookie('csrftoken');

    console.log(data);
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    fetch('/create_course/reg_course/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log('Datos guardados en el archivo.');
            
        } else {
            console.log('Ocurrió un error al guardar los datos.');
        }
    });
});


