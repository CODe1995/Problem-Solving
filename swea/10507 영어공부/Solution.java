package swea10507_영어공부;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int P = Integer.parseInt(st.nextToken());
			int studyDays[] = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				studyDays[i] = Integer.parseInt(st.nextToken());
			}
			int remainP = P;
			int left = 0;
			int right = left + 1;
			int answer = 0;
			while (left <= right && right < N) {
				int diff = studyDays[right] - studyDays[right-1] - 1;
				if (left == right) {
					right++;
				} else if (diff <= remainP) {
					// rightIndex+1
					remainP -= diff;
					answer = Integer.max(studyDays[right] - studyDays[left] + 1 + remainP, answer);
					right++;
				} else {
					// leftIndex+1
					int gap = studyDays[left + 1] - studyDays[left] - 1;
					if (gap <= P)
						remainP += gap;
					left++;
				}
			}
			if (answer == 0) {
				answer = P + 1;
			}
			sb.append("#").append(tc).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
