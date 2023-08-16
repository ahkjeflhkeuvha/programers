#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
	char a[4], b[4];
	scanf("%s %s", a, b);
	
	char a_s[4], b_s[4];
	int i, j;
	for(i=0, j=strlen(a)-1; i<strlen(a), j>=0; i++, j--){
		a_s[i] = a[j];
		b_s[i] = b[j];
	}
	
	int a_i, b_i;
	a_i = atoi(a_s);
	b_i = atoi(b_s);
	
	if(a_i > b_i) printf("%d", a_i);
	else printf("%d", b_i);
	
}