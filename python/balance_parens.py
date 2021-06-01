def balance_parens(str):    
    if len(str) == 0:
        return str 
    
    # input will be a string with letters, numbers, or parens
    balanced_str = ""
    open_parens_index_list = []

    # loop through entire string
    for c in enumerate(str):

        # if we get an opening parens.... then we MAY have a closing parens buddy
        if c == "(":
            # append index of open parens
            open_parens_index_list.append(len(balanced_str))

        # if we get a closing parens... check if there was a opening parens buddy
        elif c == ")":
            if len(open_parens_index_list) > 0:
                open_parens_index_list.pop()
            else:
                continue

        # append if we get a letter, number, or opening parens
        balanced_str += c

    # if there are no unmatched open parens, we're done! (avoid extra work)
    if len(open_parens_index_list) == 0:
        return balanced_str

    fully_balanced_str = ""
    for i, c in enumerate(balanced_str):
        # if the index isn't found in our leftover list, add it to our final output
        if i not in open_parens_index_list:
            fully_balanced_str += c

    # return value should be a string (balanced)
    return fully_balanced_str
