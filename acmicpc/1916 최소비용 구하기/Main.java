package boj1916;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static ArrayList<ArrayList<Edge>> list;
	static int N;
	static class Edge implements Comparable<Edge>{
		int node,weight;
		public Edge(int node, int weight) {
			this.node = node;
			this.weight = weight;
		}
		@Override
		public int compareTo(Edge o) {			
			return this.weight-o.weight;
		}		
	}
	static int dijkstra(int start,int end) {
		boolean visited[] = new boolean[N+1];
		int dist[] = new int[N+1];		
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start]=0;//자기자신 초기화
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start,0));
		
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			if(visited[cur.node])continue;
			visited[cur.node]=true;
			for(Edge next:list.get(cur.node)) {
				if(dist[next.node]>dist[cur.node]+next.weight) {
					dist[next.node] = dist[cur.node]+next.weight;//작은걸로갱신
					pq.add(new Edge(next.node,dist[next.node]));
				}
			}
		}		
		return dist[end];
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = stoi(br.readLine());//도시의 갯수
		int M = stoi(br.readLine());
		list = new ArrayList<>();
		for(int i =0;i<=N;i++) {
			list.add(new ArrayList<>());
		}		
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int u = stoi(st.nextToken());
			int v = stoi(st.nextToken());
			int w = stoi(st.nextToken());
			list.get(u).add(new Edge(v,w));
		}		
		st = new StringTokenizer(br.readLine());
		int start = stoi(st.nextToken());
		int end = stoi(st.nextToken());
		System.out.println(dijkstra(start,end));		
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}