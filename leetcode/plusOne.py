class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits

    def plusOne(self, digits):
        tmp = 1
        for i in range(len(digits))[::-1]:
            digits[i] += tmp
            tmp = digits[i] / 10
            digits[i] = digits[i] % 10
        if tmp > 0:
            digits.insert(0, tmp)
        return digits
