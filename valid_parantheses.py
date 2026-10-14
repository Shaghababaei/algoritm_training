"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"

Output: true
=====================
Example 2:

Input: s = "()[]{}"

Output: true
=====================
Example 3:

Input: s = "(]"

Output: false
=====================
Example 4:

Input: s = "([])"

Output: true
=====================
Example 5:

Input: s = "([)]"

Output: false
---------------------------------------------
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# # simple 
# def is_valid(value):
#         stack=[]
#         pairs={"(":")","[": "]","{":"}"}
#         for i in value:
#             if i in pairs:
#                     stack.append(i)
#             else:
#                 if stack :  
#                     print(stack)  
#                     if pairs[stack[-1]]==i:
#                         stack.pop()
#                     else:
#                         return False
#                 else: 
#                      return False
#         # if stack:
#         #     return False
#         # else:
#         #     return True  
#         return not stack        


# pro
def is_valid(value):
        pairs={")":"(","}":"{","]":"["}
        stack=[]
        if len(value)%2 :
                return False
        for i in value:
                if i not in pairs:
                    stack.append(i)
                
                elif not stack or stack.pop() != pairs[i]:
                        return False
        
        return not stack
        

print(is_valid("([])"))