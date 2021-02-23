package boj2477;
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int K = Integer.parseInt(br.readLine());
		int arr[] = new int[6];//모든 변 길이
		int max_area = 0;
		int min_area = 0;
		for(int i =0;i<6;i++) {
			st = new StringTokenizer(br.readLine());
			st.nextToken();//방향 입력은 생략						
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for(int i =0;i<6;i++) {
			int current_area =  arr[i]*arr[(i+1)%6];
			if(current_area > max_area) {//현재 넓이가 최대 넓이라면?
				max_area = current_area;
				min_area = arr[(i+3)%6]*arr[(i+4)%6];
			}
		}
		System.out.println((max_area-min_area)*K);
	}
}