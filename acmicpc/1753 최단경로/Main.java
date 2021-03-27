package boj1753;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int V,E,dist[];
	static ArrayList<ArrayList<Edge>> list;
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
	static void dijkstra(int start) {
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		boolean[] visited = new boolean[V+1];
		pq.add(new Edge(start,0));//초기		
		dist[start]=0;
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			if(visited[cur.node])continue;
			visited[cur.node]=true;
			for(Edge edge:list.get(cur.node)) {
				if(dist[edge.node] > dist[cur.node]+edge.weight) {
					dist[edge.node] = dist[cur.node] + edge.weight;
					pq.add(new Edge(edge.node,dist[edge.node]));
				}
			}				
		}
	}
	static void input() throws IOException {
		int INF = Integer.MAX_VALUE;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		V = stoi(st.nextToken());
		E = stoi(st.nextToken());
		int start = stoi(br.readLine());//시작정점
		list = new ArrayList<>();
		dist = new int[V+1];
		Arrays.fill(dist, INF);//무한대로갱신
		for(int i=0;i<=V+1;i++) {
			list.add(new ArrayList<>());
		}
		
		for(int i=0;i<E;i++) {
			st = new StringTokenizer(br.readLine());
			int u = stoi(st.nextToken());//from
			int v = stoi(st.nextToken());//to
			int w = stoi(st.nextToken());//weight
			list.get(u).add(new Edge(v,w));
		}
		dijkstra(start);		
		for(int i =1; i<dist.length;i++) {
			sb.append(dist[i]==Integer.MAX_VALUE?"INF":dist[i]).append("\n");
		}		
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}