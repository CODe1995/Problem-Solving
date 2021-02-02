package boj10866;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int N;
	public static void main(String[] args) throws IOException{
		Deque<Integer> q = new ArrayDeque<>();
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(bf.readLine());
			String order = st.nextToken();
			switch(order) {
			case "push_back":
				q.addLast(Integer.parseInt(st.nextToken()));
				break;
			case "push_front":
				q.addFirst(Integer.parseInt(st.nextToken()));
				break;
			case "front":
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.peekFirst()).append("\n");;
				break;
			case "back":			
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.peekLast()).append("\n");;
				break;
			case "empty":
				if(q.isEmpty())sb.append(1).append("\n");
				else sb.append(0).append("\n");
				break;
			case "pop_front":
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.pollFirst()).append("\n");
				break;			
			case "pop_back":
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.pollLast()).append("\n");
				break;			
			case "size":
				sb.append(q.size()).append("\n");
				break;					
			}
		}
		System.out.println(sb);
	}
}