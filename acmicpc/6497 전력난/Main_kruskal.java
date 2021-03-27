package boj6497;
import java.util.*;
import java.io.*;

public class Main_kruskal {
	static StringBuilder sb = new StringBuilder();
	static int N,M,parent[];
	static int getParent(int x) {
		if(parent[x] == x)return x;
		return parent[x] = getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());//집의수
			N = Integer.parseInt(st.nextToken());//길의수
			if(M==0 && N==0)break;
			parent = new int[M];
			for(int i =0;i<M;i++)parent[i]=i;
			class Edge{
				int from,to,dist;
				public Edge(int from, int to, int dist) {this.from = from;this.to = to;this.dist = dist;}			
			}
			ArrayList<Edge> query = new ArrayList<>();
			int total = 0;
			for(int i=0;i<N;i++) {//길의 정보
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());
				total+=d;
				query.add(new Edge(a,b,d));
			}
			Collections.sort(query,(o1,o2)->o1.dist-o2.dist);
			int answer =0;
			for(Edge edge:query) {
				int a = edge.from;
				int b = edge.to;
				if(getParent(a)==getParent(b))continue;
				unionParent(a,b);
				answer+=edge.dist;
			}
			sb.append(total-answer).append("\n");
		}		
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}