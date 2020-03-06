
//events

function handleMovement(direction) {
    let dirMap = {
        n: "down",
        s: "up",
        e: "left",
        w: "right"
    }

    if (game.currentRoom[direction] in mapCache) {
        game.currentRoom = mapCache[game.currentRoom[direction]]
        shiftRooms(dirMap[direction], game.rooms)
        movePlayer(game.currentRoom.x, game.currentRoom.y)
        $("#roomCountNum").innerText = game.roomCount
    }
    else if (game.currentRoom[direction] != 0) {
        // makeRooms(2, game.currentRoom) //! remove after testing 

        fetch(`https://roomsgame.herokuapp.com/api/dungeon/${game.currentRoom[direction]}/`, {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(r => r.json()).then(res => {

            mapCache[res.uuid] = res
            game.currentRoom = res

            shiftRooms(dirMap[direction])
            movePlayer(game.currentRoom.x, game.currentRoom.y)

            game.roomCount += 1
            $("#roomCountNum").innerText = game.roomCount

            // save("rooms", mapCache)
            // save("playerRoom", game.currentRoom)

            console.log(game.currentRoom);

        })
    }




}
$$(".controller").forEach(i => {
    i.onclick = (e) => {
        let direction = e.currentTarget.attributes.direction.value;
        handleMovement(direction)
    }
})

window.onkeypress = (e) => {
    switch (e.key) {
        case "w":
            handleMovement("n")
            break
        case "a":
            handleMovement("w")
            break
        case "s":
            handleMovement("s")
            break
        case "d":
            handleMovement("e")
            break
    }
}


//?TEST

let template = {
    monsters: "",
    items: [],
    x: 0,
    y: 0,
    height: 100,
    width: 100,
    uuid: "start",
    background: "https://i.pinimg.com/originals/e8/78/48/e878488978e87c46dbc14896f3f9c4f4.jpg",

}

function randomName() {
    const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let name = ""
    for (let i = 0; i <= 20; i++) {
        name += letters[Math.floor(Math.random() * letters.length)]
    }
    return name
}

function randomColor() {
    let colors = ["#fb29fd", "#dd32b3", "#4216d2", "#2e3bf0", "#00cff8", "#790c9b", "#6ff845", "#046877", "#b1d7a5"]
    return colors[Math.floor(Math.random() * 5)]
}


function makeRooms(int, room, roomLog = {}) {
    if (int <= 0) {
        return null
    }
    roomLog[`${room.x}-${room.y}`] = room
    game.roomCount += 1

    if (!room.n) {
        let newRoom = { ...template }
        newRoom.uuid = randomName()
        newRoom.x = room.x
        newRoom.y = room.y - 100
        newRoom.background = randomColor()

        if (`${newRoom.x}-${newRoom.y}` in roomLog) {
            room.n = roomLog[`${newRoom.x}-${newRoom.y}`]
        } else {
            room.n = makeRooms(int - 1, newRoom, roomLog)
        }

    }
    if (!room.s) {
        let newRoom = { ...template }
        newRoom.uuid = randomName()
        newRoom.x = room.x
        newRoom.y = room.y + 100
        newRoom.background = randomColor()

        if (`${newRoom.x}-${newRoom.y}` in roomLog) {
            room.s = roomLog[`${newRoom.x}-${newRoom.y}`]
        } else {
            room.s = makeRooms(int - 1, newRoom, roomLog)
        }
    }
    if (!room.e) {
        let newRoom = { ...template }
        newRoom.uuid = randomName()
        newRoom.x = room.x + 100
        newRoom.y = room.y
        newRoom.background = randomColor()

        if (`${newRoom.x}-${newRoom.y}` in roomLog) {
            room.e = roomLog[`${newRoom.x}-${newRoom.y}`]
        } else {
            room.e = makeRooms(int - 1, newRoom, roomLog)
        }
    }
    if (!room.w) {
        let newRoom = { ...template }
        newRoom.uuid = randomName()
        newRoom.x = room.x - 100
        newRoom.y = room.y
        newRoom.background = randomColor()

        if (`${newRoom.x}-${newRoom.y}` in roomLog) {
            room.w = roomLog[`${newRoom.x}-${newRoom.y}`]
        } else {
            room.w = makeRooms(int - 1, newRoom, roomLog)
        }
    }

    return room
}

//!TESTING

//check if user is logged in 
if (!localStorage["session"]) {
    location = "../login"
}

//controller logic 
//load inital game rooms
game.rooms = load("rooms", null) || game.rooms
drawRooms()
setTimeout(() => {
    movePlayer(game.currentRoom.x, game.currentRoom.y)
}, 200)
$("#roomCountNum").innerText = game.roomCount


