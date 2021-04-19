package swea3238;
import java.util.*;
import java.io.*;
//페르마+분할정복
public class Solution_swea_3238_이항계수구하기 {
	static StringBuilder sb = new StringBuilder();
	static long factorial[],N,R;
	static int P;
	static long fermat(long a, int p) {
		long ret = 1;
		while(p>0) {
			if((p&1)>0) {
				ret = (ret*a)%P;				
			}
			a=(a*a)%P;
			p/=2;
		}
		return ret;
	}
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = Integer.parseInt(br.readLine());
		factorial = new long[100001];
		factorial[0]=1;
		for(int tc=1;tc<=TC;tc++) {
			st = new StringTokenizer(br.readLine());
			N = Long.parseLong(st.nextToken());
			R = Long.parseLong(st.nextToken());
			P = Integer.parseInt(st.nextToken());
			for(int i=1;i<=P;i++)factorial[i]=(factorial[i-1]*i)%P;
			long answer = 1;
			while(N>0 || R>0){
				int a = (int) (N%P);
				int b = (int) (R%P);
				if(a<b) {
					answer = 0;
					break;
				}
				answer=(answer*factorial[a])%P;
				answer=(answer*fermat(factorial[b]*factorial[a-b]%P,P-2))%P;
				N/=P;
				R/=P;
			}
			sb.append("#").append(tc).append(" ").append(answer);
		}
	}

	public static void main(String[] args) throws IOException {
		input();
	}
}