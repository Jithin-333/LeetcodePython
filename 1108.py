class Solution(object):
    def defangIPaddr(self, address):
        address = address.replace('.','[.]')
        return address


address = "1.1.1.1"
sol = Solution()
print(sol.defangIPaddr(address))