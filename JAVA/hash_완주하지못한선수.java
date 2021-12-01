import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer>map=new HashMap<>();
        //³Ö±â
        for(String p : participant){
            if(map.get(p)==null){
                map.put(p,1);
            }else{
                int num=map.get(p)+1;
                map.put(p,num);
            }
        }
        for(String c:completion){
            int num=map.get(c)-1;
            map.put(c,num);
        }
        for(String key:map.keySet()){
            if(map.get(key)==1){
                answer=key;
            }
        }
        return answer;
    }
}