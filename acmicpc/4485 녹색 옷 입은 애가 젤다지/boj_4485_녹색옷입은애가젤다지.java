import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj_4485_녹색옷입은애가젤다지 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;	
	static HashMap<Integer, ArrayList<Node>> map = new HashMap<>();
	static int N, d[][], field[][];
	static int direction[][] = new int[][] {{0,1},{1,0},{-1,0},{0,-1}};		
	static class Node implements Comparable<Node>{
		int x,y,dist;	

		public Node(int x, int y, int dist) {
			this.x = x;
			this.y = y;
			this.dist = dist;
		}
		
		@Override
		public int compareTo(Node o) {			
			return this.dist-o.dist;
		}
	}
	public static boolean input() throws NumberFormatException, IOException {
		N = Integer.parseInt(br.readLine());
		if (N==0)return false;
		
		field = new int[N][N];
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<N;j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
			}
		}		
		
		return true;
	}
	public static void dijkstra()
	{
		int INF = 10000000;
		d = new int[N][N];
		
		for(int i =0;i<N;i++) {
			Arrays.fill(d[i], INF);
		}
		
		d[0][0] = field[0][0];//init value		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(0,0,field[0][0]));
		
		while(!pq.isEmpty()) {
			Node cur = pq.poll();
			
			for(int[] dir:direction) {
				int nx = cur.x+dir[0];
				int ny = cur.y+dir[1];
				if(nx<0||ny<0||nx>=N||ny>=N)continue;
				if(d[ny][nx]>d[cur.y][cur.x]+field[ny][nx]) {
					d[ny][nx] = d[cur.y][cur.x]+field[ny][nx];
					pq.offer(new Node(nx,ny,d[ny][nx]));
				}
			}
		}		
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		int cnt = 1;
		while (input()) {
			dijkstra();
			System.out.printf("Problem %d: %d\n",cnt,d[N-1][N-1]);
			cnt++;
		}
	}
}
