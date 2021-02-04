package boj6198;
import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException{
		int N = Integer.parseInt(bf.readLine());
		int[] arr = new int[N];
		Stack<Integer> stack = new Stack<>();
		int[] answer = new int[N];
		for(int i =0;i<N;i++)arr[i]=Integer.parseInt(bf.readLine());
		for(int i =N-1;i>=0;i--) {
			while(!stack.isEmpty()&&arr[stack.peek()]<arr[i])
				answer[i] += answer[stack.pop()]+1;
			stack.add(i);
		}
		long sum =0;
		for(int i=0;i<N;i++)sum+=answer[i];
		System.out.println(sum);
	}
}
