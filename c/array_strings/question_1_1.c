/*
    Is Unique:
         Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>


bool isUnique(char* string);
bool isUniqueBitArray(char* string);

int main(int argc, char const *argv[]) {
    char string[] = "lucass";

    printf("isUnique(%s) -> %u \n", string, isUnique(string));
    printf("isUniqueBitArray(%s) -> %u \n", string, isUniqueBitArray(string));
    return 0;
}

bool isUnique(char *string) {
    int wordLength = (int) strlen(string);

    for (int i = 0; i < wordLength; i++) {
        for (int j = i + 1; j < wordLength; j++) {
            if (string[i] == string[j]) {
                return false;
            }
        }
    }

    return true;
}

bool isUniqueBitArray(char *string) {
    int wordLength = (int) strlen(string);

    int checker = 0;

    for (int i = 0; i < wordLength; i++) {
        int mask = 1 << (string[i] - 'a');

        if (checker & mask > 0) {
            return false;
        }

        checker |= mask;
    }

    return true;
}


