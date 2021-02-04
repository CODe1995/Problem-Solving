package boj17298;

import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(bf.readLine());
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(bf.readLine());
		Stack<Integer> stack = new Stack<>();
		int []answer = new int[N];//정답 담김
		int []arr = new int[N];//입력들어감
		for(int i=0;i<N;i++)arr[i] = Integer.parseInt(st.nextToken());
		for(int i =0;i<N;i++) {
			while(!stack.isEmpty()&& arr[stack.peek()] < arr[i])
				answer[stack.pop()]=arr[i];			
			stack.push(i);			
		}
		for(int i =0;i<N;i++)
			sb.append(answer[i]==0?-1:answer[i]).append(" ");
		System.out.println(sb);		
	}
}