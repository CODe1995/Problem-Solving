package boj2346;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static class Pos{
		int value,index;
		Pos(int value,int index){
			this.value = value;
			this.index = index;
		}
	}
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(bf.readLine());
		Deque<Pos> arr = new ArrayDeque<Main.Pos>();
		for(int i =0;i<N;i++)arr.add(new Pos(Integer.parseInt(st.nextToken()),i+1));		
		while(!arr.isEmpty()) {
			sb.append(arr.peek().index).append(" ");
			int cur = arr.pollFirst().value;
			if(arr.isEmpty()) { break;}
			if(cur<0) for(int i =0;i<-cur;i++)arr.addFirst(arr.pollLast());//이동 방향이 음수 = 왼쪽
			else for(int i=0;i<cur-1;i++) arr.addLast(arr.pollFirst());
		}
		System.out.println(sb);
	}
}
