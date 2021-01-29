package boj11399;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	static void solve() throws IOException {
		int N = Integer.parseInt(st.nextToken());
		ArrayList<Integer> arr = new ArrayList<>();
		
		st = new StringTokenizer(bf.readLine());
		for(int i =0; i<N;i++)
			arr.add(Integer.parseInt(st.nextToken()));
		arr.sort(null);
		int answer =0 ;
		int prev =0 ;
		for(int x :arr) {
			answer+=prev+x;
			prev += x;
		}
		System.out.println(answer);
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(bf.readLine());
		sb = new StringBuilder();
		solve();
	}
}
