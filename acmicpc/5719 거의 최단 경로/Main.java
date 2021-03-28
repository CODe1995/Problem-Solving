package boj5719;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int N,M,dist[],S,D;
	static boolean tb[][];
	static ArrayList<ArrayList<Edge>> graph,revGraph;
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
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine());
			N = stoi(st.nextToken());
			M = stoi(st.nextToken());
			if(N==0&&M==0)return;
			graph = new ArrayList<>();
			revGraph = new ArrayList<>();
			tb = new boolean[N][N];
			st = new StringTokenizer(br.readLine());
			S = stoi(st.nextToken());//출발점 
			D = stoi(st.nextToken());//도착점
			for(int i =0;i<N;i++) {
				graph.add(new ArrayList<>());
				revGraph.add(new ArrayList<>());
			}
			for(int i=0;i<M;i++) {
				st = new StringTokenizer(br.readLine());
				int u = stoi(st.nextToken());
				int v = stoi(st.nextToken());
				int p = stoi(st.nextToken());
				graph.get(u).add(new Edge(v,p));
				revGraph.get(v).add(new Edge(u,p));
			}
			dijkstra(S,D);
			traceBack(S,D);
			dijkstra(S,D);
			System.out.println(dist[D]==Integer.MAX_VALUE?-1:dist[D]);
		}
	}
	static void dijkstra(int start,int end) {
//		boolean visited[] = new boolean[N];
		dist = new int[N];		
		int INF = Integer.MAX_VALUE;
		Arrays.fill(dist, INF);
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start,0));
		dist[start]=0;
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			if(cur.weight>dist[cur.node])continue;
//			if(visited[cur.node])continue;
//			visited[cur.node]=true;
			for(Edge edge:graph.get(cur.node)) {
				if(tb[cur.node][edge.node])continue;
//				if(visited[edge.node])continue;
				if (dist[edge.node]>dist[cur.node]+edge.weight) {
					dist[edge.node] = dist[cur.node]+edge.weight;
					pq.add(new Edge(edge.node,dist[cur.node]));
				}
			}
		}
	}
	static void traceBack(int start,int end) {//dist 역추적
		Queue<Integer> q = new LinkedList<>(); 
		boolean visited[] = new boolean[N];
		q.offer(end);
		while(!q.isEmpty()) {
			int cur = q.poll();
			if(cur==start)continue;//시작경로에 도달(역추적 끝)
			if(visited[cur])continue;
			visited[cur]=true;
			
			for(Edge edge:revGraph.get(cur)) {
				if(visited[edge.node])continue;
				if(dist[cur]==dist[edge.node]+edge.weight) {
					tb[edge.node][cur]=true;//반대로써줘야함 prev->cur
					q.offer(edge.node);
				}
			}
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();		
	}
}