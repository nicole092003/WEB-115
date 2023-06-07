var $ = function (id) {
    return document.getElementById(id);
}

var calculate_click = function()
{ 
    var cents = parseInt($("cents").value);

    var coins = new Map();
    coins.set("quarters", 25);
    coins.set("dimes", 10);
    coins.set("nickels", 5);
    coins.set("pennies", 1);

    coins.forEach(function(value, key){
        $(key).value = Math.floor(cents / value);
        cents = cents % value;
    });

    var quarters = Math.floor(cents / coins.get("quarters"));
    cents = cents % coins.get("quarters");
    $("quarters").value = quarters;

    var dimes = Math.floor(cents / coins.get("dimes"));
    cents = cents % coins.get("dimes");
    $("dimes").value = dimes;

    var nickels = Math.floor(cents / coins.get("nickels"));
    cents = cents % coins.get("nickels");
    $("nickels").value = nickels;

    var pennies = Math.floor(cents / coins.get("pennies"));
    cents = cents % coins.get("pennies");
    $("pennies").value = pennies;
    
}

$("calculate").addEventListener("click", calculate_click);
