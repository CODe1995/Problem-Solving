package boj6497;
import java.util.*;
import java.io.*;

public class Main_Prim {
	static StringBuilder sb = new StringBuilder();
	static int N,M;
	static boolean visited[];
	static class Edge implements Comparable<Edge>{
		int node,dist;
		public Edge(int node, int dist) {this.node = node;this.dist = dist;}
		@Override
		public int compareTo(Edge o) {			
			return this.dist-o.dist;
		}		
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());//집의수
			N = Integer.parseInt(st.nextToken());//길의수
			if(M==0 && N==0)break;
			visited = new boolean[M];
			ArrayList<ArrayList<Edge>> query = new ArrayList<>();
			for(int i =0;i<M;i++)query.add(new ArrayList<>());
			int totalCost = 0;
			for(int i=0;i<N;i++) {//길의 정보
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());
				totalCost+=d;
				query.get(a).add(new Edge(b,d));
				query.get(b).add(new Edge(a,d));
			}
			PriorityQueue<Edge> pq = new PriorityQueue<>();
			for(Edge cur:query.get(0))
				pq.add(cur);//임의의 정점 0부터 시작한다.
			visited[0]=true;
			int minCost =0;
			while(!pq.isEmpty()) {
				Edge edge = pq.poll();
				if(visited[edge.node])continue;//이미 방문했다면
				visited[edge.node]=true;				
				minCost+=edge.dist;				
				for(Edge next:query.get(edge.node)) {
					pq.add(next);//다음 pq에 추가
				}
			}
			sb.append(totalCost-minCost).append("\n");
		}		
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}