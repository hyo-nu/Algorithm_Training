#include <iostream>
#include <string>

using namespace std;

void sweap(char *three, char *one)
{
    char temp = *one;
    *one = *three;
    *three = temp;
}
int main()
{
    string s;
    getline(cin, s);
    
    sweap(&s[0], &s[2]);
    sweap(&s[4], &s[6]);
    
    int a = 100 * ((int)s[0]-48) + 10 * ((int)s[1]-48) + ((int)s[2]-48);
    int b = 100 * ((int)s[4]-48) + 10 * ((int)s[5]-48) + ((int)s[6]-48);
    
    if (a>b)
        cout << a;
    else
        cout << b;  
    return 0;
}