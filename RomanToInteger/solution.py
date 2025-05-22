class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = [1, 5, 10, 50, 100, 500, 1000]
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = 0
        previndex =0
        prevnum =0
        for i in list(s):
            getindex = symbol.index(i)
            if getindex > previndex:
               num = num - 2*prevnum
            num += value[getindex]
            prevnum = value[getindex]
            previndex = getindex

        return num