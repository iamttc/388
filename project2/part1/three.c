#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
 
const char *string = "The quick brown fox jumped over the lazy dog's back";
//Base code taken from https://rosettacode.org/wiki/MD5#C
//Thanks to @379 on piazza
//gcc three.c -o three -lssl -lcrypto -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include
//add -w at the end to suppress warnings


int main() {
  unsigned char result[MD5_DIGEST_LENGTH];
  printf("whaat%d\n", MD5_DIGEST_LENGTH);
  bool found = false;
 
  //MD5(string, strlen(string), result);
  //MD5 is 32 hex digits We need first 7 to be 27 20 4F 52 20 31 23

  unsigned char answer[7] = {0x27, 0x20, 0x4F, 0x52, 0x20, 0x31, 0x23, 0};
 
  while(!found){
    MD5(string, strlen(string), result);

    for(int i = 0; i < 7; i++)
      if(result[i] != answer[i]
      printf("%02x\n", answer[i]);//
    printf("\n");

  }
  //Print final output
  for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
    printf("%02x\n", result[i]);//
  printf("\n");

  for(int i = 0; i < 7; i++)
    if(result[i] != answer[i]
    printf("%02x\n", answer[i]);//
  printf("\n");
 
  return EXIT_SUCCESS;
}
