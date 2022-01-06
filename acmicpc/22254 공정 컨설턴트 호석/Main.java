package boj22254;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, X, present[];

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
		present = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			present[i] = Integer.parseInt(st.nextToken());
		}
	}

	static boolean play(int lineCnt) {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int i = 0; i < lineCnt; i++)
			pq.add(0);
		for (int i = 0; i < N; i++) {
			int curTime = present[i];
			int nextSumTime = pq.poll() + curTime;
			if (nextSumTime > X) {
				return false;
			}
			pq.add(nextSumTime);
		}
		return true;
	}

	static int bisect() {
		// pq를 라인 수만큼 생성
		// pq 중 하나라도 X 값을 넘어가면 라인 늘림
		int left = 0;
		int right = N;
		int mid = (left + right) / 2;		
		while (left < right) {
			if(play(mid)) {
				right-=1;
			}else {
				left+=1;
			}
			mid = (left + right) / 2;
		}
		return mid;
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(bisect());
	}
}