package swea8382;
import java.util.*;
import java.io.*;

public class Solution_swea_8382_방향전환 {
	static StringBuilder sb = new StringBuilder();

	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int x = Math.abs(x1-x2);
			int y = Math.abs(y1-y2);
			int diff = Math.abs(y-x);
			sb.append("#").append(t).append(" ").append(2*Math.min(x, y)+2*diff-(diff%2)).append("\n");
		}
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}