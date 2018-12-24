#include <stdio.h>
#include <stdlib.h>


int main(void){
  long int record = 0;
  long int n_record = 0;
  for(long int i = 3;i < 1000000;i++){
    long int n = i;
    printf("%ld : ", n);
    int len = 1;
    while(n != 1){
      len += 1;
      if(n%2 == 0){
	n = n/2;
      }else{
	n = 3*n+1;
      }  
    }
    if(len >= record){
      record = len;
      n_record = i;
    }
    printf("%d \n", len);
  }

  printf("\n\n\n%ld : %ld \n", n_record, record);
}
