package boj10845;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int N;
	public static void main(String[] args) throws IOException{
		Queue<Integer> q = new LinkedList<>();
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(bf.readLine());
			String order = st.nextToken();
			switch(order) {
			case "push":
				q.add(Integer.parseInt(st.nextToken()));
				break;
			case "front":
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.peek()).append("\n");;
				break;
			case "back":
				int tmp=-1;
				Iterator<Integer> iter = q.iterator();
				while(iter.hasNext())tmp=iter.next();				
				sb.append(tmp).append("\n");
				break;
			case "empty":
				if(q.isEmpty())sb.append(1).append("\n");
				else sb.append(0).append("\n");
				break;
			case "pop":
				if(q.isEmpty())sb.append(-1).append("\n");
				else sb.append(q.poll()).append("\n");
				break;			
			case "size":
				sb.append(q.size()).append("\n");
				break;					
			}
		}
		System.out.println(sb);
	}
}
