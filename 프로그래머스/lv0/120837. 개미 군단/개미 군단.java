class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        int ant = 5;
        while (true){
            if (hp<=0){
                break;
            }
            answer += hp/ant;
            hp = hp%ant;
            ant = ant -2;
        }
        return answer;
    }
}