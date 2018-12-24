#include <stdio.h>
#include <stdlib.h>


int isPrime(int n);

int main(void){
  long int len = 10001;

  for(int i = 2, j = 0;j < len;i++){
    if(isPrime(i) == 1){
      printf("%d \n", i);
      j++;
    }

  }
  

}




int isPrime(int n){

  for(int i = 2;i < n;i++){
    if(n%i == 0){
      return 0;
    }
  }

  return 1;
  

}
