package boj4343;
import java.util.*;
import java.io.*;

public class Main_kruskal {
	static StringBuilder sb = new StringBuilder();
	static int S,P,parent[];
	static class Edge{
		int from,to; double dist;

		public Edge(int from, int to, double dist) {
			super();
			this.from = from;
			this.to = to;
			this.dist = dist;
		}
	}
	static int getParent(int x) {
		if(parent[x]==x)return x;
		return parent[x]=getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a= getParent(a);
		b= getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;		
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int t=0;t<T;t++) {
			st = new StringTokenizer(br.readLine());
			S = stoi(st.nextToken());
			P = stoi(st.nextToken());
			ArrayList<int[]> query = new ArrayList<>();
			parent = new int[P];
			for(int i=0;i<P;i++) {	
				st = new StringTokenizer(br.readLine());
				int a = stoi(st.nextToken());
				int b = stoi(st.nextToken());
				query.add(new int[] {a,b});
			}
			ArrayList<Edge> graph = new ArrayList<>();
			for(int i =0;i<query.size()-1;i++) {
				for(int j =i+1;j<query.size();j++) {
					int x1 = query.get(i)[0];
					int x2 = query.get(j)[0];
					int y1 = query.get(i)[1];
					int y2 = query.get(j)[1];
					double dist = Math.sqrt(Math.pow(Math.abs(x1-x2), 2)+Math.pow(Math.abs(y1-y2), 2));
					graph.add(new Edge(i,j,dist));
				}				
			}
			Collections.sort(graph,(o1,o2)->{
				return o1.dist-o2.dist<0?-1:(o1.dist==o2.dist?0:1);
			});
			double answer =0;
			parent = new int[501];
			for(int i =0;i<501;i++)parent[i]=i;
			int cnt = 0;
			for(Edge edge:graph) {
				if(cnt==P-S)break;
				int a = edge.from;
				int b = edge.to;				
				if(getParent(a)==getParent(b))continue;
				answer=edge.dist;
				unionParent(a,b);
				cnt++;
			}
			System.out.printf("%.2f\n",answer);
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}
