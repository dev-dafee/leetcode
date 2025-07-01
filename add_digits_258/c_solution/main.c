#include <stdio.h>
#include <string.h>

int addDigits(int num) {
    char buffer[12];  // enough to hold any 32-bit int
    while (num > 9) {
        sprintf(buffer, "%d", num); // convert num to string
        int sum = 0;
        for (size_t i = 0; i < strlen(buffer); i++) {
            sum += buffer[i] - '0';  // convert char to int
        }
        num = sum;
    }
    return num;
}

int main() {
    int num = 12345;
    printf("Result: %d\n", addDigits(num));
    return 0;
}
