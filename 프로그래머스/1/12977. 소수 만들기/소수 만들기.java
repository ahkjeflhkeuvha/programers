class Solution {
   public int solution(int[] nums) {
      int answer = 0;
      boolean check = false;

      for (int i = 0; i < nums.length; i++) 
         for (int j = i + 1; j < nums.length; j++) 
            for (int k = j + 1; k < nums.length; k++) 
               if (decimal(nums[i] + nums[j] + nums[k])) answer++;
                
      return answer;
   }
   
   public boolean decimal(int num) {
      boolean check = true; 
      if(num==2)  return check;
      for(int i=2; i<num; i++) {
         if(num%i ==0) {
            check = false; break;
         }
      }
      return check;
   }
}