#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int isPalindrome(int n){
  //int to char array conversion
  char str[10] = "";
  sprintf(str, "%d", n);
  
  int len = strlen(str);
  char reverse[10];
  strcpy(reverse, str);
  for(int i = len-1, j = 0;i >= 0;i--, j++){
    reverse[j] = str[i];
  }
  
  if(strcmp(reverse, str) == 0){
    return 1;
  }else{
    return 0;
  }
}

int main(void){
  int record = 0;
  for(int i = 99; i < 998;i++){
    for(int j = 99;j < 998;j++){
      if(i != j){
				int p = i * j;
      	if(isPalindrome(p) == 1){
					printf("%d \n", p);
      	}
			}
    }
  }


  printf("%d \n", record);
}

  
