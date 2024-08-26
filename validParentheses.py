# 20. valid parentheses
# given a string s containing just the characters (, ), {, }, [ and ]
# determine if the input string is valid

# an input string is valid if: 
#   open brackets must be closed by the same type of brackets
#   open brackets must be closed in the correct order
#   every close bracket has a corresponding open bracket of the same length

# understand:
#   input: list of strings, elements corresponding to open/closed brackets
#   output: boolean true/false depending on legitimacy of string list of brackets
#   length of list is at least 1

# algorithm:
#   analyze string of brackets. when a closed bracket is encountered, evaluate whether the open
#   bracket that was most recently traversed is the complement of the current bracket
#   e.g. if ) is the current element, check whether the most recent open bracket is (

# EDGE CASES:
#   list length less than or equal to 1
#   a list of only open brackets
#   a list of only closed brackets

def validParentheses(brackets: list[str]) -> bool:
    # create dictionary/hash map of bracket pairs
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack = []

    # one bracket cannot have a complement
    if len(brackets) <= 1:
        return False

    for bracket in brackets:
        # check if the current bracket is in the hash map
        if bracket in pairs:
            # bracket is closed, check if open brackets exist
            if len(stack) == 0:
                return False

            # grab most recent open bracket
            recentOpen = stack.pop()
            # return false if the most recent open bracket is not the 
            # complement of the most recent closed bracket
            if pairs[bracket] != recentOpen:
                return False
        else:
            # bracket is open, push to stack
            stack.append(bracket)

    # return true if list was successfully traversed and stack is empty
    if len(stack) != 0:
        return False
    return True

# time complexity = O(N), corresponding to complete traversal of the string list
# space complexity = O(N), corresponding to the space required by the stack

brackets = ('(', '{', '[', ']', '}', ')')
print(validParentheses(brackets))