function solution(rank, attendance) {
    const [a, b, c] = rank
        .map((r, i) => [r, i])
        .filter(([_, i]) => attendance[i])
        .sort(([a], [b]) => a-b);
    return a[1] * 10000 + b[1] * 100 + c[1];
}