package boj1647;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,parent[];
	static PriorityQueue<Node> pq = new PriorityQueue<>();
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
		return parent[x] = getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	public static void main(String[] args) throws IOException {		
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		M = stoi(st.nextToken());
		parent=new int[N+1];
		for(int i=1;i<=N;i++)parent[i]=i;
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			pq.add(new Node(stoi(st.nextToken()),stoi(st.nextToken()),stoi(st.nextToken())));
		}
		int answer = 0;
		int lastLength = 0;
		while(!pq.isEmpty()) {
			Node cur = pq.poll();
			if(getParent(cur.s)==getParent(cur.e))continue;
			int s = cur.s;
			int e = cur.e;
			unionParent(s,e);
			answer+=cur.l;
			lastLength = cur.l;//최대길이 간선
		}
		System.out.println(answer-lastLength);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}