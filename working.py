# def first_non_repeating_char(s: str) -> str:
#     temp =""
#     char = ""
#     for i in range(len(s)):
#         temp = s[i]
#         if temp == s[i+1]:
#             char = temp
#             continue
#         else:
#             if char == temp:
#                 continue
#             else:
#                 return temp

# a=first_non_repeating_char("aabbccde") 
# print(a)

# def first_non_repeating_char(s: str) -> str:
#     print(s.count())
#     # for ch in s:
#     #     c = s.count(ch)
        
#     #     if c == 1:
#     #         return ch
        
# a=first_non_repeating_char("abcd") 
# print(a)   
