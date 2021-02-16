package boj1946;

import java.util.*;
import java.io.*;

public class Main_시간단축 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int answer=N, min = Integer.MAX_VALUE;
			int[] list = new int[N+1];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				list[a]=b;
			}
			for(int i =1;i<=N;i++) {
				if(list[i]<min) {
					min = list[i];
				}
				else {
					answer--;
				}
			}
			System.out.println(answer);
		}
	}
}