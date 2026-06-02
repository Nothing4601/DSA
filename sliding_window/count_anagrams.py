# count no. of anagrams presents in given strings
# Sliding Window:
# Maintain character frequencies of the current window using a dictionary.
# For each window shift:
#   - Subtract 1 from the frequency of the outgoing character.
#   - Add 1 to the frequency of the incoming character.
#   - Remove a character from the dictionary if its frequency becomes 0.
# If the window frequency dictionary matches the pattern frequency
# dictionary, an anagram occurrence is found.

# Time Complexity: O(n)
def make_freq_map(str):
    fre_map={}
    for i in str:
       fre_map[i]=fre_map.get(i,0) +1 # if i i  dict then return it's value othrwise return default number 0
    return fre_map
       
def count_substring_anagrams(s,anagram):

    count =0
    n= len(s)
    k = len(anagram)
    ana_map = {}

    for ch in anagram: # or directly called 'make_freq_map()'
      if ch in ana_map : # searching in map is O(1) 
         ana_map[ch] += 1
      else:
        ana_map[ch] = 1 

    curr_map = make_freq_map(s[:k])

    if curr_map==ana_map: # first window handle differently
       count+=1

    for i in range(n-k):
        curr_map[ s[i] ]-=1
        if curr_map[ s[i] ]==0:
           del curr_map[ s[i] ]
        curr_map[ s[i+k] ]=curr_map.get(s[i+k],0) + 1
        if curr_map==ana_map:
           count+=1
    return count

# using built in counter function to make map
def count_substring_anagrams_2(s,anagrams):
   from collections import Counter
   n=len(s)
   k=len(anagrams)
   ana_map = Counter(anagrams)
   curr_map = Counter(s[:k])
   count = 1 if ana_map==curr_map else 0
   for i in range(n-k):
      curr_map[ s[i] ] -= 1
      curr_map[s[i+k]] += 1
      count = count+1 if ana_map==curr_map else count
   return count

print(count_substring_anagrams('afbcabdfabcabc','abc')) # 6
print(count_substring_anagrams('gatttaathiyttahjtat','att'))# 4

print(count_substring_anagrams_2('afbcabdfabcabc','abc')) # 6
print(count_substring_anagrams_2('gatttaathiyttahjtat','att'))# 4