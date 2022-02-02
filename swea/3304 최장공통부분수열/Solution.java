package swea3304_최장공통부분수열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static char[] char1, char2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder(); 
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char1 = ("-"+st.nextToken()).toCharArray();
			char2 = ("-"+st.nextToken()).toCharArray();
			int LCS[][] = new int[char1.length+1][char2.length+1];
			for (int i = 0; i < char1.length; i++) {
				for (int j = 0; j < char2.length; j++) {
					if (i == 0 || j == 0) {
						LCS[i][j] = 0;
					} else if (char1[i] == char2[j]) {
						LCS[i][j] = LCS[i - 1][j - 1] + 1;
					} else {
						LCS[i][j] = Integer.max(LCS[i - 1][j], LCS[i][j - 1]);
					}
				}
			}
			int answer = LCS[char1.length - 1][char2.length - 1];
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
