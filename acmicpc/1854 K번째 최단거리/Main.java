package boj1854;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int N,M,K;
	static ArrayList<ArrayList<Edge>> list;
	static PriorityQueue<Integer> answer[];
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
		answer = new PriorityQueue[N+1];		
		for(int i =0;i<=N;i++)answer[i]=new PriorityQueue<>(Collections.reverseOrder());
		answer[start].add(0);
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(start,0));
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			for(Edge edge:list.get(cur.node)) {
				int nextNode = edge.node;
				int nextWeight = edge.weight+cur.weight;
				
				if(answer[nextNode].size()<K) {
					answer[nextNode].add(nextWeight);
					pq.add(new Edge(nextNode,nextWeight));
				}
				else if(answer[nextNode].peek() > nextWeight) {//가장 큰 수
					answer[nextNode].poll();
					answer[nextNode].add(nextWeight);
					pq.add(new Edge(nextNode,nextWeight));
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
		K = stoi(st.nextToken());
		list = new ArrayList<>();
		for(int i =0;i<=N;i++)list.add(new ArrayList<>());
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			list.get(stoi(st.nextToken())).add(new Edge(stoi(st.nextToken()),stoi(st.nextToken())));
		}
		dijkstra(1);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);				
	}
	public static void main(String[] args) throws IOException {
		input();
		for(int i = 1;i<=N;i++) {
			if(answer[i].size()<K) {sb.append(-1).append("\n");}
			else {sb.append(answer[i].peek()).append("\n");}
		}
		System.out.print(sb);
	}
}