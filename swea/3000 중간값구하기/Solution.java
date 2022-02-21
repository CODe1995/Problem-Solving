package swea3000_중간값구하기;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static long answer;
	static final int MOD = 20171109;

	static void init() throws IOException {
		answer = 0;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int pivot = Integer.parseInt(st.nextToken());
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();
		maxHeap.add(pivot);
		for (int i = 0; i < N; i++) {
			int mid = maxHeap.peek();
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (mid > a) {
				maxHeap.add(a);
			} else
				minHeap.add(a);
			if (mid > b) {
				maxHeap.add(b);
			} else
				minHeap.add(b);

			if (maxHeap.size() > minHeap.size() + 1) {
				minHeap.add(maxHeap.poll());
			} else if (minHeap.size() > maxHeap.size()) {
				maxHeap.add(minHeap.poll());
			}

			answer = (answer + maxHeap.peek()) % MOD;
		}
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			System.out.println("#" + tc + " " + answer);
		}
	}
}