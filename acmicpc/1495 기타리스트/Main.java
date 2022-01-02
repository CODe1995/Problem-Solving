package boj1495;

import java.util.*;
import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int songs, startVolume, masterVolume, volumes[];

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		songs = Integer.parseInt(st.nextToken());
		startVolume = Integer.parseInt(st.nextToken());
		masterVolume = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		volumes = new int[songs];
		for (int i = 0; i < songs; i++) {
			volumes[i] = Integer.parseInt(st.nextToken());
		}
	}

	static void play() {
		boolean dp[][] = new boolean[songs+1][masterVolume+1];
		dp[0][startVolume] = true;

		for (int i = 1; i <= songs; i++) {
			for (int j = 0; j <= masterVolume; j++) {
				if (!dp[i-1][j])
					continue;
				if (j - volumes[i-1] >= 0)
					dp[i][j - volumes[i-1]] = true;
				if (j + volumes[i-1] <= masterVolume)
					dp[i][j + volumes[i-1]] = true;				
			}
		}
		
		int answer = -1;
		for (int i = masterVolume; i>=0;i--) {
			if(dp[songs][i]) {
				answer = i;
				break;
			}
		}
		System.out.println(answer);
		
	}

	public static void main(String[] args) throws IOException {
		input();
		play();
	}
}