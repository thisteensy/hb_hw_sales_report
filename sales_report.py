"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # creates an empty list
melons_sold = [] # creates an empty list

f = open('sales-report.txt') # opens the text file and assigns the text to a file
for line in f:  #iterates through each line in f
    line = line.rstrip() #  removes any trailing white space.
    entries = line.split('|') # take a line and removes the delimiter and 
                                # turns it into a list of elements from the line

    salesperson = entries[0] # assigns each element of entries at index 0 to 
                            # the variable salespeople
                                #this is a terrible idea, because it separates the sales person
                                # from their data
    melons = int(entries[2]) # converts each element of entries at index 2 to 
                            # an integer and assigns it to the variable melons

    # This seems like a good place to say that lines 13 and 14 should not be done.
    # Rather a nested dicitionary should be created with salesperson as the key and 
    # their corresponding data set to key:value pairs in dictionaries assigned as values of salesperson
    # in this case, since we only care about the number of melons sold it could be as 
    # easy as a simple dictionary with key = salesperson, value = melons_sold
    
    if salesperson in salespeople: #checks to see if a sales person has already
                                    # been added to a list called salespeople
        position = salespeople.index(salesperson) # this finds the element in
                                                # the list salespeople at index
                                                # sales person
        melons_sold[position] += melons # adds the number of melons (from the same line) 
                                        # to melons_sold at index position
        # They are attempting to line up the data in the same order in the separate lists,
        # again, there is a much simpler way to do this with a dictionary.
    else:
        salespeople.append(salesperson) #adds the salesperson to the list salespeople
        melons_sold.append(melons) #adds the number of melons to the list melons_sold


for i in range(len(salespeople)): # iterates through a range of integers that is the length
                                    # of the number of elements in salespeople
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # prints the statement
                                    #salesperson at index i sold the number of 
                                    # melons from melons_sold at index i
