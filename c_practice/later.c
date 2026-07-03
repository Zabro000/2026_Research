#include <stdio.h>

struct data {
    char string[128]; 
    int code;
    unsigned int code_2;
};

#define a 101




int main(void)
{
    struct data cool = {"neat", 15, 11};
    printf("%d\n", cool.code_2);

    int aa[2] = {1, 2};

    printf("%d\n", *aa);
    printf("%c", cool.string[1]);
    printf("%c", *(cool.string + 1));

}