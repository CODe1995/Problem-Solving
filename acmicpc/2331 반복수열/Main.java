package boj2331;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		HashMap<Integer, Integer> visited = new HashMap<>();		
		int n = N;
		visited.put(n,1);
		while(true) {
			int newnum = 0; 
			while(n>0) {
				newnum+= Math.pow(n%10,P);
				n/=10;
			}
			n = newnum;
			if(visited.containsKey(newnum)) {
				if(visited.get(newnum)>=2)break;
				visited.put(newnum, visited.get(newnum)+1);
			}
			else	visited.put(newnum, 1);
		}
		int answer = 0;
		for(int key:visited.keySet()) {
			if(visited.get(key)==1) {
				answer++;
			}
		}
		System.out.println(answer);
	}
}