def balance_parens(str):    
    if str == "":
        return str 
    
    # input will be a string with letters, numbers, or parens
    balanced_str = ""
    open_parens_index_list = []

    # loop through entire string
    for i, c in enumerate(str):
        #print(i)

        # if we get an opening parens.... then we MAY have a closing parens buddy
        if c == "(":
            # append index of open parens
            open_parens_index_list.append(len(balanced_str))
            #print(balanced_str, open_parens_index_list)

        # if we get a closing parens... check if there was a opening parens buddy
        elif c == ")":
            if len(open_parens_index_list) > 0:
                open_parens_index_list.pop()
                #print(balanced_str, open_parens_index_list)
            else:
                continue

        # append if we get a letter, number, or opening parens
        balanced_str += c

        # added logic here

    #print("leftover open parens")
    #print(open_parens_index_list)

    # if there are no unmatched open parens, we're done!
    if len(open_parens_index_list) == 0:
        return balanced_str

    fully_balanced_str = ""
    for i, c in enumerate(balanced_str):
        if i not in open_parens_index_list:
            fully_balanced_str += c

    # return value should be a string (balanced)
    return fully_balanced_str


#output = balance_parens("((a(b)c(((") # should return "a(b)c"
#print(output)