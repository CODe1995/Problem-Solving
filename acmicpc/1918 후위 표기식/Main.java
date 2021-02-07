package boj1918;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static HashMap<Character, Integer> prio = new HashMap<>();
	static void solution() {

	}

	public static void main(String[] args) throws IOException {
		String str = br.readLine();
		prio.put('(', 1);//우선순위
		prio.put(')', 1);
		prio.put('+', 2);
		prio.put('-', 2);
		prio.put('*', 3);
		prio.put('/', 3);
		
		Stack<Character> stack = new Stack<>();
		for(int i =0;i<str.length();i++) {
			char x = str.charAt(i);
			//숫자인경우
			if(prio.get(x)==null) {
				sb.append(x);
			}else {//연산자인경우
				if(x==')') {//닫는 괄호나오면
					while(!stack.isEmpty()&&stack.peek()!='(') {//여는괄호까지 pop
						sb.append(stack.pop());
					}
					stack.pop();//여는 괄호도 pop 출력X
				}
				else {//나머지 연산자라면 우선순위 비교
					while(!stack.isEmpty()&&x!='('&&prio.get(x)<=prio.get(stack.peek())) {//스택에 있는게 우선순위 더 높다면?
						sb.append(stack.pop());
					}
					stack.add(x);//들고있던건 스택에 넣어주기					
				}
			}
		}
		while(!stack.isEmpty()) {
			sb.append(stack.pop());
		}
		System.out.println(sb);
	}
}