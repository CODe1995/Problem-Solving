package boj1874;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(bf.readLine());
		StringBuilder sb = new StringBuilder();
		Stack<Integer> stack = new Stack<>();
		int cur = 0;
		boolean exitflag = false;
		for (int n = 0; n < N; n++) {
			int goal = Integer.parseInt(bf.readLine());
			if (!exitflag) {
				while (cur < goal) {// 수가 증가해야하는경우
					cur++;
					stack.push(cur);
					sb.append('+').append('\n');
				}
				while (!stack.isEmpty() && stack.peek() >= goal) {// 수가 작아져야 하는 경우
					if (stack.peek() == goal) {
						stack.pop();
						sb.append('-').append('\n');
					} else {
						exitflag = true;
						break;
					}
				}
			}
		}
		if(!exitflag)System.out.println(sb);
		else
			System.out.println("NO");
	}
}
