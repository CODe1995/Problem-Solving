package swea7091_은기의아주큰그림;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer, H, W, N, M, patternHash, mapHash;
	static int[][] pattern, map, mapRowHash, mapColHash;
	static int[] patternRowHash;
	static final int ROW_MOD = 10007, COL_MOD = 10009;

	static void init() throws IOException {
		answer = 0;
		st = new StringTokenizer(br.readLine());
		H = Integer.parseInt(st.nextToken());
		W = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		pattern = new int[H][W];
		map = new int[N][M];
		patternRowHash = new int[H];
		mapRowHash = new int[N][M];
		mapColHash = new int[N][M];
		patternHash = 0;
		mapHash = 0;

		for (int i = 0; i < H; i++) {
			char[] c = br.readLine().toCharArray();
			for (int j = 0; j < W; j++) {
				pattern[i][j] = c[j] == 'o' ? 1 : 0;
			}
		}
		for (int i = 0; i < N; i++) {
			char[] c = br.readLine().toCharArray();
			for (int j = 0; j < M; j++) {
				map[i][j] = c[j] == 'o' ? 1 : 0;
			}
		}
		getPatternHash();
		getMapHash();
	}

	static void getPatternHash() {
		int power = 1;
		for (int i = 0; i < H; i++) {
			power = 1;
			for (int j = 0; j < W; j++) {
				patternRowHash[i] += pattern[i][W - j - 1] * power;
				power *= ROW_MOD;
			}
		}
		power = 1;
		for (int i = 0; i < H; i++) {
			patternHash += patternRowHash[H - 1 - i] * power;
			if (i < H - 1)
				power *= COL_MOD;
		}
	}

	static void getMapHash() {
		int power = 1;
		for (int i = 0; i < N; i++) {
			power = 1;
			for (int j = 0; j < W; j++) {
				mapRowHash[i][0] += map[i][W - 1 - j] * power;
				if (j < W - 1)
					power *= ROW_MOD;
			}
			for (int j = 1; j <= M - W; j++) {
				mapRowHash[i][j] = (mapRowHash[i][j - 1] - map[i][j - 1] * power) * ROW_MOD + map[i][j + W - 1];
			}
		}
		for (int j = 0; j <= M - W; j++) {
			power = 1;
			for (int i = 0; i < H; i++) {
				mapColHash[0][j] += mapRowHash[H - i - 1][j] * power;
				if (i < H - 1)
					power *= COL_MOD;
			}
			if (patternHash == mapColHash[0][j]) {
				answer++;
			}
			for (int i = 1; i <= N - H; i++) {
				mapColHash[i][j] = (mapColHash[i - 1][j] - mapRowHash[i - 1][j] * power) * COL_MOD
						+ mapRowHash[H + i - 1][j];
				if (patternHash == mapColHash[i][j]) {
					answer++;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			System.out.println("#" + tc + " " + answer);
		}
	}
}