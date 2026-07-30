class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def buildStr(n, NOB, s, res=None):
            if res is None:
                res = []

            if len(s) == 2*n:
                res.append(s)
                return res

            if 2*n - len(s) <= NOB:
                pass
            else:
                NOB += 1
                s += '('
                buildStr(n, NOB, s, res)
                NOB -= 1
                s = s[:-1]

            if NOB == 0:
                pass
            else:
                NOB -= 1
                s += ')'
                buildStr(n, NOB, s, res)
                NOB += 1
                s = s[:-1]

            return res

        str = ''
        no_Open_Brackets = 0

        return buildStr(n, no_Open_Brackets, str)

        
