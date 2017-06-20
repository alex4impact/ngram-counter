# Import the csv module
import csv

# Import the counter module
from collections import Counter

# Set the length of the ngram
n = 3

# Set the number of common ngrams to return
c = 3

# Define the ngrams function
def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

print('----------------------------------------------')

# Read from csv file
with open ('sample-email.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Add contents of the body field to full_text
        full_text = row['body']
        email = row['email']

        # Convert all text to lowercase
        full_text = str.lower(full_text)

        # Split words in email
        words = full_text.split()

        # Add words to the list 'input_list'
        input_list = list(words)

        # Invoke the ngrams function
        ngram_list = find_ngrams(input_list,n)

        # Tally occurrences of ngrams for this piece of text
        cnt = Counter(ngram_list)

        # Print the email address
        print (email)

        # Print the number of items in the list
        print ('There are '+str(sum(cnt.values()))+' '+str(n)+'-grams in the file.')

        # Print the full list of n-grams
        print ('The full set of '+str(n)+'-grams is:')
        print (Counter(cnt))

        # Print the most common phrases
        print ('The '+str(c)+' most common '+str(n)+'-grams are: ',(Counter(cnt).most_common(c)))

        print('----------------------------------------------')

        continue
