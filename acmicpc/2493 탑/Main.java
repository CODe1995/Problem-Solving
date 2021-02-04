package boj2493;

import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb= new StringBuilder();
	static StringTokenizer st;
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		Stack<Integer> stack = new Stack<>();
		int arr[] = new int[N+1];
		int answer[] = new int[N+1];
		st = new StringTokenizer(bf.readLine());
		for(int i =1;i<=N;i++)arr[i]=Integer.parseInt(st.nextToken());
		arr[0]=100000001;
		for(int i =N;i>=0;i--) {
			while(!stack.empty()&&arr[stack.peek()]<arr[i])answer[stack.pop()]=i;
			stack.add(i);
		}
		for(int i=1;i<=N;i++)sb.append(answer[i]).append(" ");
		System.out.println(sb);
	}
}
