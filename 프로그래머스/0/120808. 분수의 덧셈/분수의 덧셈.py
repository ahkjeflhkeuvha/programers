import math

def solution(numer1, denom1, numer2, denom2):
    fir = numer1 * denom2 + numer2 * denom1
    sec = denom1 * denom2
    return [fir/math.gcd(fir, sec), sec/math.gcd(fir, sec)]