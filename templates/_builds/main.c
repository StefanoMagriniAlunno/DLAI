/**
 * @file main.c
 * @author your name (you@domain.com)
 * @brief
 * @version 0.1
 * @date 2024-06-27
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <stdio.h>  // Include the standard input/output library
#include "inc/test.h"  // Include the header file


/**
 * @brief  main function
 *
 * @return int
 *
 * @note Use this function to test the library
 */
int main(const int argc, const char *argv[]) {
    // mi assicuro che ci siano 2 valori in input
    if (argc != 3) {
        return -1;
    }
    // converto i valori in interi
    int a = (int32_t)atoi(argv[1]);
    int b = (int32_t)atoi(argv[2]);

    // testo la funzione sum
    int32_t ret = sum(a, b);

    // stampo il risultato
    printf("The sum of %d and %d is %d\n", (int)a, (int)b, (int)ret);

    return 0;
}
