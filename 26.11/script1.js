//window.prompt("Tekst1","Tekst2");
function printForm(){
    var x  = document.forms[0].elements;
    console.log(x[0].value);
    console.log(typeof(x[0].value));
    console.log(x[1].value);
    console.log(typeof(x[1].value));
    window.alert(x[0].value + ", " + x[1].value);
}

function onLoader(){
    console.log('Tekst 1');
    //window.alert('Tekst 2');
    //document.write('Tekst 3');
}

//window.prompt(title, default_value)
//returns none on abort
//returns empty string on empty field
//returns string with value
