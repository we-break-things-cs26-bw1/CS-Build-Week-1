let game = {}
game.rooms =
{
    "uuid": 67,
    "title": "DEFAULT TITLE",
    "description": "DEFAULT DESCRIPTION",
    "monster": "DEFAULT MONSTER",
    "item": "DEFAULT ITEM",
    "x": 700,
    "y": 700,
    "height": 100,
    "width": 100,
    "background": "https://i.pinimg.com/originals/da/03/3f/da033f75aa259d59b315f673aa09de43.jpg",
    "n": 72,
    "s": 0,
    "e": 68,
    "w": 66,
    "n_to": 0,
    "s_to": 0,
    "e_to": 0,
    "w_to": 0
}
game.currentRoom = load("playerRoom", game.rooms)
game.roomCount = 0

let imageMap = {}
let mapCache = load("rooms", { 1: game.rooms })

const player = new Image()
player.src = "https://images.squarespace-cdn.com/content/v1/54fe412ce4b0c449f7369857/1437363122613-EDWK0D04HGPAKL5L46ZV/ke17ZwdGBToddI8pDm48kEBpwcrGAoNLHXdW84KG_NhZw-zPPgdn4jUwVcJE1ZvWEtT5uBSRWt4vQZAgTJucoTqqXjS3CfNDSuuf31e0tVHJnvQYQxmBKUVePszzXYD3tjiXlSQo6BhJ-c33jKf9Nt1lH3P2bFZvTItROhWrBJ0/image-asset.png"

const gameboard = $("#gameboard")
const gameCtx = gameboard.getContext("2d")

gameboard.height = window.innerHeight
gameboard.width = window.innerWidth

function getXY(x, y, height, width) {
    const centerX = gameboard.width / 2
    const centerY = gameboard.height / 2

    x = ((centerX + x) - (width / 2)) - 700
    y = ((centerY + y) - (height / 2)) - 700

    return [x, y]
}

function clearBoard() {
    gameCtx.clearRect(0, 0, gameboard.width, gameboard.height);
}

function drawRoom(room) {

    const [x, y] = getXY(room.x, room.y, room.height, room.width)

    // if (room.background.startsWith("http")) {
    //     if (room.uuid in imageMap) {
    //         gameCtx.drawImage(imageMap[room.uuid], x, y, room.width, room.height);
    //     } else {
    //         let bg = new Image()
    //         bg.src = room.background
    //         bg.onload = _ => {
    //             gameCtx.drawImage(bg, x, y, room.width, room.height);
    //             imageMap[room.uuid] = bg;
    //             movePlayer(game.currentRoom.x, game.currentRoom.y)
    //         }
    //     }
    // } else {
    gameCtx.fillStyle = room.background;
    gameCtx.fillRect(x, y, room.width, room.height);
    // }

}

function drawRooms() {

    clearBoard();
    for (key in mapCache) {
        let room = mapCache[key]
        drawRoom(room)
    }

}

function movePlayer(x, y) {
    let playerHeight = 70;
    let playerWidth = 40;
    [x, y] = getXY(x, y, playerHeight, playerWidth)

    if (player.complete) {
        gameCtx.drawImage(player, x, y, playerWidth, playerHeight);
    } else {
        player.onload = () => {
            gameCtx.drawImage(player, x, y, playerWidth, playerHeight);
        }
    }

}

function shiftRooms(direction) {

    for (key in mapCache) {
        let room = mapCache[key]

        switch (direction) {
            case "up":
                room.y -= room.height
                break
            case "down":
                room.y += room.height
                break
            case "left":
                room.x -= room.width
                break
            case "right":
                room.x += room.width
                break
        }

    }

    drawRooms()
}

