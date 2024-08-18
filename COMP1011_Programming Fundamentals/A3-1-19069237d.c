#include <stdio.h>
#include <string.h>
#define LENGTH 1000

void ignoreOthers(const char* str, char *str2); 
int decideWellBalanced(const char *str);

int main(){
    char sentence[LENGTH];
    char modifiedSentence[LENGTH];
    
    printf("%s","Please input a string: ");
    scanf("%999s",sentence);
    
    ignoreOthers(sentence,modifiedSentence);

    if(decideWellBalanced(modifiedSentence) == 1){
        printf("'%s' is well-balanced.",sentence);
    }
    else{
        printf("'%s' is not well-balanced.",sentence);
    }
    
    return 0;
}

void ignoreOthers(const char* str,char *str2){
    size_t i=0,j=0; 
    while (i<strlen(str)){
        if (str[i]=='('||str[i]==')'||str[i]=='['||str[i]==']'){ //ignore all characters in the string that are not (, ), [, or ]
            str2[j] = str[i];                                    //and store the related characters in another string
            j++;
        }
        i++;
    }
}

int decideWellBalanced(const char *str){
    size_t i=0;
    int parenthesis=0, bracket=0; //count the number of parenthesis and square bracket characters in the string
    while (i<strlen(str)){
        if (str[i] == '('){
            parenthesis++;
            if (str[i+1] == ']' || str[i+1] == '('){  //condition 2 and 3
                return 0;
                break;
            }
        }
        else if (str[i] == '['){
            bracket++;
            if(str[i+1] == ')' || str[i+1] == '['){  
                return 0;
                break;
            }
        }
        else if (str[i] == ')'){
            if (str[i+1] == ')'){      //condition 3
                return 0;
            }
            parenthesis--;
        }
        else if (str[i] == ']'){
            if (str[i+1] == ']'){
                return 0;
            }
            bracket--;
        }
        else{
            i++;
            continue;
        }
        i++;
    }
    
    if (parenthesis!=0 || bracket!=0){    //condition 1
        return 0;
    }
    
    return 1;
}