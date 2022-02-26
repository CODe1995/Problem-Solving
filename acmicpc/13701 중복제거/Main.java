package boj13701_중복제거;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int n = 0;
		BitSet bitset = new BitSet();
		while(st.hasMoreTokens()) {
			n = Integer.parseInt(st.nextToken());
			if(bitset.get(n))
				continue;
			bitset.set(n);
			sb.append(n).append(" ");
			// 켜져있다 = 반복없다
		}
		System.out.println(sb);
	}
}