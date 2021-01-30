let parser = {
parse: function (arr){
    let out = []
    let dict = {"d-":0, "d+":1, "h+":2, "h-":3}
    for(s of arr){
        try {
            out.push(dict[s]);
        } catch (error) {
            continue;
        }
    }
    return out
}}