package boj13300;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int answer = 1;
		int arr[][] = new int[N][2];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());//성별
			arr[i][1] = Integer.parseInt(st.nextToken());//학년
		}
		Arrays.sort(arr,(a,b)->{return a[0]==b[0]?a[1]-b[1]:a[0]-b[0];});
		int k =K;
		for(int i=1;i<N;i++) {
			k--;
			if(k==0 || arr[i][0]!=arr[i-1][0] || arr[i][1]!=arr[i-1][1]) {answer++;k=K;continue;}//정원꽉참, 성별다름, 학년다름
		}
		System.out.println(answer);
	}
}