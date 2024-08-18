#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define LENGTH 26

void removeSpaceANDtoUpper(char str[], int SIZE);
void storeOccurrence(const char str[], int occurrence[]);
int compareArrays(const int str1[], const int str2[], int SIZE);

int main(){
    char string1[LENGTH];
    char string2[LENGTH];
    int alphabet1[LENGTH] = {0};
    int alphabet2[LENGTH] = {0};
    
    printf("This program can check whether two sentences contain the same number of occurrences ");
    puts("as each other of each of the 26 letters in the alphabet\n");
    printf("Enter two lines of text (less than %d characters in each line): ",LENGTH-1);
    
    //first string
    fgets(string1, sizeof(string1), stdin);  // read the whole sentence
    removeSpaceANDtoUpper(string1, LENGTH);  // remove the characters that are not letters & turn all letters to uppercase
    //second string
    fgets(string2, sizeof(string2), stdin);
    removeSpaceANDtoUpper(string2, LENGTH);


    //first string
    storeOccurrence(string1, alphabet1);     // count the occurrence of each letter and store it in an array
    //second string                          // with alphabetical order (i.e. alphabet1[0] = occurrences of A,
    storeOccurrence(string2, alphabet2);     // alphabet1[1] = occurrences of B)
    
    
    int result = compareArrays(alphabet1, alphabet2, LENGTH);
    if (result == 1){ 
        puts("\nYES");
    }
    else{
        puts("\nNO");
    }
    
}


void removeSpaceANDtoUpper(char str[], int SIZE){
    for (size_t i = 0; i < SIZE; i++){
        if (isalpha(str[i]) == 0){
            for (size_t j = i; j < SIZE; j++){
                str[j] = str[j+1];              // remove the characters that are not letters
            }
        }
        str[i] = toupper(str[i]);               // convert all characters into uppercase
    }    
    for (size_t i = 0; i < SIZE; i++){          // repeat one more time to prevent excess spaces & symbols affecting the result
        if (isalpha(str[i]) == 0){
            for (size_t j = i; j < SIZE; j++){
                str[j] = str[j+1];              
            }
        }
        str[i] = toupper(str[i]);               
    }    
}


void storeOccurrence(const char str[], int occurrence[]){
    for (size_t i = 0; i < strlen(str); i++){
        int ascii = (int)str[i];                // match the characters with the array storing occurrences of each letter
        occurrence[ascii-65] += 1;              // by using their ASCII value
    } 
}


int compareArrays(const int str1[], const int str2[],int SIZE){
    for (size_t i = 0; i < SIZE; i++){
        if (str1[i] != str2[i]){               // if any pair of occurrences of a letter is not equal, 
            return 0;                          // (i.e.the two sentences are different), return 0
        }
    }
    return 1;                                  // otherwise, return 1
}