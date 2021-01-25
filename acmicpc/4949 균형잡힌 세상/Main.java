package boj4949;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static String ch;
	public static void main(String[] args) throws IOException {
		while (true) {	
			Stack<Character> stack = new Stack<>();
			boolean exitflag = false;			
			while(!exitflag) {
				ch = bf.readLine();				
				if(ch.length()==1 && ch.charAt(0)=='.')return;
				for(int i =0;i<ch.length() && !exitflag;i++) {
					if(ch.charAt(i)=='.') {
						exitflag=true;
						if(stack.size()==0)
							System.out.println("yes");
						else
							System.out.println("no");
					}
					else if(ch.charAt(i)=='(')stack.push('(');
					else if(ch.charAt(i)=='[')stack.push('[');
					else if(ch.charAt(i)==')') {
						if(!stack.isEmpty()&&stack.peek()=='(')stack.pop();
						else { exitflag=true;System.out.println("no");}
					}
					else if(ch.charAt(i)==']') {
						if(!stack.isEmpty()&&stack.peek()=='[')stack.pop();
						else { exitflag=true;System.out.println("no");}
					}
				}
			}
			
		}
	}
}
