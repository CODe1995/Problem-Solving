package boj1806;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static void solution() {

	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int arr[] = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++)arr[i]=Integer.parseInt(st.nextToken());
		int s =0;
		int e = 0;
		int sum = 0;
		int answer = Integer.MAX_VALUE;
		while(true) {			
			if(sum>=S) {
				answer = Math.min(e-s, answer);
				sum-=arr[s++];//넣었던 수 빼주고
			}
			else {
				if(e==N)break;
				sum+=arr[e++];//다음 수 넣어주고
			}
		}
		System.out.println(answer==Integer.MAX_VALUE?0:answer);
	}
}