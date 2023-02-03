#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    getline(cin,s);
    int count = 1;
    
    if(s.empty() == true)
    {
        cout << "0";
        return 0; 
    } 
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == ' ')
            count++;
    }
    if(s[s.length()-1] == ' ')
        count--;
    if(s[0]==' ')
        count--;
    
    cout << count;
    return 0;
    
}