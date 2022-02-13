package boj4354_문자열제곱;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[] source;
	static int[] pi;

	static void getPi() {
		int j = 0;
		pi = new int[source.length];
		for (int i = 1; i < source.length; i++) {
			while (j > 0 && source[i] != source[j]) {
				j = pi[j - 1];
			}
			if (source[i] == source[j]) {
				pi[i] = ++j;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		while (true) {
			source = br.readLine().toCharArray();
			if (source[0] == '.')
				break;
			getPi();
			int N = source.length;
			if (N % (N - pi[N - 1]) > 0) {
				System.out.println(1);
			} else {
				System.out.println(N / (N - pi[N - 1]));
			}
		}
	}
}