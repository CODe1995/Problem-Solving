package boj1715;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static PriorityQueue<Integer> pq = new PriorityQueue<>();
	public static void main(String[] args) throws IOException{
		N = Integer.parseInt(bf.readLine());
		for(int i =0;i<N;i++)pq.add(Integer.parseInt(bf.readLine()));
		int answer =0 ;
		while(pq.size()>1) {
			int tmp = pq.poll()+pq.poll();
			answer+=tmp;
			pq.add(tmp);
		}
		System.out.println(answer);
	}
	public static void stn() throws IOException{
		st = new StringTokenizer(bf.readLine());
	}
}
