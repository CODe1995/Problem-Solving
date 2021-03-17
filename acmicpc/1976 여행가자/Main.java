package boj1976;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M;
	static int parent[];
	static int getParent(int x) {
		if(x==parent[x])return x;
		return parent[x] = getParent(parent[x]);
	}
	static void union(int a,int b) {
		a = getParent(a);
		b = getParent(b);		
		if(a<b)parent[b]=a;
		else if(a>b) parent[a]=b;
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		parent = new int[N+1];
		for(int i =1;i<=N;i++)parent[i]=i;
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++) {
				int x = Integer.parseInt(st.nextToken());
				if(x==1) {
					union(i+1,j+1);
				}
			}
		}
		int prev= -1;
		boolean answer = true;
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<M;i++) {
			int x = Integer.parseInt(st.nextToken());
			if(prev==-1) {
				prev = getParent(x);
				continue;
			}
			if(prev!=getParent(x)) {
				answer = false;
				break;
			}
			prev = getParent(x);
		}
		System.out.println(Arrays.toString(parent));
		System.out.println(answer?"YES":"NO");
	}
}