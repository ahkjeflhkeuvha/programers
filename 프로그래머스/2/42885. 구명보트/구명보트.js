function solution(people, limit) {
    let answer = 0; 
    let sortedPeople = people.sort((a, b) => a - b) 

    while (sortedPeople.length !==0) { 
        if (sortedPeople[0] + sortedPeople[sortedPeople.length-1] <= limit) { 
            answer++ 
            sortedPeople.shift();
            sortedPeople.pop();
        } else {
            answer++
            sortedPeople.pop();  
        }
  }
    
  return answer; 
}