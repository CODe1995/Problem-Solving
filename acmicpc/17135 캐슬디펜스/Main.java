package boj17135;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	static int H,W,D;//세로, 가로, 사거리
	static int field[][];//필드 저장
	static int max_kill = 0;//최대 킬 수가 저장되는 변수
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		String input[] = br.readLine().split(" ");
		H = Integer.parseInt(input[0]);
		W = Integer.parseInt(input[1]);
		D = Integer.parseInt(input[2]);
		
		field = new int[H][W];
		for(int i  = 0 ; i<H;i++) {
			input = br.readLine().split(" ");
			for(int j = 0 ;j<W;j++)
				field[i][j] = Integer.parseInt(input[j]);
		}
		
		for(int i = 0 ; i<W;i++)
			for(int j = i+1;j<W;j++)
				for(int k = j+1;k<W;k++)
					max_kill = Math.max(max_kill, simulation(i,j,k));
		System.out.println(max_kill);
	}
	
	public static int simulation(int a1,int a2,int a3) {
		int c_field[][] = new int[H][W];
		for(int i = 0 ; i < field.length;i++)	//2차원 배열 Deep Copy 수행
			System.arraycopy(field[i], 0, c_field[i], 0, field[i].length);
		int killed_cnt = 0;
		for(int h=H; h>-1;h--) {
			ArrayList<int[]> killed_list = new ArrayList<int[]>();
			for(int p : Arrays.asList(a1,a2,a3)) {
				int[] tmp = shoot(h, p, c_field);
				if(tmp!=null) {
					killed_list.add(tmp);
				}
			}
			for(int[] killed_enemy:killed_list) {
				if(c_field[killed_enemy[1]][killed_enemy[0]]==1) {
					c_field[killed_enemy[1]][killed_enemy[0]]=0;
					killed_cnt++;
				}
			}
		}
		return killed_cnt;
	}
	public static int[] shoot(int h,int p, int[][] c_field){
		for(int d=1;d<D+1;d++) {
			for(int left=d; left>-1; left--) {
				int diff = d-left;
				int hdiff = h - diff;
				int wdiff = p - left;
				if(diff>0 && 0<=hdiff && hdiff<H && 0<=wdiff && wdiff<W && c_field[hdiff][wdiff]==1) {
					int[] ret = {wdiff, hdiff};
					return ret;
				}				
			}
			for(int right=1; right<d+1; right++) {
				int diff = d-right;
				int hdiff = h +-diff;
				int wdiff = p + right;
				if(diff>0 && 0<=hdiff && hdiff<H && 0<=wdiff && wdiff<W && c_field[hdiff][wdiff]==1) {
					int[] ret = {wdiff, hdiff};
					return ret;
				}			 
			}
		}
		return null;
	}
}
