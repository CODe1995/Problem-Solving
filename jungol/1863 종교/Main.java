package jungol1863;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,rank[],parent[];
	static int getParent(int x) {
		if(x == parent[x])return x;
		return parent[x] = getParent(parent[x]);
	}
	static void union(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a==b)return;		
		if(rank[a]>rank[b]) {
			parent[b]=a;
		}else {
			parent[a]=b;
			if(rank[a]==rank[b])rank[b]++;
		}		
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		parent = new int[N+1];
		rank = new int[N+1];
		int answer = 0;
		for(int i=1;i<=N;i++)parent[i]=i;
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if(getParent(a)==getParent(b))continue;
			union(a,b);
			answer++;
		}
		System.out.println(N-answer);
	}
}