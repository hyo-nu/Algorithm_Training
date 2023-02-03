#include <iostream>
#include <ios>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int testnum = 0;
    cin>>testnum;
    
    int *p = new int[testnum];
    int a,b;
    
    for (int i =0; i < testnum; i++)
    {
        cin >>a>>b;
        p[i] = a+b;
    }
    
    for (int i = 0; i<testnum; i++)
    {
        cout << p[i] << "\n";
    }
    return 0;
}