// canvas

const canvas = document.getElementById("pixel-canvas");
const ctx = canvas.getContext("2d");
const palette = document.getElementById("palette");

const GRID_SIZE = 100;
const CELL_SIZE = canvas.width / GRID_SIZE;
let scale = 1;
let offsetX = 0;
let offsetY = 0;

const pixelData = Array.from({length: GRID_SIZE}, () => Array(GRID_SIZE).fill(null));

canvas.width = 500;
canvas.height = 500;

let currentColor = "#000000";

// Подключение
const WS_URL = `ws://${window.location.host}/ws/canvas/0/`;
const SOCKET = new WebSocket(WS_URL);
// Получение обновлений через WebSocket
SOCKET.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.canvasState) {
        // Отрисовка начального состояния
        for (const [key, value] of Object.entries(data.canvasState)) {
            const {x, y, color} = value;
            pixelData[x][y] = color;
            redrawCanvas();
        }
    }

    if (data.pixelData) {
        // Обновление текущего состояния
        const {x, y, color} = data.pixelData;
        pixelData[x][y] = color;
        redrawCanvas();
    }
};

function drawGrid() {
    ctx.strokeStyle = "#ddd";
    for (let x = 0; x < GRID_SIZE; x++) {
        for (let y = 0; y < GRID_SIZE; y++) {
            ctx.strokeRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
        }
    }
}

function redrawPixels() {
    for (let x = 0; x < GRID_SIZE; x++) {
        for (let y = 0; y < GRID_SIZE; y++) {
            if (pixelData[x][y]) {
                ctx.fillStyle = pixelData[x][y];
                ctx.fillRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }
}

function redrawCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(offsetX, offsetY);
    ctx.scale(scale, scale);
    redrawPixels();
    drawGrid();
    ctx.restore();
}

canvas.addEventListener("click", (event) => {
    const rect = canvas.getBoundingClientRect();
    const mouseX = (event.clientX - rect.left - offsetX) / scale;
    const mouseY = (event.clientY - rect.top - offsetY) / scale;
    const x = Math.floor(mouseX / CELL_SIZE);
    const y = Math.floor(mouseY / CELL_SIZE);
    if (x >= 0 && x < GRID_SIZE && y >= 0 && y < GRID_SIZE) {
        pixelData[x][y] = currentColor;
        redrawCanvas();

        // Отправляем изменения через WebSocket
        SOCKET.send(JSON.stringify({pixel_data: {x, y, color: currentColor}, canvas_id: 0}));
    }
});

canvas.addEventListener("wheel", (event) => {
    event.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    const zoomFactor = event.deltaY < 0 ? 1.1 : 0.9;
    const previousScale = scale;
    scale = Math.min(Math.max(scale * zoomFactor, 0.5), 4);

    offsetX -= (mouseX - offsetX) * (scale / previousScale - 1);
    offsetY -= (mouseY - offsetY) * (scale / previousScale - 1);

    redrawCanvas();
});

palette.addEventListener("click", (event) => {
    if (event.target.classList.contains("color")) {
        currentColor = event.target.getAttribute("data-color");
    }
});

redrawCanvas();

// form

const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("reg-form");
const showRegisterLink = document.getElementById("show-reg");
const showLoginLink = document.getElementById("show-login");

showRegisterLink.addEventListener("click", (e) => {
    e.preventDefault();
    loginForm.classList.remove("form--active");
    registerForm.classList.add("form--active");
});

showLoginLink.addEventListener("click", (e) => {
    e.preventDefault();
    registerForm.classList.remove("form--active");
    loginForm.classList.add("form--active");
});