#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char s[101];
    int alpa[27];
    
    cin>>s;
    for(int i=0; i<26; i++)
        alpa[i] = -1;
    
    for(int i=0; i<strlen(s); i++)
    {
        if(alpa[(int)(s[i]-97)] == -1)
            alpa[(int)(s[i]-97)] = i;
    }
    
    for(int i=0; i<26; i++)
        cout << alpa[i] << " ";
    return 0;  
}