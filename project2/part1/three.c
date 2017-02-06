#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
 
//Base code taken from https://rosettacode.org/wiki/MD5#C
//Thanks to @379 on piazza
//gcc three.c -o three -lssl -lcrypto -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include
//add -w at the end to suppress warnings

int main() {
  unsigned char result[MD5_DIGEST_LENGTH];
  unsigned long long num = 0;
  unsigned char strll[256];
  int counter;
 
  //MD5(string, strlen(string), result);
  //MD5 is 32 hex digits We need first 7 to be 27 20 4F 52 20 31 23

  //OR doesn't have to be all caps
  //                          '   space   O     R   space   1     #
  //unsigned char answer[7] = {0x27, 0x20, 0x4F, 0x52, 0x20, 0x31, 0x23, 0};
  //unsigned char answer1[7] = {0x27, 0x20, 0x6F, 0x72, 0x20, 0x31, 0x23, 0};

  //Don't need 1st space actually

  unsigned char answer[6] = {0x27, 0x4F, 0x52, 0x20, 0x31, 0x23, 0};
  unsigned char answer1[6] = {0x27, 0x6F, 0x72, 0x20, 0x31, 0x23, 0};
 
  while(1){
    sprintf(strll, "%lld", num);
    MD5(strll, strlen(strll), result);

    counter = 0;
    for(int i = 0; i < 6; i++){
      if(result[i] == answer[i] || result[i] == answer1[i]){
        counter++;
      }
      else{
        break;
      }
    }

    if(counter == 6){
      printf("%llu\n", num);
      for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
        printf("%02x", result[i]);//
      printf("\n");
      return 0;
    }
    num++;
  }
  return 0;
}
