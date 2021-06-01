def balance_parens(array):
    holder = []
    output = ''

    for x in array:
        if not(x == '(' or x == ')'):
            output += x

        elif (x == '('):
            output += x
            holder.append(len(output)-1)

        elif (x == ')'):
            if holder != []:
                holder.pop()
                output += x
    
    if len(holder) > 0:
        count = 0
        for x in holder:
            output = output[0:x-count] + output[(x-count+1):]
            count += 1


    return output
