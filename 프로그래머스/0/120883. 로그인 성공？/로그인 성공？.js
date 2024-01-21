function solution(id_pw, db) {
    const [id, pw] = id_pw;
    var map = new Map(db);
    return map.has(id) ? (map.get(id) === pw ? 'login' : 'wrong pw') : 'fail';
}