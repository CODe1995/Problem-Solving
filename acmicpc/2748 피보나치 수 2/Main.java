import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static long [] dp = new long[91];
	public static long fibo(int n) {
		if(dp[n]!=-1)
			return dp[n];
		dp[n]=fibo(n-1)+fibo(n-2);
		return dp[n];
	}
	public static void main(String[] args) {
		Arrays.fill(dp,-1);
		dp[0]=0;
		dp[1]=1;
		dp[2]=1;
		Scanner scan = new Scanner(System.in);
		System.out.println(fibo(scan.nextInt()));
	}
}
