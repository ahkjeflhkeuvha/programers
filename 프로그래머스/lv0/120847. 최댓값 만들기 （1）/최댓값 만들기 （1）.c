#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int i, j, max = 0;
    for(i=0; i<numbers_len; i++){
        for(j=0; j<numbers_len; j++){
            if(i != j)
                if(max < numbers[i]*numbers[j]) max = numbers[i]*numbers[j];
        }
    }
    return answer = max;
}