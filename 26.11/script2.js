"use strict"
var resultMap = new Map()

function getWords(){
    var text = document.forms[0].elements[0].value;
    text = text.split("\n");
    var words = [];
    var i = 1;
    for (var line of text){
        var t;
        for(t of line.split(" ")){
            //console.log(line);
            if(t == ""){
                continue;
            }
            words.push({t, i});
        }
        i++
    }
    console.log(typeof(words))
    return words;
}


function getNumbers(arr){
    var out = [];
    for(var i of arr){
        var num = Number(i.t)
        var ind = i.i
        if(!isNaN(num)){
            out.push({num, ind});
        }
        else{
            return -1;
        }
    }
    return out;
}

function count(words, numbers){
    if(!document.getElementById("prev").checked){
        resultMap = new Map()
    }
    if(numbers == -1){
        for(var el of words){
            if(!resultMap.has(el.t)){
                resultMap.set(el.t, 1);
            }else{
                var x = resultMap.get(el.t);
                resultMap.set(el.t, x+1);
            }
        }
    }else{
        for(var el of numbers){
            if(!resultMap.has(el.num)){
                resultMap.set(el.num, [el.ind]);
            }else{
                var x = resultMap.get(el.num);
                x.push(el.ind)
                resultMap.set(el.num, x);
            }
        }
    }
}

function mainF(){
    var words = getWords();
    var numbers = getNumbers(words);
    count(words, numbers);
    console.log(resultMap);
}

