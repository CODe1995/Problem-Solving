package boj2239;
import java.util.*;
import java.io.*;

public class Main_boj_2239_스도쿠 {
	static StringBuilder sb = new StringBuilder();
	static int field[][];
	static boolean exitFlag = false;
	static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		field = new int[9][9];
		for(int i =0;i<9;i++) {
			char[] tc = br.readLine().toCharArray();
			for(int j =0;j<9;j++) {
				field[i][j] = tc[j]-48;
			}
		}
		dfs(0,0);
	}
	static void dfs(int x,int y) {
		if(exitFlag) {
			print();
			return;
		}		
		if(field[y][x]!=0) {
			if(x==8) {
				if(x==8 && y==8)exitFlag=true;
				dfs(0,(y+1)%9);
			}else {
				dfs((x+1)%9,y);
			}
		}
		else {
			for(int i =1;i<=9;i++) {
				if(exitFlag)return;
				if(!checkRow(x,y,i))continue;
				if(!checkSection(x,y,i))continue;
				if(!checkCol(x,y,i))continue;
				field[y][x]=i;
				if(x==8) {
					if(x==8 && y==8)exitFlag=true;
					dfs(0,(y+1)%9);
				}else {
					dfs((x+1)%9,y);
				}
				field[y][x]=0;			
			}
		}
	}
	static boolean checkRow(int x,int y,int needNum) {
		for(int i =0;i<9;i++) {
			if(field[y][i]==needNum)
				return false;
		}
		return true;
	}
	static void solution(int x,int y) {
		boolean need[] = new boolean[10];
		for(int i =0;i<9;i++)
			need[field[y][i]]=true;
		for(int i=1;i<=9;i++) {
			if(need[i])continue;
			int needNum = i;
			if(!checkSection(x,y,needNum))continue;
			if(!checkCol(x,y,needNum))continue;
			field[y][x]=needNum;
			need[i]=true;
			break;
		}
	}
	static boolean checkCol(int x,int y,int needNum) {
		for(int i=0;i<9;i++) {
			if(field[i][x]==needNum)
				return false;
		}
		return true;
	}
	static boolean checkSection(int x,int y,int needNum) {
		Pos start = getStartPos(x,y);
		for(int i =0;i<3;i++) {
			for(int j =0;j<3;j++) {
				int nx = start.x+j;
				int ny = start.y+i;
				if(field[ny][nx]==needNum) {
					return false;
				}
			}
		}
		return true;
	}
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static Pos getStartPos(int x,int y) {
		return new Pos((x/3)*3,(y/3)*3);
	}
	static void print() {
		for(int i =0;i<9;i++) {
			for(int j =0;j<9;j++) {
				sb.append(field[i][j]);
			}
			sb.append("\n");
		}
	}
	public static void main(String[] args) throws IOException {
		input();
		System.out.println(sb);
	}
}