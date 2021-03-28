package boj2458;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();

	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int N = stoi(st.nextToken());
		int M = stoi(st.nextToken());
		int arr[][] = new int[N+1][N+1];
		for(int i =0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = stoi(st.nextToken());
			int b = stoi(st.nextToken());
			arr[a][b]=1;
		}
		
		for(int k=1;k<=N;k++)
			for(int i=1;i<=N;i++)
				for(int j=1;j<=N;j++) {
					if(arr[i][k]>0 && arr[k][j]>0)
						arr[i][j]=1;
				}
		int answer = 0;
		for(int i=1;i<=N;i++) {
			for(int j=1;j<=N;j++) {
				if(i==j)continue;
				if(arr[i][j]==0 && arr[j][i]==0) {
					answer--;
					break;
				}
			}
			answer++;
		}
		System.out.println(answer);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
	}
}