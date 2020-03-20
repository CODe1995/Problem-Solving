#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <stdio.h>
#pragma warning(disable:4996)
#define MAX 100001
using namespace std;

int cnt[MAX*10];
pair<int, int>* query;
pair <pair< int, int >, int >* sqrtQuery;
int answer[MAX];
int val = 0;

void Qsub(int numb) {
	if (--cnt[numb] == 0) val--;
}
void Qsum(int numb) {
	if (cnt[numb]++ == 0) val++;
}

int main() {
	int N, M;
	scanf("%d", &N);
	//쿼리가 1부터 시작되기 때문에 1씩 미리 증가해줌(계산하기 편하게끔)
	int* arr = new int[N + 1];
	for (int i = 1; i < N + 1; i++) {
		scanf("%d",&arr[i]);
		//cin >> arr[i];
	}
	//cin >> M;
	scanf("%d",&M);
	//for (int i = 0; i < M + 1; i++) { answer[i] = 0; }
	query = new pair<int, int>[M + 1];
	sqrtQuery = new pair<pair<int, int>, int>[M + 1];
	for (int i = 1; i < M + 1; i++) {
		scanf("%d %d", &query[i].first, &query[i].second);
		//cin >> query[i].first >> query[i].second;
		sqrtQuery[i].first = pair<int, int>(query[i].first / sqrt(N), query[i].second);
		sqrtQuery[i].second = i;//순서가 바뀌어도 i로 순차적 출력을 해줘야함
	}
	sort(sqrtQuery + 1, sqrtQuery + M + 1);

	int s, e, bs, be;
	s = query[sqrtQuery[1].second].first;
	e = query[sqrtQuery[1].second].second;

	//첫번째 쿼리에서 미리 갯수 파악해두기
	for (int i = s; i <= e; i++) {		
		if (cnt[arr[i]] == 0) {
			val++;
		}
		cnt[arr[i]]++;
	}
	answer[sqrtQuery[1].second]=val;

	for (int i = 2; i < M + 1; i++) {
		val = answer[sqrtQuery[i - 1].second];
		int qi = sqrtQuery[i].second;
		s = query[qi].first;
		e = query[qi].second;
		bs = query[sqrtQuery[i - 1].second].first;
		be = query[sqrtQuery[i - 1].second].second;
		while (s > bs) Qsub(arr[bs++]);
		while (s < bs) Qsum(arr[--bs]);
		while (e > be) Qsum(arr[++be]);
		while (e < be) Qsub(arr[be--]);
		answer[qi] = val;
	}
	for (int i = 1; i < M + 1; i++) {
		printf("%d\n",answer[i]);
	}	
	return 0;
}