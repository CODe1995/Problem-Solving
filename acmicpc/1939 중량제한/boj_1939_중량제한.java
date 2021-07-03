import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj_1939_중량제한 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M;
	static int parent[];
	static ArrayList<Node> graph = new ArrayList<>();
	static class Node implements Comparable<Node>{
		int from,to;
		long dist;
		
		public Node(int from, int to, long dist) {
			super();
			this.from = from;
			this.to = to;
			this.dist = dist;
		}

		@Override
		public int compareTo(Node o) {
			if(this.dist==o.dist)return 0;
			if(this.dist<o.dist)return 1;//무게 큰게 앞으로
			return -1;
		}
	}
	public static int getParent(int x) {
		if(x==parent[x])return x;
		return parent[x] = getParent(parent[x]);
	}
	public static void unionParent(int a,int b) {
		a= getParent(a);
		b= getParent(b);
		if(a==b)return;
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	public static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		parent = new int[N+1];
		for(int i =0;i<N+1;i++)parent[i]=i;
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a,b;
			long d;
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			d = Long.parseLong(st.nextToken());
			graph.add(new Node(a,b,d));
		}
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		dijkstra(start, end);
	}
	public static void dijkstra(int start,int end) {
		Collections.sort(graph);
		for(Node cur:graph) {
			unionParent(getParent(cur.from),getParent(cur.to));
			if(getParent(start)==getParent(end)) {//이어지는 순간
				System.out.println(cur.dist);
				break;
			}
		}
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}
