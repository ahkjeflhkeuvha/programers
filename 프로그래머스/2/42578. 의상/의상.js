function solution(clothes) {
    var selection = 1;
    var cloth = new Map();
    
    clothes.forEach((val) => {
        if(cloth.get(val[1]) === undefined) cloth.set(val[1], 2)
        else cloth.set(val[1], cloth.get(val[1]) + 1)
        
    })
    
    for(let [key, val] of cloth){ 
        selection *= val
    }
    
    return selection - 1;
}