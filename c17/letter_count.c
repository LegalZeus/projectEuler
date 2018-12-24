#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int letterCount(int n);

int main(void){
  int o = letterCount(12);
  printf("%d \n", o);


}




int letterCount(int n){
  int r = 0;
  int ns[20] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 0, 6, 6, 8, 8, 7, 7, 9, 8, 8};
  
  char str[10] = "";
  sprintf(str, "%d", n);
  
  if(strlen(str) == 3) r += 7;
  if(n < 20) r += ns[str -'0'];
  for(int i = 0;i < strlen(str);i++){
    r += ns[str[i]-'0'];   
  }
  
  
  return r;
}







