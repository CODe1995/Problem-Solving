package boj18428;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, direction[][] = new int[][] { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };
	static boolean answer;
	static char[][] field;

	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		field = new char[N][N];
		answer = false;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++)
				field[i][j] = st.nextToken().charAt(0);
		}
	}

	static boolean canFindStudent() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (field[i][j] == 'T') {
					for (int dir[] : direction) {
						int nx = j;
						int ny = i;
						while (true) {
							nx += dir[0];
							ny += dir[1];
							if (0 > nx || 0 > ny || N <= nx || N <= ny)
								break;
							if (field[ny][nx] == 'O' || field[ny][nx] == 'T')
								break;
							if (field[ny][nx] == 'S')
								return true;
						}
					}
				}
			}
		}
		return false;
	}

	static void permutation(int depth, int index) {
		if (answer)
			return;
		if (depth == 3) {
			if (!canFindStudent()) {
				answer = true;
			}
			return;
		}
		for (int i = index + 1; i < N * N; i++) {
			int x = i % N;
			int y = i / N;
			if (field[y][x] != 'X')
				continue;
			field[y][x] = 'O';
			permutation(depth + 1, i);
			field[y][x] = 'X';
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		permutation(0, 0);
		System.out.println(answer ? "YES" : "NO");
	}
}