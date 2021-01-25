package boj10773;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int K;
	static Stack<Integer> stack = new Stack<>();
	static BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(bf.readLine());
		K = Integer.parseInt(st.nextToken());
		for(int k=0;k<K;k++) {
			st = new StringTokenizer(bf.readLine());
			int t = Integer.parseInt(st.nextToken());
			if (t==0)stack.pop();
			else stack.push(t);
		}
		long sum=0;
		for(int i =0;i<stack.size();i++) {
			sum += stack.elementAt(i);
		}
		
		System.out.println(sum);	
	}
}
