function solution(name, yearning, photo) {
    var answer = new Array(photo.length).fill(0);
    
    for(i in photo){
        photo[i].forEach((val, idx) => {
            if(name.indexOf(val) > -1) answer[i] += yearning[name.indexOf(val)];
        })
    }
    return answer;
}