package swea5604;
import java.util.*;
import java.io.*;

public class Solution_swea_5604_구간합수열 {
	static StringBuilder sb = new StringBuilder();
	static HashMap<Long, Long> map = new HashMap<>();
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = Integer.parseInt(br.readLine());
		for(int tc=1;tc<=TC;tc++) {
			st = new StringTokenizer(br.readLine());
			long A = Long.parseLong(st.nextToken());
			long B = Long.parseLong(st.nextToken());
			sb.append("#").append(tc).append(" ").append(calc(A,B)).append("\n");
		}
	}
	static long calc(long start,long end) {
		return F(end) - F(start==0?0:start-1);
	}
	static long getV(long N) {
		return pow10(len(N));
	}
	static long G(long N,long V) {
		if(N<10)return map.get(N);
		return N/V * (N%V+1L) + F(N%V);
	}
	static long F(long N) {
		if(map.containsKey(N))return map.get(N);
		long V = getV(N);
		long part1 = F(N-1 - N%V);
		long part2 = G(N,V);
		long result = part1+part2;
		map.put(N, result);
		return map.get(N);
	}
	static void init() {
		map.put(0L, 0L);
		for(long i = 1;i<=9;i++)
			map.put(i, map.get(i-1)+i);
		for(long i = 1;i<=15;i++) {
			long v = pow10(i);
			long h = pow10(i)/10;
			map.put(v-1L,i*h*45);
		}
	}
	static long len(long x) {
		return 0L+(x+"").length()-1;
	}
	static long pow10(long x) {
		return (long)Math.pow(10, x);
	}
	public static void main(String[] args) throws IOException {
		init();
		input();
		System.out.println(sb);
	}
}