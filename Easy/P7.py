class Solution:
    def reverse(self, x: int) -> int:

        string = str(x)
        if string[0] != '-':
            string = int(string[::-1])
            if string >= 2_147_483_647:
                return 0
            else:
                return string
        else:
            string = string[1::]
            string = string[::-1]
            string = - int(string)
            if string <= -2_147_483_647:
                return 0
            else:
                return string

