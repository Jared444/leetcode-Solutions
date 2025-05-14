class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        for i in range(len(str(x))):
            length = len(str(x))
            front_num = str(x)[i]
            back_num = str(x)[length - (i +1)]
            if (front_num != back_num):
                return False
        
        return True
            