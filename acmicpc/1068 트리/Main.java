package boj1068;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int nodes[][],N,cnt;
	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		nodes = new int[N+1][2];
		st = new StringTokenizer(br.readLine());
		for(int i =0;i<N;i++) {
			int parent = Integer.parseInt(st.nextToken()) ;
			nodes[i][0]=parent;//부모 번호
			if (parent!=-1)nodes[parent][1]++;//자식 카운팅
		}
		int d = Integer.parseInt(br.readLine());
		if(nodes[d][0]!=-1)
			nodes[nodes[d][0]][1]--;//유효한 부모라면 자식 갯수 감소
		nodes[d][0]=-2;//부모 인덱스 제거
		int answer=0;
		for(int i =0;i<N;i++) {
			if(nodes[i][1]==0) {//자식이없다 = 리프노드
				int parent = nodes[i][0];
				while(parent>-1)parent = nodes[parent][0];//-1,-2중 하나가 나오면 끝
				if(parent==-1)answer++;//정상적인 부모라면				
			}
		}
		System.out.println(answer);
	}
}