#include <iostream>
#include <cctype>
using namespace std;


void main(void) {
	int list[26] = {0,};
	int point, max=0;
	bool same = false;
	while (1) {
		int ch = getchar();
		if (ch == '\n')
			break;
		if (++list[tolower(ch) - 'a'] > max) {
			point = tolower(ch) - 'a';
			max = list[tolower(ch) - 'a'];
			same = false;
		}
		else if (list[tolower(ch) - 'a'] == max)
			same = true;

	}
	if (same)
		cout << "?" << endl;
	else
		cout<<(char)toupper(point+'a')<<endl;
}