#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int test;
    cin >> test;
    char S[21];
    
    for(int i = 0; i<test; i++)
    {
        int R;
        cin >> R >> S;
        for(int j = 0; j < strlen(S); j++)
        {
            for(int k = 0; k < R; k++)
            {
                cout << S[j];
            }
        }
        cout << endl;
    }
    return 0;
}