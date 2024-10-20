class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # '&':
        #   Initialize result as True.
        #   For each sub-expression inside the parentheses:
        #     If a sub-expression is False, short-circuit and return False.
        # '|':
        #   Initialize result as False.
        #   For each sub-expression inside the parentheses:
        #     If a sub-expression is True, short-circuit.
        # '!':
        #   Return Negation.
        
        idx = [0]

        def helper():
            if expression[idx[0]] == 't':
                idx[0] += 1
                return True
            if expression[idx[0]] == 'f':
                idx[0] += 1
                return False

            if expression[idx[0]] == '&':
                idx[0] += 2
                result = True
                while expression[idx[0]] != ')':
                    if expression[idx[0]] == ',':
                        idx[0] += 1
                    else:
                        result &= helper()
                idx[0] += 1
                return result

            if expression[idx[0]] == '|':
                idx[0] += 2
                result = False
                while expression[idx[0]] != ')':
                    if expression[idx[0]] == ',':
                        idx[0] += 1
                    else:
                        result |= helper()
                idx[0] += 1
                return result

            if expression[idx[0]] == '!':
                idx[0] += 2
                result = not helper()
                idx[0] += 1
                return result

        return helper()
