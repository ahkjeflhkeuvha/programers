function solution(numbers) {
    return numbers
        .map(num => num.toString())
        .sort((a, b) => (b + a).localeCompare(a + b))
        .join('')
        .replace(/^0+/, '0');
}