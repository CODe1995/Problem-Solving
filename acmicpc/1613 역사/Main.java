package boj1613;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();

	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int N = stoi(st.nextToken());
		int K = stoi(st.nextToken());
		int arr[][] = new int[N+1][N+1];
		for(int i=0;i<K;i++) {
			st = new StringTokenizer(br.readLine());
			int a = stoi(st.nextToken());
			int b = stoi(st.nextToken());
			arr[a][b]++;
		}
		for(int k =1;k<=N;k++)
			for(int i =1;i<=N;i++)
				for(int j =1;j<=N;j++) {
					if(arr[i][k]>0 && arr[k][j]>0)
						arr[i][j]++;
				}
		
		int S = stoi(br.readLine());
		for(int i =0;i<S;i++) {
			st = new StringTokenizer(br.readLine());
			int a = stoi(st.nextToken());
			int b = stoi(st.nextToken());
			if(arr[a][b]<arr[b][a]) {//뒷사건이 먼저일어남
				System.out.println(1);
			}
			else if(arr[a][b]>arr[b][a]) {
				System.out.println(-1);
			}
			else System.out.println(0);
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}