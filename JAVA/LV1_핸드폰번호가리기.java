class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int len=phone_number.length()-4;
        for(int i=0;i<len;i++){
            answer+='*';
        }
        answer+=phone_number.charAt(len);
        answer+=phone_number.charAt(len+1);
        answer+=phone_number.charAt(len+2);
        answer+=phone_number.charAt(len+3);
        return answer;
    }
}