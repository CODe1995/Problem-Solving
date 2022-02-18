package swea8935_스팟마트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Solution {
	static int dp[][][] = new int[3001][101][101], N, M, nArr[], mArr[];

	static int dfs(int n, int m, int skip) {
		if (n > N)
//			return dp[n][m][skip]=0;
			return 0;
		if (dp[n][m][skip] != -1)
			return dp[n][m][skip];
		int result = 0;
		// N 선택 N 스킵
		if (n < N) {
			result = Math.max(result, dfs(n + 2, m, skip) + nArr[n]);
		}
		// N 선택 M 스킵, M 선택 N 스킵
		if (n < N && m + skip < M) {
			result = Math.max(result, dfs(n + 1, m, skip + 1) + nArr[n]);
			result = Math.max(result, dfs(n + 1, m + 1, skip) + mArr[m]);
		}
		// M 선택 M 스킵
		if (m + skip + 1 < M) {
			result = Math.max(result, dfs(n, m + 1, skip + 1) + mArr[m]);
		}
		// N 스킵
		if (n < N) {
			result = Math.max(result, dfs(n + 1, m, skip));
		}
		if (m + skip < M) {
			result = Math.max(result, dfs(n, m, skip + 1));
		}
//		System.out.println(String.format("[%s][%s][%s]:%s", n, m, skip, result));
		return dp[n][m][skip] = result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; tc++) {
//			System.out.println(String.format("====%s====", tc));
			N = Integer.parseInt(br.readLine());
			nArr = new int[N];
			for (int i = 0; i < N; i++) {
				nArr[i] = Integer.parseInt(br.readLine());
			}
			M = Integer.parseInt(br.readLine());
			mArr = new int[M];
			for (int i = 0; i < M; i++) {
				mArr[i] = Integer.parseInt(br.readLine());
			}

			for (int i = 0; i <= N; i++) {
				for (int j = 0; j <= M; j++) {
					for (int k = 0; k <= M; k++) {
						dp[i][j][k] = -1;
					}
				}
			}
			Arrays.sort(mArr);
			arrayReverse();
//			System.out.println(Arrays.toString(mArr));
			sb.append("#").append(tc).append(" ").append(dfs(0, 0, 0)).append("\n");
		}
		System.out.println(sb);
	}

	static void arrayReverse() {
		for (int i = 0; i < M / 2; i++) {
			int tmp = mArr[i];
			mArr[i] = mArr[M - i - 1];
			mArr[M - i - 1] = tmp;
		}
	}
}
