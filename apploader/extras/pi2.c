#include <stdio.h>
#include <float.h>
#include <stdio.h>
#include <time.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
int main() {
    long double number = 3.14159;
    printf("Wdboyes13\n");
    printf("Calculatin PI *2\n");
    printf("ENTER To start");
    int c = getchar();
    if (c == '\n') {
        while (1) {
            #ifdef _WIN32
            Sleep(10);
            #else
            struct timespec ts = {0, 10000000L}; // 10 ms = 10,000,000 ns
            nanosleep(&ts, NULL);
            #endif
            number *= 2;
            printf("%Lf\n", number);
            if (number == LDBL_MAX) {
                number = 3.14159;
            }
        }
    }
}