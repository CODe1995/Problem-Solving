#include <iostream>
#include <math.h>
#define M_PI       3.14159265358979323846
using namespace std;

int main() {
	double r;	cin >> r;
	double w[2]; w[0] = r * r * M_PI;
	w[1] = r * r * 2;
	cout<<fixed;
	cout.precision(6);
	cout << w[0] << endl<<w[1]<<endl;

	return 0;
}