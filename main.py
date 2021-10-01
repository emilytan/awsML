# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Wine Refactoring
df = pd.read_csv('winequality-red.csv', sep=';')
# print(df)
for label in df.columns:
  labels = label.replace(' ', '_')
  # print('labels: ', labels)

df.columns = [label.replace(' ', '_') for label in df.columns]
# print('df.columns: ', df.columns)

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low'

for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    # print(df.groupby(feature).quality.mean(), '\n')


# Common Books
import time
import numpy as np

with open('books-published-last-two-years.txt') as f:
    recent_books = f.read().split('\n')
    # print('recent_books', recent_books)
    print(len(recent_books))

with open('all-coding-books.txt') as f:
    coding_books = f.read().split('\n')
    # print('coding_books', coding_books)
    print(len(coding_books))

start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# refactor code for time efficiency
start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# refactor code for time efficiency
start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))


# Holiday Gift
import time
import numpy as np
with open('gift-costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)
print('gift-costs', gift_costs)

start = time.time()
total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax
print('total_price', total_price)
print('Duration: {} seconds'.format(time.time() - start))

# refactor code for time efficiency
start = time.time()
total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print('total_price', total_price)
print('Duration: {} seconds'.format(time.time() - start))
