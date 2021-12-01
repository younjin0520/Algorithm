class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int num=0; int zero=0; int max=0; int min=0;
        for(int lotto:lottos){
            for(int win:win_nums){
                if(win==lotto){
                    num++;
                    break;
                }
            }
            if(lotto==0){
                zero++;
            }
        }
        max=7-(num+zero);
        min=7-num;
        if(max>6){
            max=6;
        }
        if(min>6){
            min=6;
        }
        answer[0]=max;
        answer[1]=min;
        return answer;
    }
}