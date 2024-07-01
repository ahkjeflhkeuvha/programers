function solution(phone_book) {
    let answer = true;
    let hashMap = new Map();

    phone_book.forEach(e=> {
        hashMap.set(e, '');
    })

    for(let [key, value] of hashMap) {
        for(let i=1; i<key.length; i++) {
            let pre = key.slice(0, i);

            if(hashMap.has(pre)) return false;
        }
    }

    return answer;
}