if (localStorage.getItem("background") == null) {
    document.getElementById("body").className = "background-animated-3";
} else {
    document.getElementById("body").className = localStorage.getItem("background");
};

document.getElementById("button-1").addEventListener("click", function() {
    document.getElementById("body").className = "background-animated-1";
    localStorage.setItem("background", "background-animated-1");
});
document.getElementById("button-2").addEventListener("click", function() {
    document.getElementById("body").className = "background-animated-2";
    localStorage.setItem("background", "background-animated-2");
});
document.getElementById("button-3").addEventListener("click", function() {
    document.getElementById("body").className = "background-animated-3";
    localStorage.setItem("background", "background-animated-3");
});
document.getElementById("button-4").addEventListener("click", function() {
    document.getElementById("body").className = "background-animated-4";
    localStorage.setItem("background", "background-animated-4");
});