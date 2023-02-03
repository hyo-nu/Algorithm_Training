#include <iostream>
using namespace std;

int main()
{
    int test,high,wide,count;
    cin >> test; 
    for(int i = 0; i < test; i++)
    {
        cin >> high >> wide >> count;
        int floor;
        int ho;
        
        floor = count % high;
        ho = count / high;
        if(floor > 0)
            ho++;
        else if(floor == 0)
            floor = high;
        cout << floor*100 + ho << endl;       
    }
    return 0;
}