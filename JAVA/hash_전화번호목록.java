import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        for(int i=0;i<phone_book.length-1;i++){
            int l=phone_book[i].length();
            if(l<=phone_book[i+1].length()&&phone_book[i].equals(phone_book[i+1].substring(0,l))){
                answer=false;
            }
        }
        return answer;
    }
}