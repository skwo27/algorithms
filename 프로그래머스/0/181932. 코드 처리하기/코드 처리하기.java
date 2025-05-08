class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        for(int i = 0 ; i < code.length() ; i++) {
            if (code.charAt(i) == '1') {
                if (mode == 0) {
                    mode = 1;
                } else {
                    mode = 0;
                }

            } else {
                switch (mode) {
                    case 0:
                        if (i % 2 == 0) {
                            answer = answer + code.charAt(i);
                        }
                        break;
                    case 1:
                        if (i % 2 != 0) {
                            answer = answer + code.charAt(i);
                        }
                }
            }
        }
        return answer.isEmpty() ? "EMPTY" : answer;
    }
}