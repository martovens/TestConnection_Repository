import time

sample = input("Input Text: ")
keyword = input("Search for word: ")

global match_counter, found_array, found_string, counter, found_counter

counter = 0
match_counter = 0
found_array = []
found_string = ""
found_counter = 0

print("[Text]: " + sample)




for i in sample:
    #print("[Text]: ",sample[counter])

    if match_counter < len(keyword): # if all matches have not been found yet
        if ord(sample[counter]) == ord(keyword[match_counter]): # if characters match

            #important stuff
            found_array.append(counter) #append match value's index to be evaluated later
            match_counter = match_counter + 1 #numerical value added if match found
            found_string = found_string + sample[counter] #continate for end result presentation

            if match_counter > 1: #if more than one match
                if found_array[match_counter-1] - found_array[match_counter-2] == 1: #if the distance between matching char <1
                    found_counter += 1
                    print(True, "\nCurrent Found: ", found_array,"\n", "Found_Counter: ", found_counter)
                else:
                    print("Resetting... \n", "Difference: ",found_array[match_counter-1] - found_array[match_counter-2])
                    found_array = []
                    match_counter = 0
                    found_string = ""

            #output stuff
            #print("\nMatch Counter: ", match_counter)
            #print("Found Keyword: ", sample[counter], "\nMatch Counter: ", match_counter, "\nString Index: ", counter-1, "\n ") # printing out letter found, the letter index respective to keyword, and the placement in string

    else:
        match_counter = 0 #reset to find new word
        print("Reset")


    #other stuff
    counter = counter + 1 #observe next letter
    #time.sleep(.01)


print(len(keyword))
print("Found keyword: {}".format(keyword))

time.sleep(5000)

x







#for i in sample:
#    print(i, sample.index('{}'.format(str(i)))) #turn i into string to be found in sample
