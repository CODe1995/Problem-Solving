package swea1868_파핑파핑지뢰찾기;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[][] field;
	static int[][] checkField;
	static boolean[][] visited;
	static final int[][] direction = { { -1, 1 }, { -1, 0 }, { -1, -1 }, { 0, 1 }, { 0, -1 }, { 1, 1 }, { 1, 0 },
			{ 1, -1 } };
	static int N, totalMineCount;

	static int solution() {
		visited = new boolean[N][N];
		int clickCount = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (checkField[i][j] == 0 && !visited[i][j])
					if (searchColumn(j, i))
						clickCount++;
			}
		}
		return clickCount;
	}

	static boolean searchColumn(int x, int y) {
		if (visited[y][x])
			return false;
		visited[y][x] = true;
		if (checkField[y][x] != 0) {
			return false;
		}
		for (int[] dir : direction) {
			int nx = dir[0] + x;
			int ny = dir[1] + y;
			if (isOutField(nx, ny) || visited[ny][nx])
				continue;
			if (checkField[ny][nx] != -1)
				searchColumn(nx, ny);
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			int clickCount = solution();
			int notVisitedCount = findNotVisited();
			System.out.println("#" + tc + " " + (clickCount + notVisitedCount));
		}
	}

	static int findNotVisited() {
		int ret = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j] && checkField[i][j] != -1)
					ret++;
			}
		}
		return ret;
	}

	static void init() throws IOException {
		N = Integer.parseInt(br.readLine());
		field = new char[N][N];
		checkField = new int[N][N];
		totalMineCount = 0;
		for (int i = 0; i < N; i++) {
			field[i] = br.readLine().toCharArray();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (field[i][j] == '*') {
					totalMineCount++;
					checkField[i][j] = -1;
					for (int[] dir : direction) {
						int nx = dir[0] + j;
						int ny = dir[1] + i;
						if (isOutField(nx, ny))
							continue;
						if (field[ny][nx] != '*')
							checkField[ny][nx]++;
					}
				}
			}
		}
	}

	static boolean isOutField(int x, int y) {
		if (x == -1 || y == -1 || x == N || y == N)
			return true;
		return false;
	}
}