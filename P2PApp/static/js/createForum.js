var registerform = document.getElementById("reg_form");
registerform.addEventListener("submit", function(event) {
    event.preventDefault(); // previene que el formulario se envíe automáticamente

    // obtener los valores de los campos de entrada
    var descripcion = document.getElementById("descripcion").value;
    var description = document.getElementById("comentario").value;

    var data = {
        "name": descripcion,
        "comentario": description,
        "messages":[]
    };

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

    fetch('/create_forum/reg_forum/', {
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