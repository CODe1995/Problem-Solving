import java.util.*;
import java.io.*;

public class boj_2352_반도체설계 {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, length=0;
	static int arr[], v[];
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		v = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++)
			arr[i] = Integer.parseInt(st.nextToken());
	}
	static void solution() {
		for(int i=0;i<N;i++) {
			if(length==0 || v[length-1] < arr[i]) {
				v[length] = arr[i];
				length++;
			}
			else {
				int update = Arrays.binarySearch(v, arr[i]);
				v[update] = arr[i];				
			}
		}
	}
	public static void main(String[] args) throws IOException {
		input();
		solution();
		System.out.println(length);
	}
}