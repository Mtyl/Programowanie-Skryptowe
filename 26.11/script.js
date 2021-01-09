"use strict"
function cyfry(napis){
    var sum = 0;
    for (const char of napis) {
        sum += isNaN(Number(char)) ? 0 : Number(char);        
    }
    return sum
}

function litery(napis){
    var sum = 0;
    for (const char of napis) {
        sum += isNaN(Number(char))? 1 : 0;        
    }
    return sum
}

function suma(napis){
    if(typeof(suma.suma) == 'undefined'){
        suma.suma = 0
    }
    var num = ""
    for (const char of napis){
        if(isNaN(Number(char))){
            break;
        }else{
            num += char
        }
    }
    suma.suma += Number(num)
    return suma.suma
}
var a = chai.assert
describe('String', function(){
    it('numbers only', function(){
        a.equal(cyfry("1234") , 10)
        a.equal(litery("1234") , 0)
        a.equal(suma("1234") , 1234)
    });
    it('letters only', function(){
        a.equal(cyfry("abcd") , 0)
        a.equal(litery("abcd") , 4)
        a.equal(suma("abcd") , 1234)
    });
    it('numbers after letters', function(){
        a.equal(cyfry("ab34") , 7)
        a.equal(litery("ab34") , 2)
        a.equal(suma("ab34") , 1234)
    });
    it('numbers before letters', function(){
        a.equal(cyfry("12cd") , 3)
        a.equal(litery("12cd") , 2)
        a.equal(suma("12cd") , 1246)
    });
    it('empty string', function(){
        a.equal(cyfry("") , 0)
        a.equal(litery("") , 0)
        a.equal(suma("") , 1246)
    });
});

var x = window.prompt()
while(x != null){
    console.log(cyfry(x), litery(x), suma(x))
    x = window.prompt()
}