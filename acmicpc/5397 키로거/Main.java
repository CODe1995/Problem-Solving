package boj5397;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb;
	static int T;
	public static void solution() throws IOException{
		sb = new StringBuilder();
		String input = bf.readLine();
		Deque<Character> mainq = new ArrayDeque<>();
		Deque<Character> subq = new ArrayDeque<>();
		for(int i =0; i<input.length();i++) {
			char c = input.charAt(i);
			switch(c) {
			case '<':
				if(!mainq.isEmpty())subq.addFirst(mainq.pollLast());					
				break;			
			case '>':
				if(!subq.isEmpty())mainq.add(subq.pollFirst());		
				break;
			case '-':
				if(!mainq.isEmpty())mainq.pollLast();
				break;
			default:
				mainq.add(c);
				break;				
			}
		}
		while(!mainq.isEmpty())sb.append(mainq.pollFirst());
		while(!subq.isEmpty())sb.append(subq.pollFirst());		
		System.out.println(sb);
	}
	public static void main(String[] args) throws IOException{
		T = Integer.parseInt(bf.readLine());
		for(int t=1;t<=T;t++) {
			solution();
		}
	}
}
