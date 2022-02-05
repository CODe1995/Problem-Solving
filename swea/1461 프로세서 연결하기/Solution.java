package swea1461_프로세서연결하기;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, field[][], answerCore, answerLine, alreadyConnectedCoreCnt;
	static ArrayList<Core> cores;
	static final int direction[][] = { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };

	static class Core {
		int x, y;

		public Core(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Core [x=" + x + ", y=" + y + "]";
		}		
	}

	static void solution(int depth, int totalLength, int totalCore) {
		if (depth == cores.size()) {
			if (answerCore < totalCore) {
				answerCore = totalCore;
				answerLine = totalLength;
			} else if (answerCore == totalCore) {
				answerLine = Integer.min(answerLine, totalLength);
			}
			return;
		}
		Core core = cores.get(depth);
		Queue<Integer> lineQueue = new LinkedList<>();
		for (int[] dir : direction) {
			int nx = core.x;
			int ny = core.y;
			int length = 0;
			while (true) {
				nx += dir[0];
				ny += dir[1];
				if (isHitWall(nx, ny)) {
					solution(depth + 1, totalLength + length, totalCore + 1);
					break;
				}
				if (isHitCoreOrLine(nx, ny)) {
					break;
				}
				createLine(nx, ny, lineQueue);
				length++;
			}
			deleteLine(lineQueue);
		}
		solution(depth + 1, totalLength, totalCore);
	}

	static void createLine(int x, int y, Queue<Integer> queue) {
		field[y][x] = 2;
		queue.add(x+y*N);
	}

	static void deleteLine(Queue<Integer> queue) {
		while (!queue.isEmpty()) {
			int num = queue.poll();
			int x = num % N;
			int y = num / N;
			field[y][x] = 0;
		}
	}

	static boolean isHitWall(int x, int y) {
		if (x == -1 || y == -1 || x == N || y == N)
			return true;
		return false;
	}

	static boolean isHitCoreOrLine(int x, int y) {
		if (field[y][x] != 0)
			return true;
		return false;
	}

	static void init() throws IOException {
		answerCore = 0;
		answerLine = Integer.MAX_VALUE;
		alreadyConnectedCoreCnt = 0;
		N = Integer.parseInt(br.readLine());
		field = new int[N][N];
		cores = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
				if (field[i][j] == 1) {
					if (i != 0 && j != 0 && i != N - 1 && j != N - 1)
						cores.add(new Core(j, i));
					else
						alreadyConnectedCoreCnt++;
				}
			}
		}
		answerCore = alreadyConnectedCoreCnt;
	}

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			init();
			solution(0, 0, alreadyConnectedCoreCnt);
			System.out.println("#"+tc+" "+answerLine);
		}

	}
}