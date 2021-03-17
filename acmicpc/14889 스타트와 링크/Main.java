package boj14889;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,field[][],answer = Integer.MAX_VALUE;
	static boolean checked[];
	
	static void dfs(int depth,int index,int team1[]) {
		if(depth==N/2) {
			int team2[] = new int[N/2];
			int cnt =0;
			for(int i =0;i<N;i++) {
				if(!checked[i])team2[cnt++]=i;
			}
			int score1= 0;
			int score2= 0;			
			for(int i =0;i<N/2;i++) {
				for(int j =i+1;j<N/2;j++) {
					if(i==j)continue;
					score1+=field[team1[i]][team1[j]]+field[team1[j]][team1[i]];
					score2+=field[team2[i]][team2[j]]+field[team2[j]][team2[i]];
				}
			}
			
//			for(int i =0;i<N/2;i++)System.out.print(team1[i]+1);
//			System.out.print(" , ");
//			for(int i =0;i<N/2;i++)System.out.print(team2[i]+1);
//			System.out.println(":"+(score1-score2));
			answer = Math.min(Math.abs(score1-score2), answer);
			return;
		}
		for(int i = index;i<N;i++) {
			if(checked[i])continue;
			checked[i]=true;
			team1[depth]=i;
			dfs(depth+1,i+1,team1);
			checked[i]=false;
		}
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		checked = new boolean[N];
		field=new int[N][N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<N;j++) {
				field[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		dfs(0,0,new int[N/2]);
		System.out.println(answer);
	}
}