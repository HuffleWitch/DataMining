#Template for Assignment 1.
#Author:
#Date:
#Note: This implementation is not very efficient. 
# Hint: @lru_cache(maxsize=None) is likely to be a 
#   favourable decoration for some functions.


#Computes the support of the given itemset in the given database.
#itemset: A set of items
#database: A list of sets of items
#return: The number of sets in the database which itemset is a subset of. 
def support(itemset, database):


#Computes the confidence of a given rule.
#The rule takes the form precedent --> antecedent
#precedent: A set of items
#antecedent: A set of items that is a superset of precedent
#database: a list of sets of items.
#return: The confidence in precedent --> antecedent.
def confidence(precedent, antecedent, database):    

#Finds all itemsets in database that have at least minSupport.
#database: A list of sets of items.
#minSupport: an integer > 1
#return: A list of sets of items, such that 
#   s in return --> support(s,database) >= minSupport.
def findFrequentItemsets(database, minSupport):
                
    
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


#Produces a visualization of frequent itemsets.
def visualizeItemsets(frequentItemsets):
    return 0

#Produces a visualization of rules.
def visualizeRules(rules):
    return 0


#Here's a simple test case:

database = (frozenset([1,2,3]), frozenset([2,3]), frozenset([4,5]), frozenset([1,2]), frozenset([1,5]))
out = findFrequentItemsets(database, 2)
print(out) #should print something containing sets {1},{2},{3},{5},{1,2}, and {2,3}.

#Should print something like {2} ===> {1,2}, {1} ===> {1,2}, {3} ===> {2,3}, and {2} === {2,3}
for r in findRules(out, database,0.4):
    print(str(r[0])+"  ===>   "+str(r[1]))