#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int count = 0;
    
    for(int i = 0; i < s.length(); i++)
    {
        count++;
        if(s[i] == 'c')
        {
            if(s[i+1] == '=' || s[i+1] == '-')
                count--;
        }
        else if(s[i] == 'j')
        {
            if(s[i-1] == 'l' || s[i-1] == 'n')
                count--;
        }
        else if(s[i] == '=')
        {
            if(s[i-1] == 's' || s[i-1] == 'z')
                count--;
        }
        else if(s[i] == 'd')
        {
            if(s[i+1] == '-')
                count--;
            else if(s[i+1] == 'z')
            {
                if(s[i+2] == '=')
                    count--;
            }
        }     
    }
    cout << count;
    return 0;
    
}