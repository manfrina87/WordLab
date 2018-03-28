
# Anagrams

**Purpose:** Find which word is an anagram of another word

**Input:** A list of words

**Output:** A list of tuples (message, word1, word2)

```python
[('NOT an ANAGRAM', 'python', 'tyhphon'),
('ANAGRAM found', 'python', 'typhon'),
('NOT an ANAGRAM', 'tyhphon', 'typhon')]
```

## Hello World


```python
from anagrams import anagrammer

words=['python', 'tyhphon', 'typhon']
anagrammer(words)
```


