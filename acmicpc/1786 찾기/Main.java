package boj1786_찾기;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[] target, word;
	static int[] pi;
	static ArrayList<Integer> answer;

	static void input() throws IOException {
		target = br.readLine().toCharArray();
		word = br.readLine().toCharArray();
		pi = new int[word.length];
		answer = new ArrayList<>();
	}

	public static void main(String[] args) throws IOException {
		input();
		analizeTarget();
		kmp();
		int answerSize = answer.size();
		System.out.println(answerSize);
		StringBuilder sb = new StringBuilder();
		for(int i =0;i<answerSize;i++) {
			sb.append(answer.get(i)).append(" ");
		}
		System.out.println(sb);
	}

	static void kmp() {
		int targetLength = target.length;
		int wordLength = word.length;
		int j = 0;
		for (int i = 0; i < targetLength; i++) {
			while (j > 0 && target[i] != word[j]) {
				j = pi[j - 1];
			}
			if (target[i] == word[j]) {
				if (j == wordLength - 1) {
					answer.add(i - wordLength + 2);
					j = pi[j];
				} else {
					j++;
				}
			}
		}
	}

	static void analizeTarget() {
		int wordLength = word.length;
		int j = 0;

		for (int i = 1; i < wordLength; i++) {
			while (j > 0 && word[i] != word[j]) {
				j = pi[j - 1];
			}
			if (word[i] == word[j]) {
				pi[i] = ++j;
			}
		}
	}
}