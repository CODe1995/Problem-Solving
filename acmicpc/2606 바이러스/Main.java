package boj2606;

import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(bf.readLine());
		int M = Integer.parseInt(st.nextToken());
		int graph[][] = new int[N+1][N+1];
		for(int i=0;i<M;i++){
			st = new StringTokenizer(bf.readLine());
			int a =Integer.parseInt(st.nextToken());
			int b =Integer.parseInt(st.nextToken());
			graph[a][b]=1;
			graph[b][a]=1;
		}
		Deque<Integer> dq = new ArrayDeque<Integer>();
		dq.add(1);
		int check[] = new int[N+1];
		int answer =0;check[1]=1;
		while(!dq.isEmpty()) {
			int x= dq.pollFirst();
			answer++;
			for(int i =1;i<=N;i++) {
				if(graph[x][i]==1 && check[i]==0) {dq.add(i);check[i]=1;}
			}
		}
		System.out.println(answer-1);
	}
}
