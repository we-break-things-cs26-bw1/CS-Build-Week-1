const $ = (i) => {
    return document.querySelector(i)
}
const $$ = (i) => {
    return document.querySelectorAll(i)
}

let game = {}
game.rooms =
{
    monsters: "",
    items: [],
    x: 0,
    y: 0,
    height: 100,
    width: 100,
    uuid: "start",
    background: "https://files.slack.com/files-pri/T4JUEB3ME-FUJ7WV4V7/fall_background.jpg",
    n: null,
    s: null,
    e: null,
    w: null
}
game.currentRoom = game.rooms
game.roomCount = 0

const player = new Image()
player.src = "https://images.squarespace-cdn.com/content/v1/54fe412ce4b0c449f7369857/1437363122613-EDWK0D04HGPAKL5L46ZV/ke17ZwdGBToddI8pDm48kEBpwcrGAoNLHXdW84KG_NhZw-zPPgdn4jUwVcJE1ZvWEtT5uBSRWt4vQZAgTJucoTqqXjS3CfNDSuuf31e0tVHJnvQYQxmBKUVePszzXYD3tjiXlSQo6BhJ-c33jKf9Nt1lH3P2bFZvTItROhWrBJ0/image-asset.png"

const gameboard = $("#gameboard")
const gameCtx = gameboard.getContext("2d")

gameboard.height = window.innerHeight
gameboard.width = window.innerWidth

function getXY(x, y, height, width) {
    const centerX = gameboard.width / 2
    const centerY = gameboard.height / 2

    x = (centerX + x) - (width / 2)
    y = (centerY + y) - (height / 2)

    return [x, y]
}

function clearBoard() {
    gameCtx.clearRect(0, 0, gameboard.width, gameboard.height);
}

function drawRoom(room) {
    const [x, y] = getXY(room.x, room.y, room.height, room.width)

    gameCtx.fillStyle = room.background;
    gameCtx.fillRect(x, y, room.width, room.height);
}

function drawRooms(room, tracked = {}, cleared = false) {
    if (!room) return
    if (room.uuid in tracked) return
    //room is outside the bounds of the board
    // const buffer = 600
    // if (room.x < -(gameboard.width / 2) - buffer || room.y < -(gameboard.height / 2) - buffer) return
    // if (room.x > (gameboard.width / 2) + buffer || room.y > (gameboard.height / 2) + buffer) return

    if (!cleared) {
        clearBoard();
        cleared = true
    }
    tracked[room.uuid] = true

    if (room.n) drawRooms(room.n, tracked, cleared)
    if (room.s) drawRooms(room.s, tracked, cleared)
    if (room.e) drawRooms(room.e, tracked, cleared)
    if (room.w) drawRooms(room.w, tracked, cleared)

    drawRoom(room)
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

function shiftRooms(direction, room, roomTracker = {}) {
    if (!room) return
    if (room.uuid in roomTracker) return
    roomTracker[room.uuid] = true

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

    shiftRooms(direction, room.n, roomTracker)
    shiftRooms(direction, room.s, roomTracker)
    shiftRooms(direction, room.e, roomTracker)
    shiftRooms(direction, room.w, roomTracker)

    drawRooms(game.rooms)
}

