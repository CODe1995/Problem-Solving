package boj17144;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M, T, field[][], mx, my, direction[][];

	static void input() throws IOException {
		direction = new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };// 하,우,상,좌
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		field = new int[N][M];
		mx = -1;
		my = -1;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int x = Integer.parseInt(st.nextToken());
				if (x == -1) {
					if (mx == -1) {
						mx = j;
						my = i;
					}
					continue;
				}
				field[i][j] = x;
			}
		}
	}

	static int getAllDust() {
		int cnt = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				cnt += field[i][j];
		return cnt;
	}

	static void spread() {
		int[][] newField = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (field[i][j] >= 5) { // 5부터 유의미
					int spreadedCnt = 0;
					int minusDust = field[i][j] / 5;
					for (int[] dir : direction) {
						int nx = dir[0] + j;
						int ny = dir[1] + i;
						if (nx < 0 || ny < 0 || nx >= M || ny >= N)
							continue;
						if ((nx == mx && ny == my) || (nx == mx && ny == my + 1))
							continue;
						spreadedCnt++;
						newField[ny][nx] += minusDust;
					}
					newField[i][j] -= minusDust * spreadedCnt;
				}
			}
		}
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				field[i][j] += newField[i][j];
	}

	static void runMachine() {
		int[][] mList = new int[][] { { mx, my }, { mx, my + 1 } };
		// direction: 하-우-상-좌
		// 위쪽: 상-우-하-좌 2103
		// 아래쪽: 하-우-상-좌 0123
		int[][] machineDirs = new int[][] { { 2, 1, 0, 3 }, { 0, 1, 2, 3 } };
		for (int machineIndex = 0; machineIndex < 2; machineIndex++) {
			int cmx = mList[machineIndex][0];
			int cmy = mList[machineIndex][1];
			int[] curMachineDir = machineDirs[machineIndex]; // 이번 머신이 도는 방향

			int curDirPos = 0;
			int cx = cmx;
			int cy = cmy;
			while (curDirPos < 4) {
				int nx = cx + direction[curMachineDir[curDirPos]][0];
				int ny = cy + direction[curMachineDir[curDirPos]][1];
				while (nx != -1 && nx != M && ny != mList[(machineIndex+1)%2][1] && ny != (machineIndex==0?-1:N)) {
					if(cx==cmx&&cy==cmy)
						field[cy][cx] = 0;
					else
						field[cy][cx] = field[ny][nx];
					field[ny][nx]=0;
					cx = nx;
					cy = ny;
					nx = cx + direction[curMachineDir[curDirPos]][0];
					ny = cy + direction[curMachineDir[curDirPos]][1];
				}
				curDirPos++;
			}

		}
	}

	public static void main(String[] args) throws IOException {
		input();
		for (int t = 0; t < T; t++) {
			spread();
			runMachine();
		}
		System.out.println(getAllDust());
	}
}