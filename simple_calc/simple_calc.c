#include <stdio.h>

// float functions from assembly
extern float add(float a, float b);
extern float sub(float a, float b);
extern float mul(float a, float b);
extern float fdiv(float a, float b);

int main() {
    float x, y, result;
    int choice;

    while (1) {
        printf("\nChoose operation:\n");
        printf("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        if (choice == 5) {
            printf("Exiting calculator. Goodbye!\n");
            break;
        }

        printf("Enter x: ");
        scanf("%f", &x);
        printf("Enter y: ");
        scanf("%f", &y);

        switch (choice) {
            case 1:
                result = add(x, y);
                printf("Sum of %.2f & %.2f is %.2f\n", x, y, result);
                break;
            case 2:
                result = sub(x, y);
                printf("Difference of %.2f & %.2f is %.2f\n", x, y, result);
                break;
            case 3:
                result = mul(x, y);
                printf("Product of %.2f & %.2f is %.2f\n", x, y, result);
                break;
            case 4:
                if (y == 0.0f) {
                    printf("Error: Division by zero!\n");
                    break;
                }
                result = fdiv(x, y);
                printf("Division of %.2f / %.2f is %.2f\n", x, y, result);
                break;
            default:
                printf("Invalid choice! Please select 1-5.\n");
                break;
        }
    }

    return 0;
}