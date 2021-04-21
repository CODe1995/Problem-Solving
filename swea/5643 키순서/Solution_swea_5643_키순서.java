package swea;
import java.util.*;
import java.io.*;

public class Solution_swea_5643_키순서 {
	static StringBuilder sb = new StringBuilder();
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = stoi(br.readLine());
		for(int tc=1;tc<=TC;tc++) {			
			int N = stoi(br.readLine());//학생수
			int M = stoi(br.readLine());//비교횟수
			int arr[][] = new int[N][N];
			for(int i =0;i<M;i++) {
				st = new StringTokenizer(br.readLine());
				int a = stoi(st.nextToken())-1;
				int b = stoi(st.nextToken())-1;
				arr[a][b] = 1;
			}
			
			for(int k=0;k<N;k++) {
				for(int i=0;i<N;i++) {
					for(int j=0;j<N;j++) {
						if(arr[i][k]==1 && arr[k][j]==1) {
							arr[i][j]=1;
						}
					}
				}
			}
			int answer = 0;
			for(int i=0;i<N;i++) {
				for(int j =0;j<N;j++) {
					if(i==j)continue;
					if(arr[i][j]==0 && arr[j][i]==0) {
						answer--;
						break;
					}
				}
				answer++;
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}

	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}