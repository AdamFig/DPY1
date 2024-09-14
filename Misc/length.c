#include <string.h>
#include <stdio.h>

int main() {
  char str[100];
  printf("Enter a string: ");
  scanf("%s", str);
  int length = strlen(str);
  printf("The length of the string is: %d\n", length);
  return 0;
}