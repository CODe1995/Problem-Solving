package swea2930_힙;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;

	static void init() throws IOException {
		sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());		
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			int order = Integer.parseInt(st.nextToken());
			if(order==2) {
				if(pq.isEmpty()) {
					sb.append("-1 ");
				}else {
					sb.append(pq.poll()).append(" ");
				}
			}else if(order==1) {
				int num = Integer.parseInt(st.nextToken());
				pq.add(num);
			}
		}
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			System.out.println("#" + tc + " " + sb.toString());
		}
	}
}