import java.util.*;
class Solution {
    public int solution(int[] a) {
    int n = a.length;
    int[] leftMin = new int[n];
    int[] rightMin = new int[n];

    // 왼쪽 최소값
    int min = a[0];
    leftMin[0] = a[0];
    for (int i = 1; i < n; i++) {
        min = Math.min(min, a[i]);
        leftMin[i] = min;
    }

    // 오른쪽 최소값
    min = a[n - 1];
    rightMin[n - 1] = a[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        min = Math.min(min, a[i]);
        rightMin[i] = min;
    }

    // 풍선을 남길 수 있는 경우
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] <= leftMin[i] || a[i] <= rightMin[i]) {
            count++;
        }
    }

    return count;
}
}
