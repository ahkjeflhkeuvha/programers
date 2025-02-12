function solution(today, terms, privacies) {
    var answer = [];
    let termDict = {}
    
    for(let term of terms) {
        let [cases, month] = term.split(" ")
        termDict[cases] = month
    }
    
    let todayDate = new Date(today)
    
    privacies.forEach((privacy, i) => {
        let [date, cases] = privacy.split(" ")
        let month = termDict[cases]
        
        let privacyDate = new Date(date)
        let endDate = new Date(privacyDate.setMonth(privacyDate.getMonth() + Number(month)))
        
        if(todayDate >= endDate) answer.push(i+1)
    }) 
    return answer;
}