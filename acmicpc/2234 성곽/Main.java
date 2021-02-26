package boj2234;
import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N,M,field[][],roomNum=0,visited[][],direction[][]= new int[][]{{1,0},{0,1},{-1,0},{0,-1}};	//동남서북
	static int maxRoom;
	static ArrayList<Integer> saveRoomCnt = new ArrayList<>();//각 방 갯수 저장
	static HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();//연결그래프
	static class Pos{
		int x,y;
		public Pos(int x, int y) {this.x = x;this.y = y;}
	}
	static void bfs(int x,int y) {
		roomNum++;
		int roomCnt=0;//방 갯수
		visited[y][x]=roomNum;
		Deque<Pos> dq = new ArrayDeque<>();
		dq.add(new Pos(x,y));
		while(!dq.isEmpty()) {
			roomCnt++;
			Pos cur = dq.pollFirst();
			for(int d=0;d<4;d++) {//
				int[] dir = direction[d];
				int nx = cur.x+dir[0];
				int ny = cur.y+dir[1];				
				if(nx<0 || nx>=M || ny<0 || ny>=N || visited[ny][nx]!=0)continue;
				if((field[ny][nx]&(1<<d))==(1<<d))continue;//가는 방향에 벽이 있다?
				dq.add(new Pos(nx,ny));
				visited[ny][nx]=roomNum;
			}
		}
		saveRoomCnt.add(roomCnt);//각 방의 갯수 저장
		maxRoom = Math.max(maxRoom, roomCnt);
	}
	static void makeGraph(int x,int y) {//그래프생성
		for(int[] dir:direction) {
			int nx = x+dir[0];
			int ny = y+dir[1];
			if(nx<0 || nx>=M || ny<0 || ny>=N || visited[ny][nx]==visited[y][x])continue;//같은 방이면 취소
			//다른 방이 나오면 여기로 들어오게 된다.
			int	cur = visited[y][x]-1;
			int next = visited[ny][nx]-1;
			if(graph.get(cur)==null||!graph.get(cur).contains(next)) {//아직 등록안되었다면
				graph.get(cur).add(next);
				graph.get(next).add(cur);//양방향그래프
			}
		}
	}
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		M = stoi(st.nextToken());
		N = stoi(st.nextToken());		
		field = new int[N][M];
		visited = new int[N][M];//방을 번호로 기록해둔거, 방문확인도 가능
		for(int i =0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0;j<M;j++)field[i][j]=stoi(st.nextToken());
		}
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				if(visited[i][j]==0)
					bfs(j,i);
			}
		}		
		for(int i=0;i<roomNum;i++) {
			graph.put(i, new ArrayList<Integer>());//그래프 init			
		}
		for(int i =0;i<N;i++)for(int j =0;j<M;j++) {
			makeGraph(j,i);//그래프 연결하기
		}
		int maxBreakSize = 0;		
		for(int i =0;i<graph.size();i++) {//모든 그래프 탐색
			for(Integer x:graph.get(i)) {//ArrayList하나씩 꺼내옴
				maxBreakSize = Math.max(saveRoomCnt.get(x)+saveRoomCnt.get(i), maxBreakSize);
			}
		}
		
		
		sb.append(roomNum).append("\n").append(maxRoom).append("\n").append(maxBreakSize).append("\n");
		System.out.println(sb);
		
		//  0001 서쪽벽 : 동쪽방향으로 갈 때
		//	0010 북쪽벽 : 남쪽방향으로 갈 때
		//	0100 동쪽벽 : 서쪽방향으로 갈 때
		//	1000 남쪽벽 : 북쪽방향으로 갈 때
	}
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
}