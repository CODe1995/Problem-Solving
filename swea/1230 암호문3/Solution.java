package swea1230_암호문3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static LinkedList<String> encryptedNumber;
	static int N, countOrder;

	static String getAnswer() {
		StringBuilder sb = new StringBuilder();
		Iterator<String> iter = encryptedNumber.iterator();
		for (int i = 0; i < 10; i++) {
			sb.append(iter.next()).append(" ");
		}
		return sb.toString();
	}

	static void init() throws Exception {
		N = Integer.parseInt(br.readLine());
		encryptedNumber = new LinkedList<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			encryptedNumber.add(st.nextToken());
		}
		countOrder = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < countOrder; i++) {
			String cmd = st.nextToken();
			if (cmd.equals("I")) {// 삽입
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				LinkedList<String> numberArray = new LinkedList<>();
				for (int j = 0; j < y; j++) {
					numberArray.add(st.nextToken());
				}
				encryptedNumber.addAll(x, numberArray);
			} else if (cmd.equals("D")) {// 삭제
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				for (int j = 0; j < y; j++)
					encryptedNumber.remove(x);
			} else if (cmd.equals("A")) {// 추가
				int y = Integer.parseInt(st.nextToken());
				for (int j = 0; j < y; j++) {
					encryptedNumber.add(st.nextToken());
				}
			}
		}
	}

	public static void main(String[] args) throws Exception {
		for (int t = 1; t <= 10; t++) {
			init();
			System.out.println("#"+t+" "+getAnswer());
		}
	}
}
