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
		int startPoint = 0;
		for (int i = 0; i < lineCnt; i++) {
			pq.add(present[i]);
			startPoint = i;
		}
		for (int i = startPoint+1; i < N; i++) {
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
		int left = 1;
		int right = N;
		int mid = -1;		
		while (left <= right) {
			mid = (left + right) / 2;
			if(play(mid)) {
				right=mid-1;
			}else {
				left=mid+1;
			}
		}
		return right+1;
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(bisect());
	}
}