#Template for Assignment 1.
#Author: Skylar Lingenfelser
#Note: This implementation is not very efficient. 
# Hint: @lru_cache(maxsize=None) is likely to be a 
#   favourable decoration for some functions.


#import csv
#file = open('ACMAuthors.csv')
#database = csv.reader(file)

database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([1,2,4]),
            frozenset([3, 4]), frozenset([1,2,5]), frozenset([1,2,4,5]),
            frozenset([1,2]), frozenset([2,3,4]), frozenset([1,4,5]))

def ItemsfromDatabase(database):
    power_set = []
    for row in database:
        for column in row:
            if column not in power_set:
                power_set.append(column)
#    power_set.sort()
    return power_set

p1 = ItemsfromDatabase(database)
print ("ItemsfromDatabase")
print(p1)

    

#Computes the support of the given itemset in the given database.
#itemset: A set of items
#database: A list of sets of items
#return: The number of sets in the database which itemset is a subset of.
def support(itemset, database):
    len_set = len(database)
    count = 0
    for row in database:
        for column in row:
            if column == itemset:
                count = count + 1
    return count
    support = (freq_set/count)
    print ("The support is:" + str (support))
    return support

    
    

#Computes the confidence of a given rule.
#The rule takes the form precedent --> antecedent
#precedent: A set of items
#antecedent: A set of items that is a superset of precedent
#database: a list of sets of items.
#return: The confidence in precedent --> antecedent.

def confidence(precedent, antecedent, database):
    ante_support = support(antecedent, database)
    pre_support = support(precedent, database)
    confidence = (ante_support/pre_support)
    return confidence


#Finds all itemsets in database that have at least minSupport.
#database: A list of sets of items.
#minSupport: an integer > 1
#return: A list of sets of items, such that 
#   s in return --> support(s,database) >= minSupport.
def findFrequentItemsets(database, minSupport):
    FS = []
    for row in database:
        FS.append([row])
    cands = FS
    while len(cands) > 0:
        H = []
        for c in cands:
            if support(c, database) >= minSupport:
                H.append(c)
        cands = []
        FS = FS + H
    print ("FS")
    return FS
                
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
    setFreq = frequentItemsets.copy()
    for s in frequentItemsets:
        setFreq.remove(s)
        for t in setFreq:
            if confidence(s, setFreq.append(t), database) >= minConfidence:
                rules.append((s,t))
    return rules
            
        

#Produces a visualization of frequent itemsets.
def visualizeItemsets(frequentItemsets):
    return 0

#Produces a visualization of rules.
def visualizeRules(rules):
    return 0


#Here's a simple test case:

#database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([4,5]), frozenset([1,2]), frozenset([1,5]))
out = findFrequentItemsets(database, 2)
print ("Freq Items")
print(out) #should print something containing sets {1},{2},{3},{5},{1,2}, and {2,3}.

#Should print something like {2} ===> {1,2}, {1} ===> {1,2}, {3} ===> {2,3}, and {2} === {2,3}
for r in findRules(out, database, 0.4):
    print ("rules")
    print(str(r[0])+"  ===>   "+str(r[1]))
