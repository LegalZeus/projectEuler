#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n = 1000;
	int multiples[n-1];

	for(int i = 0; i < n-1;i++){
		multiples[i] = i+1;
	}


	int r = 0;
	for(int i = 0; i < n-1;i++){
		int x = multiples[i];
		if(x%3 == 0 || x%5 == 0){
			r += x;
		}
	}


	printf("sum : %d \n", r);


}
