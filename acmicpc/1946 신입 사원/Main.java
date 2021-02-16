package boj1946;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int N = Integer.parseInt(br.readLine());
			int answer=N, min = Integer.MAX_VALUE;
			ArrayList<int[]> list = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				list.add(new int[] { a, b});
			}
			Collections.sort(list,new Comparator<int[]>() {
				@Override
				public int compare(int a[],int b[]) {					
					return a[0]-b[0];	
				}
			});
			for(int i =0;i<N;i++) {
				if(list.get(i)[1]<min) {
					min = list.get(i)[1];
				}
				else {
					answer--;
				}
			}
			System.out.println(answer);
		}
	}
}