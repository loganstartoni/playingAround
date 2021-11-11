import calendar
import itertools
import random
import re
import string

from collections import Counter
from pprint import pprint as pp
from timeit import timeit

import requests

# Day 1
# Get a list of Names
names = "pybites mike bob julian tim sara guido ross wendy andy charles".split()
print(names)

# Loop over list of Names
for name in names:
    print(name.title())

# Only get names from first half of the alphabet
first_half_of_alphabet = list(string.ascii_lowercase[:13])
print(first_half_of_alphabet)

new_names = []
for name in names:
    if name[0] in first_half_of_alphabet:
        new_names.append(name.title())

print(new_names)

# list comprehensions sort names
new_names_comprehension = [name.title() for name in names if name[0] in first_half_of_alphabet]
print(new_names_comprehension)

assert new_names_comprehension == new_names

# load in Harry Potter
resp = requests.get("https://projects.bobbelderbos.com/pcc/harry.txt")
words = resp.text.lower().split()
if not resp.ok:
    from listComprehensionsAndGenerators_sourceFile import harry
    words = harry.lower().split()
print(words)
print(len(words))

# Setup a counter
cnt = Counter(words)
print(cnt.most_common(5))

# remove non-alphanumerics
print('-' in words)
words = [re.sub(r'\W+', r'', word) for word in words]
print('-' in words)

# get a list of stopwords
resp = requests.get("https://projects.bobbelderbos.com/pcc/stopwords.txt")
stopwords = resp.text.lower().split()
if not resp.ok:
    from listComprehensionsAndGenerators_sourceFile import stopwords
    stopwords = stopwords.lower().split()
print(words)
print(len(words))

# Remove Stop Words
words = [word for word in words if word not in stopwords and word.strip()]
print('the' in words)

cnt = Counter(words)
print(cnt.most_common(5))


# Generators
def num_gen():
    for i in range(5):
        yield i


gen = num_gen()

print(next(gen))

for i in gen:
    print(i)

try:
    print(next(gen))
except StopIteration:
    print("No More Values")

# No exception because for handles for us
for i in gen:
    print(i)

gen = num_gen()
for i in gen:
    print(i)


# Generators to build a sequence
options = 'red yellow blue white black green purple'.split()


def create_select_options(options:list = options):
    select_list = []

    for option in options:
        select_list.append(f"<option value={option}>{option.title()}</option>")

    return select_list


pp(create_select_options())


def create_select_options_gen(options: list = options):
    for option in options:
        yield f"<option value={option}>{option.title()}</option>"


print(create_select_options_gen())
print(list(create_select_options_gen()))


# Compare lists and Generators in performance
default_iterations: int = 1000000
# List Version
def leap_years_lst(n: int = default_iterations):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years


# Generator Version
def leap_years_gen(n: int = default_iterations):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year


print(timeit(leap_years_lst, number=2))
print(timeit(leap_years_gen, number=2))


# Day 2
# Practice
NAMES = ["arnold schwarzenegger", "alec baldwin", "bob belderbos",
         "julian swqueira", "sandra bullock", "keanu reaves",
         "julbob pybytes", "bob belderbos", "julian sequira",
         "al pacino", "brad pitt", "matt damon", "brad pitt"]

# list comprehension convert names to title case
title_names = [name.title() for name in NAMES]
print(title_names)

# list comprehension reverse name order
reversed_names = [name.split().reverse() for name in NAMES]
print(reversed_names)


# Create a generator to randomly select 2 names from the list and print the sentance ___ teams up with ____
def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        first_name, second_name = None, None
        while first_name == second_name:
             first_name, second_name = random.SystemRandom().choices(first_names, k=2)
        yield  f"{first_name} teams up with {second_name}"


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))


islice = itertools.islice(pairs, 10)

pp(list(islice))
