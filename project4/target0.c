#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int _main(int argc, char *argv[])
{
	char grade[5];
	char name[10]; //Buffer holds 10 bytes

	strcpy(grade, "nil");

	gets(name); //We can put in more than 10 bytes..

	printf("Hi %s! Your grade is %s.\n", name, grade);
	
	exit(0);	
}
