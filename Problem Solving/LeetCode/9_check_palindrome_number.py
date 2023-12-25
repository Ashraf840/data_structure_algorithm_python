x = 535

class CheckPalindrome:
    def __init__(self, num):
        self.num = num
    
    def reverseNumber(self):
        num_clone = self.num
        reverse_number = 0
        while num_clone != 0:
            temp = num_clone % 10
            reverse_number = reverse_number * 10 + temp
            num_clone = num_clone // 10
        return reverse_number
    
    def isPalindrome(self):
        if self.num == self.reverseNumber(): return True
        else: return False

checkPalindrome = CheckPalindrome(x)
if checkPalindrome.isPalindrome():
    print(f"{x} is a palindrome!")
else:
    print(f"{x} is not a palindrome!")