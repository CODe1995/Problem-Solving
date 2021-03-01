package boj2166;
import java.util.*;
import java.io.*;
import java.math.BigDecimal;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int N  = Integer.parseInt(br.readLine());
		long[][] arr = new long[N+1][2];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0]=Integer.parseInt(st.nextToken());
			arr[i][1]=Integer.parseInt(st.nextToken());
		}
		arr[N][0]=arr[0][0];
		arr[N][1]=arr[0][1];
		long xsum = 0;
		long ysum = 0;
		for(int i =0;i<N;i++) {
			xsum+=arr[i][0]*arr[i+1][1];
			ysum+=arr[i][1]*arr[i+1][0];
		}
		BigDecimal big = new BigDecimal(Math.abs(ysum-xsum)); 
		BigDecimal dv = new BigDecimal(2);
		System.out.println(big.divide(dv,1,BigDecimal.ROUND_UP));
	}
}