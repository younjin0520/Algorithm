import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int j=0;j<commands.length;j++){
            int[] command=commands[j];
            int start=command[0]-1;
            int end=command[1];
            int[] arr=new int[end-start];
            for(int i=start;i<end;i++){
                arr[i-start]=array[i];
            }
            Arrays.sort(arr);
            answer[j]=arr[command[2]-1];
        }
        return answer;
    }
}