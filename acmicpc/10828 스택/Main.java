package boj10828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {	
	static int N;
	static Stack<Integer> stack = new Stack<>();
	static BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		for(int n = 0;n<N;n++) {
			st = new StringTokenizer(bf.readLine());
			String cmd = st.nextToken();
			switch(cmd) {
			case "push":
				stack.push(Integer.parseInt(st.nextToken()));
				break;
			case "top":
				if(!stack.isEmpty())System.out.println(stack.peek());
				else System.out.println(-1);break;
			case "size":
				System.out.println(stack.size());break;
			case "pop":
				if(stack.size()>0)
					System.out.println(stack.pop());
				else System.out.println(-1);
				break;
			case "empty":
				if(stack.isEmpty())System.out.println(1);
				else System.out.println(0);break;				
			}
		}
	}
}
