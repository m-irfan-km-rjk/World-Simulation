const canvas = document.querySelector("#world");
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const colours = ["Red","Black","Green","Yellow"];

var Animal = ( id,color ) => {
    this.age = 0;
    this.size = 1;
    this.id = id;
    this.color = colours[color];

    this.update = () => {

    };
};