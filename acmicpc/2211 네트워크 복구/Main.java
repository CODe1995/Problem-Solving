package boj2211;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int N,M,dist[],answer[][];
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
		boolean visited[] = new boolean[N+1];
		dist = new int[N+1];
		answer = new int[N+1][];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start]=0;
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start,0));
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			if(visited[cur.node])continue;
			visited[cur.node]=true;
			for(Edge next:list.get(cur.node)) {
				if(dist[next.node]>dist[cur.node]+next.weight) {
					dist[next.node] = dist[cur.node]+next.weight;
					answer[next.node] = new int[] {next.node,cur.node};
					pq.add(new Edge(next.node,dist[next.node]));
				}
			}
		}
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		M = stoi(st.nextToken());
		list = new ArrayList<>();
		for(int i =0;i<=N;i++)list.add(new ArrayList<>());
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int u = stoi(st.nextToken());
			int v = stoi(st.nextToken());
			int w = stoi(st.nextToken());
			list.get(u).add(new Edge(v,w));
			list.get(v).add(new Edge(u,w));
		}
		dijkstra(1);
		sb.append(answer.length-2).append("\n");
		for(int i =2;i<answer.length;i++)
			sb.append(answer[i][0]).append(" ").append(answer[i][1]).append("\n");
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}