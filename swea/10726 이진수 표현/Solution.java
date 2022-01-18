package swea10726;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static String getAnswer(int N, int M) {
		String bin = Integer.toBinaryString(M);
		if (bin.length() < N) {// 자릿수 초과
			return "OFF";
		}
		for(int i = bin.length()-1;i>bin.length()-1-N;i--) {
			if (bin.charAt(i) == '0')
				return "OFF";
		}
		return "ON";
	}

	public static void main(String[] args) throws Exception {
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			System.out.println("#" + (t + 1) + " " + getAnswer(N, M));
		}
	}
}
