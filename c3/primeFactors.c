#include <stdio.h>
#include <math.h>



void primeFactors(long int n){
  while(n%2 == 0){

    printf("%d - ", 2);
    n = n/2;
  }

  for(int i = 3;i <= sqrt(n);i += 2){

    while(n%i == 0){
      printf("%d - ", i);
      n = n/i;
    }
 
  }

  if(n > 2){
    printf("%ld - ", n);
  }
}




int main(void){
  long int n = 600851475143;
  primeFactors(n);

}
