#Template for Assignment 1.
#Author: Skylar Lingenfelser
#Note: This implementation is not very efficient. 
# Hint: @lru_cache(maxsize=None) is likely to be a 
#   favourable decoration for some functions.
import csv
# database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([4,5]), frozenset([1,2]), frozenset([1,5]))


# create an array of all authors in the csv file
def create_array(filename):
    # create array and counters to aid looping
    authors = []
    author_count = 0
    row_count = 0

    # open csv file and read
    f = open(filename)
    csv_f = csv.reader(f, delimiter ='\t')

    # loop through the file
    for row in csv_f:
        for column in row:
            # check if the author is new
            if column not in authors:
                # if new, add to authors array
                authors.append(column)
                author_count = author_count + 1
            row_count = row_count + 1
    return authors

# create an array of itemsets from the database
def itemsets(filename):
    # create array
    itemsets = []
    # open the file and read
    f = open(filename)
    csv_f = csv.reader(f, delimiter='\t')

    # loop through the file
    for row in csv_f:
        if row not in itemsets:
            itemsets.append([row])
    return itemsets

# database = str(create_array('tinyAuthors.csv'))
# print(database)

# database = [[1], [1], [1], [1], [1], [1,2,3], [2,3], [2,3], [2,3], [2,3], [2,3], [1,2,4],
#             [3, 4], [1,2,5], [1,2,4,5],
#             [1,2], [2,3,4], [1,4,5], [1,4,5], [1,4,5], [1,4,5]]

database = [[6], [6],[6],[6],[6],[6],[6],[6], [8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [10, 12, 14], 
    [5,7], [5,7], [5,7], [7,9], [9, 6], [12, 14], [12, 11, 13], [12, 11, 13],[12, 11, 13], 
    [12, 11, 13], [12, 11, 13], [12, 11, 13], [12, 11, 13], [12, 11, 13], [1], [1], [1], 
    [1], [1], [1,2,3], [2,3], [2,3], [2,3], [2,3], [2,3], [1,2,4],[6,8], [6,8], [6,8], [6,8],
    [3, 4], [1,2,5], [1,2,4,5],[1,2], [2,3,4], [1,4,5], [1,4,5], [1,4,5], [1,4,5], [1,4,5], [1,4,5]
    ,[1,4,5], [1,4,5], [1,4,5], [1,4,5], [1,4,5], [1,4,5],[6],[6],[6],[6],[6],[6], [2,3], [2,3], [2,3], [2,3],
    [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8]
    , [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8]
    , [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8], [6,8]]

# database = itemsets('tinyAuthors.csv')
# print("Item Sets: \n ")
# print(database)

#this function creates the powerset of the database
def ItemsfromDatabase(database):
    power_set = []
    for row in database:
        for column in row:
            if column not in power_set:
                power_set.append(column)
    temp_set = []
    for item in power_set:
        for thing in power_set:
            if item != thing:
                if [item, thing] and [thing, item] not in temp_set:
                    temp_set.append([item, thing])
    power_set.extend(temp_set)
    return power_set

# p1 = ItemsfromDatabase(database)
# print("Power Set: \n ")
# print(p1)

    

#Computes the support of the given itemset in the given database., 
# used in a loop to get the support of all
# items in the powerset against the 
#itemset: A set of items
#database: A list of sets of items
#return: The number of sets in the database which itemset is a subset of.
#support works!!
def support(itemset, database):
    len_set = len(database)
    itemset_len = len(itemset)
    count = 0
    for item in database:
        for element in itemset:
            item_check = 1
            if element not in item:
                break
            else:
                item_check += 1

        if item_check == itemset_len:     
            count = count + 1
    support = (count/len_set)
    return support

# s1 = support([6,8], database)
# print("Support: \n ")
# print(s1)
    

#Computes the confidence of a given rule.
#The rule takes the form precedent --> antecedent
#precedent: A set of items
#antecedent: A set of items that is a superset of precedent
#database: a list of sets of items.
#return: The confidence in precedent --> antecedent.
# 
def confidence(precedent, antecedent, database):
    ante_support = support(antecedent, database)
    pre_support = support(precedent, database)
    confidence = (ante_support/pre_support)
    return confidence

# print("confidence")
# print(confidence([6], [6,8], database))



#Finds all itemsets in database that have at least minSupport.
#database: A list of sets of items.
#minSupport: an integer > 1
#return: A list of sets of items, such that 
#   s in return --> support(s,database) >= minSupport.
def findFrequentItemsets(database, minSupport):
    cands = database
    for x in range(len(cands)+1):
        H = []
        for c in cands:
            if (c not in H and support(c, database) >= minSupport):
                H.append(c)
    frequent_sets = H
    frequent_sets.sort()
    return frequent_sets

print("Frequent Sets: \n ")
freq_sets= findFrequentItemsets(database, .1)
print(freq_sets)


#Given a set of frequently occuring Itemsets, returns
# a list of pairs of the form (precedent, antecedent)
# such that for every returned pair, the rule 
# precedent --> antecedent has confidence >= minConfidence
# in the database.
#frequentItemsets: a set or list of sets of items.
#database: A list of sets of items.
#minConfidence: A real value between 0.0 and 1.0. 
#return: A set or list of pairs of sets of items.

def findRules(frequentItemsets, database, minConfidence):
    rules = []
    for s in frequentItemsets:
        for t in frequentItemsets:
            if (s != t and confidence(s, t, database) >= minConfidence):
                rules.append((s,t))
    return rules


rules = findRules(freq_sets, database, .5)
print("rules",rules)


#Produces a visualization of frequent itemsets.
def visualizeItemsets(frequentItemsets):
    return 0

#Produces a visualization of rules.
def visualizeRules(rules):
    return 0


#Here's a simple test case:


# database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([4,5]), 
#     frozenset([1,2]), frozenset([1,5]))

#database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([4,5]), frozenset([1,2]), frozenset([1,5]))

# out = findFrequentItemsets(database, 2)
# print ("Freq Items")
# print(out) #should print something containing sets {1},{2},{3},{5},{1,2}, and {2,3}.

#Should print something like {2} ===> {1,2}, {1} ===> {1,2}, {3} ===> {2,3}, and {2} === {2,3}
# for r in findRules(out, database, 0.4):
#     print ("rules")
#     print(str(r[0])+"  ===>   "+str(r[1]))
