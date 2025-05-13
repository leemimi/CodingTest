import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, (f1, f2) -> {
            String[] file1 = splitFile(f1);
            String[] file2 = splitFile(f2);

            // HEAD 비교 (대소문자 무시)
            int headCompare = file1[0].toLowerCase().compareTo(file2[0].toLowerCase());
            if (headCompare != 0) {
                return headCompare;
            }

            // NUMBER 비교 (숫자 크기 비교)
            int num1 = Integer.parseInt(file1[1]);
            int num2 = Integer.parseInt(file2[1]);
            return num1 - num2;
        });

        return files;
    }

    // 파일명을 HEAD, NUMBER, TAIL 로 나누는 메서드
    private String[] splitFile(String file) {
        int idx = 0;
        int len = file.length();

        // HEAD
        while (idx < len && !Character.isDigit(file.charAt(idx))) {
            idx++;
        }
        String head = file.substring(0, idx);

        // NUMBER
        int numberStart = idx;
        while (idx < len && Character.isDigit(file.charAt(idx)) && idx - numberStart < 5) {
            idx++;
        }
        String number = file.substring(numberStart, idx);

        // 나머지 부분은 필요 없으므로 안 잘라도 됨
        return new String[]{head, number};
    }
}
