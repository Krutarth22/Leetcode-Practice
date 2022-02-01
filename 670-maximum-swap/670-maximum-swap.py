class Solution:
    def maximumSwap(self, num: int) -> int:
        
        
        
        num = [str(d) for d in str(num)]
        max_ind, first_ind, second_ind = len(num)-1, 0, 0
        for i in range(len(num)-1,-1,-1):
            if(num[i]>num[max_ind]):    
                max_ind = i
                
            if(num[i]<num[max_ind]):    #if num[i] can be replaced with max_num on the right
                first_ind = i      
                second_ind = max_ind   
                
        num[first_ind],num[second_ind] = num[second_ind], num[first_ind]
       
        return("".join(num))