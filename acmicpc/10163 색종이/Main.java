package boj10163;
import java.util.*;
import java.io.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int stoi(String s) {return Integer.parseInt(s);}
	public static void main(String[] args) throws IOException {
		int[][] field = new int[101][101];
		int N  = Integer.parseInt(br.readLine());
		int answer[] = new int[N+1];
		for(int i =1;i<=N;i++) {
			st = new StringTokenizer(br.readLine());
			int pos[] = new int[] {stoi(st.nextToken()),stoi(st.nextToken()),stoi(st.nextToken()),stoi(st.nextToken())};
			for(int y = pos[0];y<pos[0]+pos[2];y++)for(int x = pos[1];x<pos[1]+pos[3];x++)field[y][x]=i;
		}
		for(int i =0;i<101;i++)for(int j =0;j<101;j++)answer[field[i][j]]++;
		for(int i = 1;i<=N;i++)System.out.println(answer[i]);
	}	
}