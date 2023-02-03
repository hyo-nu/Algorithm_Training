#include <iostream>
using namespace std;

int main()
{
	int n, temp;
	int front, back;
	int count = 0;

	cin >> n; 

	temp = n;

	if (n < 0 || n > 99)
		return 0;
	
	while (1)
	{
		front = n / 10;
		back = n % 10;

		n = back * 10 + ((front + back) % 10);
		count++;

		if (n == temp)
		{
			cout << count << endl;
			break;
		}
	}
	
	return 0;
}