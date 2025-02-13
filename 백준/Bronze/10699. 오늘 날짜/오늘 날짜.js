let n = new Date();
let year = n.getFullYear();
let month = n.getMonth() + 1;
let date = n.getDate();

console.log(`${year}-${month.toString().padStart(2, "0")}-${date}`);
