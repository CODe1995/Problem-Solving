package swea5607;
import java.util.*;
import java.io.*;

public class Solution_swea_5607_조합 {
	static StringBuilder sb = new StringBuilder();
	static int MOD = 1234567891;
	static long factorial[];
	static long fermat(long n, int x) {
		if(x==0)return 1;
		long tmp = fermat(n,x/2);
		long ret = (tmp*tmp)%MOD;
		if(x%2==0)return ret;
		else return (ret*n)%MOD;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = Integer.parseInt(br.readLine());
		factorial = new long[1000001];//매 TC마다 재계산 방지
		factorial[0]=1;
		for(int i=1;i<=1000000;i++)factorial[i]=(factorial[i-1]*i)%MOD;	
		for(int tc=1;tc<=TC;tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());
			long bottom = factorial[N]*fermat((factorial[R]*factorial[N-R])%MOD,MOD-2);			
			sb.append("#").append(tc).append(" ").append(bottom%MOD).append("\n");
		}		
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}