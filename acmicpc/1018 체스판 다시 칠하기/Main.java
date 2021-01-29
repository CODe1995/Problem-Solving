package boj1018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static char[][] field;	
	static char[][] comp;
	static int func(int W,int H) {
		int cnt1=0, cnt2=0;
		for(int h =H;h<H+8;h++) {
			for(int w=W;w<W+8;w++) {
				//첫 칸이 B인 경우
				if(field[h][w]==comp[h-H][w-W])cnt1++;				
				//첫 칸이 W인 경우
				if(field[h][w]!=comp[h-H][w-W])cnt2++;
			}
		}		
		return Math.min(cnt1, cnt2);
	}
	
	static void solve() throws IOException{				
		String args[] = bf.readLine().split(" ");
		int height = Integer.parseInt(args[0]);
		int width = Integer.parseInt(args[1]);
		field = new char[height][width];
		for(int i =0;i<height;i++)
			field[i] = bf.readLine().toCharArray();		
		
		int answer = 2501;
		for(int y =0;y+8<=height;y++)
			for(int x =0;x+8<=width;x++)
				answer = Math.min(func(x,y),answer);//더 작은 값으로
		
		System.out.println(answer);
	}
	
	public static void main(String[] args) throws IOException{
		comp = new char[8][8];
		for(int i =0;i<8;i++)
			for(int j =0;j<8;j++)
				comp[i][j]=(i+j)%2==0?'W':'B';			
		solve();
	}
}