class Solution {
    public int solution(int a, int b) {
        String aStr = Integer.toString(a);
        String bStr = Integer.toString(b);
        String ab = aStr + bStr;
        String ba = bStr + aStr;
        int ab1 = Integer.parseInt(ab);
        int ba1 = Integer.parseInt(ba);
        int answer;
        if (ab1 > ba1) {
            answer = ab1;
        } else {
            answer = ba1;
        }

        return answer;
    }
}