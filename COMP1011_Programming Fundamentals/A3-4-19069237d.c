#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define LENGTH 21

void toUppercase(char *str);
void matchWithOneTDel(const char *sT, const char *sP);

int main(void){
    char target[LENGTH];
    char pattern[LENGTH];
    
    printf("Please input a target string: ");
    scanf("%s",target);
    toUppercase(target);                        //turn all letters to uppercase for convenience
    printf("Please input a pattern string: ");
    scanf("%s",pattern);
    toUppercase(pattern);
    
    matchWithOneTDel(target,pattern);
    
    return 0;
}

void toUppercase(char *str){
    for(size_t i=0; i<LENGTH; i++){
        str[i] = toupper(str[i]);
    }
}

void matchWithOneTDel(const char *sT, const char *sP){
    if (strstr(sT,sP) == NULL){                
        int count=0, match=0;                 //count: count the number of characters to be deleted
        size_t indexOfsT=0, indexOfsP=0;      //match: count the times of getting consecutive matching letter (the character to be deleted is excluded)
        size_t targetIndex=0, deleteIndex=0;
        
        while (indexOfsT < strlen(sT) && indexOfsP < strlen(sP)){
            if (match == strlen(sP)){   //if the number of matching characters == length of pattern string
                break;                  //exit the loop
            }
            
            if (sT[indexOfsT] != sP[indexOfsP]){  //if the current characters are not the same
                indexOfsT++;                      //prepare to read next character in target string

                if (match!=0){                        //if common character(s) is found already
                
                    if (sT[indexOfsT] != sP[indexOfsP]){  //if next character in target string is not the same as the current character in pattern string
                        match-=1;                         
                        indexOfsP=0;                      //start over to find a new combination
                    } 
                    else{                                 //else
                        count+=1;                         //one character should be deleted
                        deleteIndex=indexOfsT-1;          //store the previous index which is the index of character to be deleted
                        match++;                          //one more matching character
                        indexOfsT++;                      //prepare to read next characters in target string and pattern string
                        indexOfsP++;
                    }
                }
            }
            else{
                indexOfsT++;
                indexOfsP++;
                match++;       //one more matching character
            }
        }
        
        targetIndex = indexOfsT-1-strlen(sP); //since one character should be deleted, the target index should minus one
        
        if (count != 1){  //if number of characters to be deleted is not equal to 1
            match = 0;    //the two strings have no any matches
        }
        
        if(match==strlen(sP)){
            printf("No exact matches, but the pattern matches the target at index %zu after\n",targetIndex);
            printf("deleting the character at index %zu of the target.",deleteIndex);
        }
        else{
            puts("No exact matches.");
            puts("Also, no matches are possible by deleting a single character from the target.");
        }
    }
    else{
        puts("The pattern matches the target.");
        char *ptr = strstr(sT,sP);
        int index = ptr - sT;
        printf("The first exact match is at index %d in the target.",index);
    }
}