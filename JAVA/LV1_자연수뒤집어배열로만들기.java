import java.util.*;
class Solution {
    public int[] solution(long n) {
        ArrayList<Long> answer = new ArrayList<Long>();
        while(n>0){
            answer.add(n%10);
            n=n/10;
        }
        int[] arr = new int[answer.size()];
        int size=0;
        for(long item:answer){
            arr[size++]=(int)item;
        }
        return arr;
    }
}