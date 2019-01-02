class Solution:
    
    def if_all_prefix(self, strs, n, small_world, low, mid):
        
        for i in range(len(n)):
            str_1 = strs[i]
            for j in range(len(low, mid+1)):
                if str_1[j] != small_world[j]:
                    return False
        return True
    
    def longestCommonPrefix(self, strs):
        def if_all_prefix(strs, n, small_world, low, mid):
        
            for i in range(n):
                str_1 = strs[i]
                for j in range(low, mid+1):
                    if str_1[j] != small_world[j]:
                        return False
            return True
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) != 0:
            l = len(min(strs, key = len))
            
        else:
            return result
           
        low = 0
        high = l-1
        
        while low <= high:
            mid = low + (high - low) // 2
            if (if_all_prefix(strs, len(strs), strs[0], low, mid)):
                result += strs[0][low:mid+1]
                low = mid +1 
            else:
                high = mid -1
        return result
                
        
            
        
    
