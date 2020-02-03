/* Reverse String
    Implement a function void reverse(char * str) in C or C++ which reverses
    a null terminated string.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void reverse(char* string);

int main(int argc, char const *argv[]) {
    char string[] = "lucass";
    char original[strlen(string)];
    
    strcpy(original, string);

    reverse(string);
    printf("reverse(%s) -> %s \n", original, string);
    return 0;
}


void reverse(char * string) {
    char *end = string;
    char tmp;

    if (string) {
        while (*end) { /* Find end of the strings */
            ++end;
        }
    }
    --end; /* set one char back, since last char is null */

    while (string < end) {
        tmp = *string;
        *string++ = *end;
        *end-- = tmp;
    }
}