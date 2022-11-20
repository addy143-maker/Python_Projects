#function for removing the characters 
def remove_match_char(list1,list2):

    for i in range(len(list1)):
        for j in range(len(list2)):

            #if common character is found 
            #then it will remove that character 
            #and return list of concatenated
            #list with true flag 
            if list[i] == list2[j]:
                c = list1[i]

                #remove character from the list 
                list1.remove(c)
                list2.remove(c)

                #concatentation of two list elements with *
                # * act as border mark here 
                list3 = list1 + ["*"] + list2

                #reutrn its value with the true flag 
                return [list3,True]

# no common character is found 
# return the list with false flag 
    list3 = list1 + ["*"] + list2
    return [list3 , False]
if __name__ == "__main__" :
    # taking first name from user 
    p1 = input("Enter your name :")

    # converting all the letters in uppercase
    p1 = p1.upper()

    #replacing any space with the empty string 
    p1.replace(" ", "")

    #make list of letter or characters 
    p1_list = list(p1)

    #taking second name from the user 
    p2 = input("Enter your partner name :")
    p2 = p2.upper()
    p2.replace(" ","")
    p2_list = list(p2)

    proceed = True

    #keep calling remove_match_char function 
    #until common characters is found or 
    #keep looping until proceed flag is True 
    while proceed :
        ret_list = remove_match_char(p1_list,p2_list)

        con_list = ret_list[0]
        proceed = ret_list[1]

        star_index = con_list.index("*")

        # list slicing perform 
        p1_list = con_list[ : star_index]

        #all character after * store in p2_list
        p2_list = con_list[star_index + 1 :]

    # count total remaining character 
    count = len(p1_list) + len(p2_list)

    # list of FLAMES acronym 
    result = ["Friends", "Love","Affection","Marriage","Enemy","Siblings"]

    #looping until one item is not reamaing in the result list 
    while len(result) > 1 :

        #storing the index value from where we have to perfom slicing 
        split_index = (count % len(result) - 1)

        if split_index >= 0 :

            #list slicing 
            right = result[split_index + 1 :]
            left = result[ : split_index]

            # list concatation 
            result = right + left 
        else :
            result = result [ : len(result) - 1]

    print ("Relationship status is :", result[0])



