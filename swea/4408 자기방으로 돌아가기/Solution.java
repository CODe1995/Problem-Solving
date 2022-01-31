package swea4408_자기방으로돌아가기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int[] hallway;
	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine().trim());
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= T; testCase++) {
			int studentNum = Integer.parseInt(br.readLine().trim());
			hallway = new int[400];
			for (int i = 0; i < studentNum; i++) {
				st = new StringTokenizer(br.readLine().trim());
				int src = (Integer.parseInt(st.nextToken())-1)/2;
				int dest = (Integer.parseInt(st.nextToken())-1)/2;
				if (dest < src) {
					int tmp = dest;
					dest = src;
					src = tmp;
				}
				for (int j = src; j <= dest; j++) {
					hallway[j] += 1;
				}
			}
			int max = 0;
			for (int i = 0; i < 400; i++) {
				max = Integer.max(hallway[i], max);
			}
			sb.append("#").append(testCase).append(" ").append(max).append("\n");
		}
		System.out.println(sb);
	}
}
