package boj6603;
//10:53~11:06 13mins

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer st;
	static ArrayList<Integer> arr;
	static int[] choice = new int[6];
	static void solve(int start,int depth) {
		if(depth==6) {
			for(int x:choice) {
				sb.append(x).append(" ");
			}
			sb.append("\n");
			return;
		}
		for(int i =start;i<arr.size();i++) {
			choice[depth]=arr.get(i);
			solve(i+1,depth+1);
		}
	}
	public static void main(String[] args) throws IOException{
		while(true) {
			arr = new ArrayList<>();
			st = new StringTokenizer(bf.readLine());
			if(st.countTokens()==1)break;
			while(st.hasMoreTokens())arr.add(Integer.parseInt(st.nextToken()));
			arr.remove(0);
			solve(0,0);
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
