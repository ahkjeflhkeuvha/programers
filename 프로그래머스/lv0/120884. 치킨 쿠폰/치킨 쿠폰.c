#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int chicken) {
    int answer = -1;
    
    int coupon = chicken;
    int order = 0, last = 0;
    
    while(coupon>9){
        order += coupon/10;
        last = coupon%10;
        coupon = coupon/10 + last;
    }
    
    return answer = order;
}