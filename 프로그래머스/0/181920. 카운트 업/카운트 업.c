#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start_num, int end_num) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * (end_num - start_num + 1));
    int i = 0;
    int num = start_num;
    for(i = 0; i<end_num - start_num + 1; i++){
        answer[i] = num++;
    }
    return answer;
}