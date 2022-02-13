package swea2948_문자열교집합;

import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int answer, N, M;
	static HashSet<String> nMap;

	static void solution() {

	}

	static void init() throws IOException {
		answer = 0;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		nMap = new HashSet<>();

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			nMap.add(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			if (nMap.contains(st.nextToken())) {
				answer++;
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