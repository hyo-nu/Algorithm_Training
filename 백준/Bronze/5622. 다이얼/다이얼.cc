#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int sum = 0;
    
    for(int i = 0; i < s.length(); i++)
    {
        if((int)s[i] >= 65 && (int)s[i] <=67)
            sum += 3;
        else if((int)s[i] >= 68 && (int)s[i] <=70)
            sum += 4;
        else if((int)s[i] >= 71 && (int)s[i] <=73)
            sum += 5;
        else if((int)s[i] >= 74 && (int)s[i] <=76)
            sum += 6;
        else if((int)s[i] >= 77 && (int)s[i] <=79)
            sum += 7;
        else if((int)s[i] >= 80 && (int)s[i] <=83)
            sum += 8;
        else if((int)s[i] >= 84 && (int)s[i] <=86)
            sum += 9;
        else if((int)s[i] >= 87 && (int)s[i] <=90)
            sum += 10;        
    }
    cout << sum;
}