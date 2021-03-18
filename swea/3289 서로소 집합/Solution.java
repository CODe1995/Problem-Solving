package swea3289;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M;
	static int parent[] = new int[1000001];
	static int getParent(int x) {
		if(x==parent[x])return x;
		return parent[x] = getParent(parent[x]);
	}
	static void union(int a,int b) {
		a = getParent(a);
		b = getParent(b);		
		if(a<b)parent[b]=a;
		else if(b<a) parent[a]=b;
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	static String snt() {
		return st.nextToken();
	}
	public static void main(String[] args) throws IOException {
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			sb.append("#").append(t).append(" ");
			st = new StringTokenizer(br.readLine());
			N = stoi(snt());
			M = stoi(snt());
			for(int i =1;i<=N;i++) parent[i]=i;			
			for(int i =0;i<M;i++) {
				st = new StringTokenizer(br.readLine());
				int num = stoi(snt());
				int a = stoi(snt());
				int b = stoi(snt());	
				if(num==0) union(a,b);
				else {//1
					if(getParent(a)==getParent(b))sb.append(1);
					else sb.append(0);
				}					
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}