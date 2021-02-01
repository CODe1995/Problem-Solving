package boj1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, M;
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(bf.readLine());
		T = Integer.parseInt(st.nextToken());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(bf.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(bf.readLine());
			PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
			Queue<Integer> indexQ = new LinkedList<>();
			Queue<Integer> valueQ = new LinkedList<>();
			for(int i =0;i<N;i++) {
				int tmp = Integer.parseInt(st.nextToken());
				pq.add(tmp);//우선순위로 정렬
				indexQ.add(i);//index 저장
				valueQ.add(tmp);//값 저장
			}
			int cnt = 0;
			while(true) {
				//우선순위, M(인덱스)와 같다면 정답임.
				if(pq.peek()==valueQ.peek()) {
					if(indexQ.peek()==M) {
						System.out.println(cnt+1);
						break;
					}
					else {
						pq.poll();
						valueQ.poll();
						indexQ.poll();
						cnt++;
					}
				}
				else if(pq.peek() > valueQ.peek()) {//우선 순위가 뒤인가?
					valueQ.add(valueQ.poll());
					indexQ.add(indexQ.poll());
				}
			}
		}
	}
}