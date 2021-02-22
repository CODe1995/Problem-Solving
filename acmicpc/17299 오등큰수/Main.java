package boj17299;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int numCount[] = new int[1000001];//최대치
	static int N,arr[];
	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {			
			arr[i] = Integer.parseInt(st.nextToken());
			numCount[arr[i]]++;//입력과 동시에 숫자 갯수를 세어준다.
		}
		Stack<Integer> stack = new Stack<>();//index가 들어간 스택
		int[] answer = new int[N];
		for(int i=0;i<N;i++) {
			while(!stack.isEmpty() && numCount[arr[stack.peek()]]<numCount[arr[i]])
				answer[stack.pop()]=arr[i];
			stack.push(i);			
		}
		for(int i =0;i<N;i++)sb.append(answer[i]==0?-1:answer[i]).append(" ");
		System.out.println(sb);
	}
}