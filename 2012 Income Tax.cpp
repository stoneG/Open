#include <iostream>

int main()
{
    using namespace std;
    double income = 0.0;
    double tax = 0.0;
    double taxRate[6] = {0.10, 0.15, 0.25, 0.28, 0.33, 0.35};
    double taxBracket[5] = {8700.0, 35350.0, 85650.0, 178650.0, 388350.0};
    double amtTaxable[5];
    for (int i = 1; i < 5; i++) // determines amount taxable in all but the highest bracket
    {
        amtTaxable[i] = taxBracket[i] - *(taxBracket+(i-1));
    }
    amtTaxable[0] = taxBracket[0];
    cout << "What's your income? (q to quit)\n$";
    while (cin >> income)
    {
        for (int i = 0; i < 5; i++) // Calculates taxes for incomes <= $388,350.
            if (income <= amtTaxable[i])
            {
                tax += income * taxRate[i];
                income = 0.0;
            }
            else
            {
                tax += amtTaxable[i] * taxRate[i];
                income -= amtTaxable[i];
            }
        tax += income * taxRate[5];
        cout << "You need to pay $" << tax << " in taxes.\n";
        cout << "Another income? (q to quit)\n$";
        tax = 0.0;
        continue;
    }
    return 0;
}
