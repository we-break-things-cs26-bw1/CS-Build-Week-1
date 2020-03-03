//vars
let mode = "registration"

//helper functions 
const $ = (i) => {
    return document.querySelector(i)
}
const $$ = (i) => {
    return document.querySelectorAll(i)
}
//events 
window.onkeypress = (e) => {

    switch (e.key) {
        case "Enter":
            submit()
            break
        case " ":
            toggleScreens()
            break
    }
}

function toggleScreens() {
    mode = mode == "registration" ? "login" : "registration";
    $("#login").classList.toggle("show");
    $("#signup").classList.toggle("show");
}

function getData() {
    let data = {}
    let form = mode + "Field"

    for (child of $$(`.${form}`)) {
        data[child.name] = child.value
    }


    return data
}

function submit() {

    const data = getData()

    fetch(`http://127.0.0.1:8000/api/${mode}/`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFTOKEN": $("[name=csrfmiddlewaretoken]").value
        },
        body: JSON.stringify(data)
    }).then(r => r.json()).then(r => {
        localStorage["session"] = r.key;
    }).catch(err => {
        console.log(err);
    })
}