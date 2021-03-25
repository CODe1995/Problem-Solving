package swea1251;
import java.util.*;
import java.io.*;

public class Solution {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,arr[][],parent[];
	static double E;
	static ArrayList<DIST> query;
	static double answer;
	static class DIST{
		int start,end;
		double cost;
		public DIST(int start, int end, double cost) {
			this.start = start;this.end = end;this.cost = cost;
		}		
	}
	static int getParent(int x) {
		if(parent[x]==x)return x;
		return parent[x] = getParent(parent[x]);
	}
	static void unionParent(int a,int b) {
		a = getParent(a);
		b = getParent(b);
		if(a<b)parent[b]=a;
		else parent[a]=b;
	}
	
	static void input() throws IOException{
		int T = stoi(br.readLine());
		for(int t=1;t<=T;t++) {
			/*STATIC INIT*/
			answer = 0;
			N = stoi(br.readLine());
			arr = new int[N][2];
			parent = new int[N+1];
			for(int i =0;i<N+1;i++)parent[i]=i;
			query = new ArrayList<>();
			
			for(int z=0;z<2;z++) {
				st = new StringTokenizer(br.readLine());
				for(int i =0;i<N;i++) {
					arr[i][z] = stoi(st.nextToken());
				}
			}
			E = Double.parseDouble(br.readLine());//환경부담세율
			for(int i =0;i<N;i++) {
				for(int j=i+1;j<N;j++) {
					double tmp = Math.pow(Math.abs(arr[i][0]-arr[j][0]),2)+Math.pow(Math.abs(arr[i][1]-arr[j][1]),2);
					query.add(new DIST(i,j,tmp));
				}
			}
			Collections.sort(query,(o1,o2)->{
				return o1.cost-o2.cost<0?-1:o1.cost==o2.cost?0:1;
			});

			for(int i =0;i<query.size();i++) {
				DIST cur = query.get(i);
				if(getParent(cur.start)==getParent(cur.end))continue;
				unionParent(cur.start,cur.end);
				answer += cur.cost;
//				System.out.println(cur.start+"~"+cur.end+":"+cur.cost);
			}
			
			
			sb.append("#").append(t).append(" ").append(Math.round(E*answer)).append("\n");
		}
		System.out.println(sb);
	}
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException {
		input();
		
	}
}