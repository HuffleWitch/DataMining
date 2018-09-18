import csv


# create an array of all authors in the csv file
def create_array(filename):
    # create array and counters to aid looping
    authors = []
    author_count = 0
    row_count = 0

    # open csv file and read
    f = open(filename)
    csv_f = csv.reader(f)

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

print(str(create_array('ACM Authors.csv')))

