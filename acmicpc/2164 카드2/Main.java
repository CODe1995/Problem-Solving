package boj2164;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static int N;
	public static void main(String[] args) throws IOException{
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		Queue<Integer> q = new LinkedList<Integer>();
		for(int i =0;i<N;i++)q.add(i+1);
		while(q.size()>1) {q.poll();q.add(q.poll());}
		System.out.println(q.poll());
	}

}
