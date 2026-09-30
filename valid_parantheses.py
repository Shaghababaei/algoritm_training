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


# def is_valid(stringg:str):
#     validator={}
#     for i in stringg:
#         if i not in validator:
#             validator[i] = 1
#         else : 
#             validator[i] +=1

#     if validator.get('(',0) == validator.get(')',0) and validator.get('{',0) == (validator.get('}',0)) and (validator.get('[',0) == validator.get(']',0)) :
#         return True 
#     return False

def is_valid(value):
    if len(value)%2==0 and value[0] != (')',']','}'):
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack=[]
        boolian = False
        for i in value:
            stack.append(value(i))
            if value[i] == (')',']','}') and value[i-1]== pairs[i]:
               boolian==true
               return True
    else:
        return False        
           

print(is_valid(")("))