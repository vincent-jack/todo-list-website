if (localStorage.getItem("background") != null) {
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

document.getElementById('checkbox-wrapper').addEventListener('change', function(event){
    var checkbox = event.target;
    var text = document.getElementsByClassName('task-' + checkbox.value)[0];
    console.log(text.innerText);
    if(checkbox.checked == true){
        text.innerHTML = '<strike>' + text.innerText + '</strike>';
    } else {
        text.innerHTML = text.innerText.replace('<strike>', '').replace('</strike>', '');
    }

    if(checkbox.name == "check"){
         $.ajax({
                url: '/updatedata',
                type: 'POST',
                data: { 'row': checkbox.value,
                        'checked': checkbox.checked},
            });
    }
});