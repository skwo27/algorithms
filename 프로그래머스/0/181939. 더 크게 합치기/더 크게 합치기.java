class Solution {
    public int solution(int a, int b) {
        // Convert integers to strings
        String aStr = Integer.toString(a);
        String bStr = Integer.toString(b);

        // Concatenate the strings
        String ab = aStr + bStr;
        String ba = bStr + aStr;

        // Parse the concatenated string back to integer
        int ab1 = Integer.parseInt(ab);
        int ba1 = Integer.parseInt(ba);

        // Declare the answer variable
        int answer;
        
        // Determine which concatenation gives a larger number
        if (ab1 > ba1) {
            answer = ab1;
        } else {
            answer = ba1;
        }

        return answer;
    }
}