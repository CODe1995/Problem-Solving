package boj15649;
///https://st-lab.tistory.com/114

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static int N,M;
	public static int[] arr;
	public static boolean[] visit;
	public static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N];
		visit = new boolean[N];
		
		dfs(0);
		System.out.println(sb);
	}
	
	public static void dfs(int depth) {
		if(depth == M) {//최대 깊이까지 도달했다면
			for(int val:arr) {
				if(val!=0)
					sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}
		for( int i =0;i<N;i++) {
			if(!visit[i]) {
				visit[i]=true;
				arr[depth]=i+1;
				dfs(depth+1);
				visit[i]=false;
			}
		}
	}
}
