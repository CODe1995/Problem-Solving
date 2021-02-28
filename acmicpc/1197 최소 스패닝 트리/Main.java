package boj1197;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int V,E;
	static PriorityQueue<Node> pq = new PriorityQueue<>();
	static int parent[];
	static class Node implements Comparable<Node>{
		int s,e,l;		
		public Node(int s, int e, int l) {this.s = s;this.e = e;this.l = l;}
		@Override
		public int compareTo(Node o) {			
			return this.l-o.l;
		}		
	}
	static int getParent(int x) {
		if(parent[x]==x)return x;		
		return parent[x]=getParent(parent[x]);
	}
	
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		V = stoi(st.nextToken());
		E = stoi(st.nextToken());		
		for(int i =0;i<E;i++) {
			st = new StringTokenizer(br.readLine());
			int s = stoi(st.nextToken());
			int e = stoi(st.nextToken());
			int l = stoi(st.nextToken());
			pq.add(new Node(s,e,l));
		}
		parent = new int[V+1];
		for(int i =1;i<=V;i++)parent[i]=i;//init 자기자신이 부모
		int answer = 0;
		for(int i =0;i<E;i++) {
			Node cur = pq.poll();
			int s = cur.s;
			int e = cur.e;
			int sp = getParent(s);
			int ep = getParent(e);
			if(sp==ep)continue;//부모가 같다면 이미 이어졌다는 것
			unionParent(s,e);
			answer += cur.l;
		}
		System.out.println(answer);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}