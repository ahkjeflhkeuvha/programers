#include <stdio.h>
int main(void){
	int price, num, i;
	
	scanf("%d %d", &price, &num);
	
	int thing, count;
	int totalPrice = 0, totalNum = 0;
	for(i = 1; i<=num; i++){
		scanf("%d %d", &thing, &count);
		totalPrice += thing*count;
	}
	if(totalPrice == price) printf("Yes");
	else printf("No");
	return 0;
}