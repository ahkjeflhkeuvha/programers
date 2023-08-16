#include <stdio.h>
#include <string.h>

int main(void) {
	
	int T,R;
	char S[20];
	
    	scanf("%d", &T);
	
	int i, j, k;
	for(i=0; i<T; i++) {
				
		scanf("%d %s", &R, S);
		
		for(j=0; j < strlen(S); j++) 
			for(k=0; k<R; k++) printf("%c", S[j]);
		
		printf("\n");
	}

}