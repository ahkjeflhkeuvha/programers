function solution(name, yearning, photo) {
    var answer = new Array(photo.length).fill(0);
    for(let i = 0; i<photo.length; i++){
        for(person of photo[i]){
            if(name.indexOf(person) > -1) answer[i] += yearning[name.indexOf(person)]; 
        }
    }
    return answer;
}