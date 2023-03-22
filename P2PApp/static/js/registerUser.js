var registerform = document.getElementById("reg_form");
registerform.addEventListener("submit", function(event) {
    event.preventDefault(); // previene que el formulario se envíe automáticamente

    // obtener los valores de los campos de entrada
    var carne = document.getElementById("fcarne").value;
    var name = document.getElementById("fname").value;

    // crear el objeto JSON utilizando los valores de los campos de entrada
    var data = {
        "carne": carne,
        "name": name,
        "uid":uuidv4()
    };
    
    function uuidv4() { //Funcion que genera valor aleatorio para asignarlo como uid
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
          (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );
    }
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

    fetch('/register/guardar-json/', {
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


