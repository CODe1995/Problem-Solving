package swea1244_최대상금;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	static int answer;
	static int changeCount;
	static char[] number;

	private static void swap(int src, int dest) {
		char temp = number[src];
		number[src] = number[dest];
		number[dest] = temp;
	}

	private static void swapNumber(int depth, int index) {
		if (depth == changeCount) {
			int result = Integer.parseInt(new String(number));
			answer = Integer.max(answer, result);
			return;
		}
		for (int i = index; i < number.length - 1; i++) {
			for (int j = i + 1; j < number.length; j++) {
				swap(i, j);
				swapNumber(depth + 1, i);
				swap(j, i);
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuffer sb = new StringBuffer();
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			number = st.nextToken().toCharArray();
			answer = 0;
			changeCount = Integer.parseInt(st.nextToken());
			swapNumber(0, 0);
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
