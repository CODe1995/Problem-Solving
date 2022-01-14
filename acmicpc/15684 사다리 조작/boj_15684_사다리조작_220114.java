package boj15684;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, H, field[][], answer;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 가로
		M = Integer.parseInt(st.nextToken()); // 짝대기 갯수
		H = Integer.parseInt(st.nextToken()); // 높이
		field = new int[H][N];
		answer = 4;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int y = Integer.parseInt(st.nextToken()) - 1;
			int x = Integer.parseInt(st.nextToken()) - 1;
			field[y][x] = 1;
		}
	}

	static boolean isSuccess() {
		for (int i = 0; i < N; i++) {
			boolean used = false;
			int nx = i;
			int ny = 0;
			while (true) {
				if (ny == H) {// 끝에 도달
					if (nx == i)// 성공
						break;
					else
						return false; // 불가
				}
				if (!used && field[ny][nx] == 1) {// 오른쪽으로
					nx += 1;
					used = true;
				} else if (!used && nx-1 >= 0 && field[ny][nx - 1] == 1) { //왼쪽으로
					nx -= 1;
					used = true;
				} else { //내려가기
					used = false;
					ny += 1;
				}
			}
		}
		return true;
	}

	static void permutation(int depth, int index, int maxLadder) {
		if (answer != 4)
			return;
		if (depth == maxLadder) {
			if (isSuccess())
				answer = maxLadder;
			return;
		}
		for (int i = index + 1; i < N * H - H; i++) {
			int nx = i % (N - 1);
			int ny = i / (N - 1);
			// 좌, 현재, 우 위치에 이미 사다리가 설치된 경우
			if (field[ny][nx] == 1 || (nx - 1 >= 0 && field[ny][nx - 1] == 1) || field[ny][nx + 1] == 1)
				continue;
			field[ny][nx] = 1;
			permutation(depth + 1, i, maxLadder);
			field[ny][nx] = 0;
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		for (int i = 0; i < 4; i++) {
			permutation(0, -1, i);
			if (answer != 4)
				break;
		}
		System.out.println(answer > 3 ? -1 : answer);
	}
}