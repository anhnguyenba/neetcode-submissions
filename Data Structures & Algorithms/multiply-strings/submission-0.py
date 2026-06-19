class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')
        if not num1 or not num2:
            return "0"

        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        result = 0
        k = 0
        for d1 in num1[::-1]:
            v = 0
            subprod = 0
            carry = 0
            for i, d2 in enumerate(num2[::-1]):
                p = int(d1) * int(d2)
                mod = p % 10 if i < len(num2) - 1 else p
                subprod += (mod + carry) * (10 ** v)
                v += 1
                carry = p // 10
            result += subprod * (10 ** k)
            k += 1

        return str(result)
