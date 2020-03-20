#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#define MAX 1000002
using namespace std;

int cnt[MAX];
int cntNum[MAX];
pair<int, int> *query;
pair <pair< int, int >, int >* sqrtQuery;

int* Qsub(int numb, int *answer) {
	cnt[numb]--;
	if (cnt[numb] == 0){
		answer[numb]--;
	}
	return answer;
}
int* Qsum(int numb, int* answer) {
	if (cnt[numb] == 0) {
		answer[numb]++;
	}
	cnt[numb]++;
	return answer;
}

int main() {
	int N,M;
	cin >> N;
	//쿼리가 1부터 시작되기 때문에 1씩 미리 증가해줌(계산하기 편하게끔)
	int *arr= new int[N+1];
	for (int i = 1; i < N+1; i++) {
		cin >> arr[i];		
	}
	cin >> M;
	int* answer;
	answer = new int[M + 1];
	for (int i = 0; i < M + 1; i++) { answer[i] = 0; }
	query = new pair<int, int>[M+1];
	sqrtQuery = new pair<pair<int, int>, int>[M+1];
	for (int i = 1; i < M+1; i++) {
		cin >> query[i].first>> query[i].second;		
		sqrtQuery[i].first = pair<int, int>(query[i].first / sqrt(N), query[i].second);
		sqrtQuery[i].second = i;//순서가 바뀌어도 i로 순차적 출력을 해줘야함
	}
	sort(sqrtQuery + 1, sqrtQuery + M + 1);

	int s, e,bs,be;
	s = query[sqrtQuery[1].second].first;
	e = query[sqrtQuery[1].second].second;

	//첫번째 쿼리에서 미리 갯수 파악해두기
	for (int i = s; i <= e; i++) {
		if (cnt[i] == 0) {
			answer[sqrtQuery[1].second]++;
		}
		cnt[arr[i]]++;
	}

	for (int i = 2; i < M + 1; i++) {
		s = query[sqrtQuery[i].second].first;
		e = query[sqrtQuery[i].second].first;
		bs = query[sqrtQuery[i - 1].second].first;
		be = query[sqrtQuery[i - 1].second].second;
		while (s > bs) { Qsub(arr[bs],answer); ++bs; }
		while (s < bs) { --bs; Qsum(arr[bs], answer); }
		while (e > be) { ++be; Qsum(arr[be], answer); }
		while (e < be) { Qsub(arr[be], answer); ++be; }
	}
	cout << "결과출력" << endl;
	for (int i = 1; i < M + 1; i++) {
		cout << answer[i]<<endl;
	}

	delete sqrtQuery;
	delete answer;
	delete query;
	delete arr;
	return 0;
}