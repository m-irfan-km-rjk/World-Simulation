const canvas = document.querySelector("#world");
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var cols = 100;
var rows = 100;
var tw = canvas.width/rows;
var th = canvas.height/cols;

const terrains = [
  ["Grass", "#7CFC00FF"],   // 0
  ["Water", "#00BFFFCC"],   // 1
  ["Sand",  "#F4A460FF"],   // 2
  ["Forest","#228B22FF"],   // 3
  ["Swamp", "#556B2FFF"]    // 4
];

var world_data = [];

function get_world() {
    fetch("http://localhost:5000/generate")
        .then(response => response.json())
        .then(data => {
            world_data = data;
            update();
        })
        .catch(error => {
            console.error("Error fetching world data:", error);
        });
}

function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for(var i = 0;i < cols;i++) {
        for(var j = 0; j< rows;j++) {
            ctx.fillStyle = terrains[world_data[j][i]][1];
            ctx.strokeRect(tw*j,th*i,tw,th);
            ctx.fillRect(tw*j,th*i,tw,th);
        }
    }
}


setInterval(() => {
    get_world();
}, 3000);