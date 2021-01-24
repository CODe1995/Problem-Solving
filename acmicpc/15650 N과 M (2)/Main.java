package boj15650;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static int arr[];
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;	
	public static void dfs(int at,int depth) {
		if(depth==M) {
			for(int x:arr) {
				if(x!=0)
					System.out.print(x+" ");
			}
			System.out.println();
			return;
		}
		for(int i = at;i<=N;i++) {
			arr[depth]=i;
			dfs(i+1,depth+1);
		}
	}
	public static void main(String[] args) throws IOException {		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];		
		dfs(1,0);
	}
}
