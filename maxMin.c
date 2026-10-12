/* Assignment 5 - Find the minimum and maximum of a set of values (max 15) */
#include <stdio.h>

#define MAX_ENTRIES 15

/* Finds min and max and returns them in the result array:
   result[0] = minimum, result[1] = maximum */
void find_min_max(int numbers[], int count, int result[])
{
    int i;
    result[0] = numbers[0];
    result[1] = numbers[0];

    for (i = 1; i < count; i++)
    {
        if (numbers[i] < result[0])
            result[0] = numbers[i];
        if (numbers[i] > result[1])
            result[1] = numbers[i];
    }
}

int main()
{
    int numbers[MAX_ENTRIES];
    int result[2];
    int count, i;

    printf("How many numbers (1 to %d)? ", MAX_ENTRIES);
    scanf("%d", &count);

    if (count < 1 || count > MAX_ENTRIES)
    {
        printf("Invalid number of entries.\n");
        return 1;
    }

    printf("Enter the numbers:\n");
    for (i = 0; i < count; i++)
    {
        scanf("%d", &numbers[i]);
    }

    find_min_max(numbers, count, result);

    printf("\nNumbers entered: %d\n", count);
    printf("Minimum number is: %d\n", result[0]);
    printf("Maximum number is: %d\n", result[1]);

    return 0;
}