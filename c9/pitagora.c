#include <stdio.h>
#include <stdlib.h>

int isTriplet(int a, int b, int c);

int main(void){
  int sum = 1000; 
  long int r = 0;
  for(int a = 0;a < sum;a++){
    for(int b = 0;b < sum;b++){
      for(int c = 0;c < sum;c++){
	if(a+b+c == sum && isTriplet(a, b, c)){
	  r = a*b*c;
	  break;
	}
      }
    }
  }


  printf("%ld \n", r); 
}





int isTriplet(int a, int b, int c){

  if(a != b && c > a && c > b){
    a = a * a;
    b = b * b;
    if(c * c == a+b){
      return 1;
    }
  }
  return 0;
}
