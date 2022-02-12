package boj1701_Cubeditor;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static String source;
	static int answer, pi[];

	static void input() throws IOException {
		source = br.readLine();
		answer = 0;
	}

	static void getPi(String splitString) {
		char[] s = splitString.toCharArray();
		int N = s.length;
		int j = 0;
		pi = new int[N];
		for (int i = 1; i < N; i++) {
			while (j > 0 && s[i] != s[j]) {
				j = pi[j - 1];
			}
			if (s[i] == s[j]) {
				pi[i] = ++j;
				answer = Math.max(answer, pi[i]);
			}
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		for (int i = 0; i < source.length(); i++)
			getPi(source.substring(i));
		System.out.println(answer);
	}
}