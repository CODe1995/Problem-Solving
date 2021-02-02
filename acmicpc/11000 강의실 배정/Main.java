package boj11000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int T, N, M;

	static class Query implements Comparable<Query>{
		int start;
		int end;

		Query() {}
		Query(int start, int end) {
			this.start = start;
			this.end = end;
		}
		@Override
		public int compareTo(Query target) {
	        return this.start >= target.start ? 1 : - 1;
	    }
		@Override
		public String toString() {
			return start + " " + end;
		}
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		PriorityQueue<Query> pq = new PriorityQueue<>();
		PriorityQueue<Integer> rooms = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(bf.readLine());
			pq.add(new Query(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		
		for(int i =0;i<N;i++) {
			if(!rooms.isEmpty()&&rooms.peek()<=pq.peek().start) {
				rooms.poll();
			}
			rooms.add(pq.poll().end);
		}
		System.out.println(rooms.size());
		/*출력부*/
//		Iterator<Query> iter = pq.iterator();
//		while (iter.hasNext()) {
//			System.out.println(iter.next());
//		}
		
	}
}