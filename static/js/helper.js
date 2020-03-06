const $ = (i) => {
    return document.querySelector(i)
}
const $$ = (i) => {
    return document.querySelectorAll(i)
}
function save(key, value) {
    localStorage[key] = JSON.stringify(value);
}
function load(key, _default) {
    return localStorage.getItem(key) ? JSON.parse(localStorage[key]) : _default
}