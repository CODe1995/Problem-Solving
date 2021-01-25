package boj9012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int T, cnt;
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(bf.readLine());
		T = Integer.parseInt(st.nextToken());
		for (int t = 0; t < T; t++) {
			cnt = 0;
			st = new StringTokenizer(bf.readLine());
			String tmp = st.nextToken();
			for (int i = 0; i < tmp.length(); i++) {
				if (tmp.charAt(i) == '(') {
					cnt++;
				} else
					if (--cnt < 0)break;
			}
			if (cnt == 0)System.out.println("YES");
			else System.out.println("NO");
		}
	}
}
