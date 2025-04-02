#include <stdio.h>
#include <string.h>
#define max 100

char infix[max],postfix[max],stack[max];
int postfix_top=-1;
int stack_top=-1;

void push(char item)
{
    stack_top++;
    stack[stack_top]=item;
}

char pop()
{
    char x=stack[stack_top];
    stack_top--;
    return x;
}

int is_operator(char symbol)
{
    if(symbol=='^' || symbol=='*' || symbol=='/' || symbol=='%' || symbol=='+' || symbol=='-')
        return 1;
    else
        return 0;
}

int pre(char symbol)
{
    if(symbol=='^')
        return 3;
    else if(symbol=='*' || symbol=='/' || symbol=='%')
        return 2;
    else if(symbol=='+' || symbol=='-')
        return 1;
    else
        return 0;
}

void convert()
{
    push('(');
    strcat(infix,")");

    int i=0;
    char x,item;
    item=infix[i];

    while(item!='\0'){
        if(item=='(')
            push(item);
            
        else if(isdigit(item) || isalpha(item)){
            postfix_top++;
            postfix[postfix_top]=item;
        }
            
        else if(is_operator(item)==1){
            x=pop();
            while(is_operator(item)==1 && pre(x)>=pre(item)){
                postfix_top++;
                postfix[postfix_top]=x;
                x=pop();
            }
            push(x);
            push(item);
        }
            
        else if(item==')'){
            x=pop();
            while(x!='('){
                postfix_top++;
                postfix[postfix_top]=x;
                x=pop();
            }
        }
        i++;
        item=infix[i];
    }
}

void main()
{
    printf("Enter the expression : ");
    scanf("%s",&infix);

    convert();
    int i=0;
    while(postfix[i]!='\0'){
        printf("%c ",postfix[i]);
        i++;
    }
}
