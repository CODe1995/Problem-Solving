package boj17406;

import java.util.*;
import java.io.*;

public class Main_220111 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, K, arr[][], originArr[][], commands[][], answer;
	static boolean visitCommand[];
	static int nextCommand[];
	static int direction[][] = new int[][] { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };// 우하좌상

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		answer = Integer.MAX_VALUE;
		originArr = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				originArr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		nextCommand = new int[K];
		visitCommand = new boolean[K];
		commands = new int[K][3];
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			commands[i][1] = Integer.parseInt(st.nextToken()) - 1;
			commands[i][0] = Integer.parseInt(st.nextToken()) - 1;
			commands[i][2] = Integer.parseInt(st.nextToken());
		}
	}

	static int getSumArr() {
		int answer = 250000;
		for (int i = 0; i < N; i++) {
			int lineSum = 0;
			for (int j = 0; j < M; j++) {
				lineSum += arr[i][j];
			}
			answer = Math.min(answer, lineSum);
		}
		return answer;
	}

	static void turnArray(int x, int y, int size) {
		for (int length = 1; length <= size; length++) {
			int nx = x - length;
			int ny = y - length;
			turnLayer(nx, ny, length * 2 + 1);
		}
	}

	static void turnLayer(int x, int y, int size) { // 좌측 상단 좌표부터 시작
		int cx = x;
		int cy = y;
		int beforeValue = arr[cy][cx];
		for (int dir[] : direction) {
			while (true) {
				int nx = cx + dir[0];
				int ny = cy + dir[1];
				if (nx >= x + size || nx < x || ny < y || ny >= y + size)
					break;
				// 값의 이동
				int temp = arr[ny][nx];
				arr[ny][nx] = beforeValue;
				beforeValue = temp;
				cx = nx;
				cy = ny;
			}
		}
	}

	static int[][] deepCopy(int[][] src) {
		int[][] dest = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				dest[i][j] = src[i][j];
			}
		}
		return dest;
	}

	static void permutation(int depth) {
		if (depth == K) {
			arr = deepCopy(originArr);
			for (int i = 0; i < K; i++) {
				turnArray(commands[nextCommand[i]][0], commands[nextCommand[i]][1], commands[nextCommand[i]][2]);
			}
			answer = Math.min(getSumArr(), answer);
			return;
		}
		for (int i = 0; i < K; i++) {
			if (visitCommand[i])
				continue;
			visitCommand[i] = true;
			nextCommand[depth] = i;
			permutation(depth + 1);
			visitCommand[i] = false;
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		permutation(0);
		System.out.println(answer);
	}
}