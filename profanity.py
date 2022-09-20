#Let the name of the file be twitter_file.txt

#Let the list of profane words be called as profanity_list
profanity_list = ['Nigger', 'Brownie', 'Blackie', 'Paleface', 'Pikey', 'Pocahontas', 'Prod', 'Roundeye']
p_dict = {}
# We will create a dictionary to store the value of degree of profanity, with the sentence that it is calculatd for.
with open('twitter_file.txt','r') as file:  
    # reading each line of the twitter file    
    for line in file:
        # we will use a metric of calculating the number of profane words
        # a sentence contains and append it to the dictionary p_dict
        degree_of_profanity = 0
        # reading each word in every line after splitting the line 
        for word in line.split():
            for i in profanity_list:
                if word == i:
                    degree_of_profanity += 1
        p_dict[line] = degree_of_profanity
file.close()