package boj20304;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer;
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());//기본 입력
		int M = Integer.parseInt(br.readLine());
		Deque<Integer> dq = new ArrayDeque<Integer>();
		int arr[] = new int[1000001];//최대초기화
		Arrays.fill(arr, Integer.MIN_VALUE);
		st = new StringTokenizer(br.readLine());
		for(int i=1;i<=M;i++) {
			int x =Integer.parseInt(st.nextToken()); 
			arr[x] = 0;
			dq.offerLast(x);
		}//M의 범위 1<=M
		while(!dq.isEmpty()) {
			int x = dq.pollFirst();
			for(int i =0;i<20;i++){				
				int nx = x^(1<<i);
				if(nx>N||arr[nx]!=Integer.MIN_VALUE)continue;
				arr[nx] = arr[x]+1;
				dq.offerLast(nx);
				answer = Math.max(answer, arr[nx]);
			}
		}		
		System.out.println(answer);
	}
}