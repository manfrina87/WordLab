
# Anagrams

**Purpose:** find which word is an anagram of another word

**Input:** list of words

## Hello World


```python
from anagrams import anagrammer

words=['python', 'tyhphon', 'typhon']
anagrammer(words)
```




    [('NOT an ANAGRAM', 'python', 'tyhphon'),
     ('ANAGRAM found', 'python', 'typhon'),
     ('NOT an ANAGRAM', 'tyhphon', 'typhon')]



## Palyndromes

**Purpose:** find if a word is palyndrome

**Input:** Word as a string


```python
from palindromes import palyndromer

pword='satorarepotenetoperarotas'
palyndromer(pword)
```




    'Char IS palindrome'


