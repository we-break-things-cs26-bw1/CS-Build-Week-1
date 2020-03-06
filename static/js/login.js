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

function errorMessage(obj) {
    let v = Object.values(obj)
    let message = v.reduce((acc, val) => {
        return acc + val.join(" | ")
    }, "")

    $("#error").innerHTML = `<p>${message}</p>`
    $("#error").style.height = "50px"

    setTimeout(() => {
        $("#error").style.height = "0";
    }, 5000)
}


function submit() {

    const data = getData()

    fetch(`https://roomsgame.herokuapp.com/api/${mode}/`, {
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
        console.log(r);

        if ("key" in r) {
            localStorage["session"] = r.key;
            location = "../"
        } else {
            errorMessage(r)
        }


    }).catch(err => {
        console.log(err);
    })
}