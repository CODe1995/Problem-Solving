package boj11062;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int T, N, cards[], dp[][];

	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		cards = new int[N];
		for (int i = 0; i < N; i++)
			cards[i] = Integer.parseInt(st.nextToken());
		dp = new int[N + 1][N + 1];
	}

	static int play(int left, int right, int turn) {
		if (left > right)
			return 0;
		if (dp[left][right] > 0)
			return dp[left][right];
		if (turn % 2 == 0)
			return dp[left][right] = Math.max(cards[left] + play(left + 1, right, turn + 1),
					cards[right] + play(left, right - 1, turn + 1));
		else
			return dp[left][right] = Math.min(play(left + 1, right, turn + 1), play(left, right - 1, turn + 1));
	}

	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());		
		for (int t = 0; t < T; t++) {
			input();
			sb.append(play(0, N-1, 0));
			sb.append('\n');
		}
		System.out.println(sb);
	}
}