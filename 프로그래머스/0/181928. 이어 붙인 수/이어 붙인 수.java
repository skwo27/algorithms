class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String a = "";
        String b = "";
        String c;
        for (int i = 0 ; i < num_list.length ; i++) {
            if (num_list[i] % 2 == 0 ) {
                c = num_list[i] + "";
                a += c;
            } else {
                c = num_list[i] + "";
                b += c;
            }
        }
        int a1 = Integer.parseInt(a);
        int b1 = Integer.parseInt(b);
        answer += a1 + b1;
        return answer;
    }
}