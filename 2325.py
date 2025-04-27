import string


class Solution(object):
    def decodeMessage(self, key, message):
        # key = key.replace(" ","")
        # dic = {}
        # for i in key:
        #     dic[i] = True
        # key = ''
        # for i in dic:
        #     key += i
        # dic={k:v for (k,v) in zip(key,string.ascii_lowercase)}
        # res = ''
        # for i in range(len(message)):
        #     if message[i] == ' ':
        #         res += message[i]
        #     else:
        #         res += dic[message[i]]
        # return res
        # Remove spaces from the key and keep the order of unique characters
        key = ''.join(dict.fromkeys(key.replace(" ", "")))

        # Create a mapping from characters in the key to the alphabet
        mapping = {k: v for k, v in zip(key, string.ascii_lowercase)}

        # Decode the message using the created mapping
        decoded_message = ''.join([mapping[char] if char != ' ' else ' ' for char in message])

        return decoded_message


sol = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(sol.decodeMessage(key,message))
