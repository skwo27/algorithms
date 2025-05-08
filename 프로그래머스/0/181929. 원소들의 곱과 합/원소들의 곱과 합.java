class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int a = 1;
        int b = 0;
        for (int i = 0 ; i < num_list.length ; i++) {
            a*=num_list[i];
        }
        for (int i = 0 ; i < num_list.length ; i++) {
            b+=num_list[i];
        }
        b*=b;
        answer = a>b ? 0 :  1;
        return answer;
    }
}