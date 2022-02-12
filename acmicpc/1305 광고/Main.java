package boj1305_광고;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, answer;
	static char[] source;
	static int[] pi;

	public static void main(String[] args) throws IOException {
		input();
		getPi();
		System.out.println(answer);
	}	

	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		source = br.readLine().toCharArray();
		pi = new int[N];
		answer = 0;
	}

	static void getPi() {
		int j = 0;
		for (int i = 1; i < N; i++) {
			while (j > 0 && source[i] != source[j]) {
				j = pi[j - 1];
			}
			if (source[i] == source[j]) {
				pi[i] = ++j;
			}
		}
		answer = N - pi[N - 1];
	}
}