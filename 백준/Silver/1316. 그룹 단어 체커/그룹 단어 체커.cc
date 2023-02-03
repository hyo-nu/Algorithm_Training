#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    cin >> num;
    int count[100] = { 0, };
    int sum = 0;

    for (int i = 0; i < num; i++)
    {
        string s;
        cin >> s;

        count[i] = 1;
        for (int j = 0; j < s.length(); j++)
        {
            for (int k = j + 2; k < s.length(); k++)
            {
                if (s[j] != s[j + 1])
                {
                    if (s[j] == s[k])
                        count[i] = 0;
                }
            }
        }

    }
    for (int i = 0; i < num; i++)
    {
        sum += count[i];
    }
    cout << sum;
    return 0;
}
