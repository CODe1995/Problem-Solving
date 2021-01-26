package boj4889;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		int t = 1;
		while(true) {
			String input = bf.readLine();
			if(input.contains("-")) {return;}
			Stack<Character> stack = new Stack<>();
			for(int i =0;i<input.length();i++) {
				char c = input.charAt(i);
				if(!stack.isEmpty()&&i!=0) {
					if(stack.peek()=='{'&&c=='}')
						stack.pop();
					else stack.push(c);
				}else {stack.push(c);}
			}
			int answer= 0;
			for(int i =stack.size()-1;i>=0;i-=2) {
				char b = stack.elementAt(i);//뒤
				char a = stack.elementAt(i-1);//앞
				if(a=='{'&&b=='{') {
					answer+=1;
				}
				else if(a=='}'&&b=='{') {
					answer+=2;
				}
				else if(a=='}'&&b=='}') {
					answer+=1;
				}
				stack.pop();stack.pop();
				if(stack.isEmpty())break;
			}
			System.out.println(t+". "+answer);			
			t++;
		}
		
	}
}
