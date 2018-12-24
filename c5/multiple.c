#include <stdio.h>
#include <stdlib.h>

int main(void){
  long long int n = 1;
  int state = 0;
  
  while(state < 20){
    state = 0;
    for(int i = 1; i <= 20;i++){
      if(n%i == 0){
	state += 1;
      }
    }
    n += 1;
  }


  printf("%lld \n", n-1);
  
}
