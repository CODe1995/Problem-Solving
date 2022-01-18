package swea1288;

import java.util.*;
import java.io.*;

public class Solution {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int getAnswer(int originN) {
		int n = originN;
		int visited = 0;
		int mul = 1;
		int goal = 0;
		for (int i = 0; i <= 9; i++) {
			goal += 1 << i;
		}
		while (visited != goal) {
			String tmp = String.valueOf(n);
			for (int i = 0; i < tmp.length(); i++) {
				int ca = Integer.parseInt(String.valueOf(tmp.charAt(i)));
				visited |= 1<<(ca);				
			}
			if(visited == goal)
				break;
			n = originN * ++mul;
		}
		return n;
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			sb.append("#").append(t+1).append(" ")
				.append(getAnswer((Integer.parseInt(br.readLine())))).append("\n");
		}
		System.out.println(sb);
	}
}