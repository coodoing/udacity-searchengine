#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
 if t == s:
  return 0

 subject,word = t,s
 if len(s) > len(t):
  subject,word = s,t

 #print "subject is " + subject + "(" + str(len(subject)) + ")"
 #print "word is " + word + "(" + str(len(word)) + ")"

 i = 0
 matches = {}
 while i < len(word):
#  print "trying new letter " + word[i] + " at " + str(i)
  matched = 0

  hits = find_all(subject,word[i])
#  print "trying letter '" + word[i] + "' in '" + subject + "'"

  if len(hits) > 0:

   updates = hits
   while len(updates) > 0 and matched < len(word):

    matched += 1

#    print "trying all '" + word[i:(i+matched+1)] + "' in '" + subject + "' (" + str(matched) + ")"

    updates = find_all(subject,word[i:(i+matched+1)])
#    print "Findings for " + word[i:(i+matched+1)]
#    print updates
#    print "Hits for letter " + word[i]
#    print hits

    if len(updates) > 0:
#     print "before Update"
#     print hits
     for offset in updates:
      if len(updates[offset]) > len(hits[offset]):
       hits[offset] = updates[offset]

#     print "Updated hits "
#    print hits

#   print "Copying " + str(len(hits)) + " to matches..."
   for offset in hits:
    if offset not in matches or len(hits[offset]) > len(matches[offset]):
     matches[offset] = hits[offset]

#   print "Matches till now"
#   print matches
  i += 1


# wenn best am anfang oder am ende steht, muss nicht bewegt werden!

# print "subtstr find:"
 #print matches

 max_list = {}
 for m in matches:
  key = len(matches[m])
  if key not in max_list:
   max_list[key] = []

  max_list[key].append(matches[m])

 best = get_next_best(max_list)

 while best:
#  print "testing <" + best + ">"

# wenn best jeweils am anfang oder am ende bei word und subject...
  same_start = word.find(best) == subject.find(best)
  same_end = (word.find(best) + len(best)) == len(word) and (subject.find(best) + len(best)) == len(subject)

  if same_start or same_end:
   cost = 0

  else:
   cost = len(subject)
   cost = subject.find(best) - word.find(best)
   if cost < 0:
    cost = cost * -1

  if cost >= len(best):
   best = get_next_best(max_list)
  else:
#   print "Super, <" + best+"> " + str(len(best)) + " chars match, losing " + str(cost) + " to move them in place (" + str(len(best) - cost) + ") totals " + str(len(subject) - len(best) + cost) + " [" + str(len(subject)) + "]"
   return (len(subject) - len(best) + cost)


 return len(subject)

def find_all(string, fragment):
 matches = {}
 match = string.find(fragment)
 while match > -1:
  matches[match] = fragment
  match = string.find(fragment,(match+1))

 return matches


def get_next_best(max_list):
 max = -1
 next = None
 for i in max_list:
  if i >= max:
   max = i

 if max > -1:
  next = max_list[max].pop()
  if len(max_list[max]) == 0:
   del max_list[max]
 return next


print(edit_distance("polliijhneziaxaxa","uzuxomanxallipo"))

print (edit_distance('audacity', 'udacity'))
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print (edit_distance('audacity', 'Udacity'))
#>>> 2

# Five replacements
print( edit_distance('peter', 'sarah'))
#>>> 5

# One deletion
print(edit_distance('pete', 'peter'))
#>>> 1

#two deletion
#print (edit_distance("s","sss"))
# One deletion)
#print (edit_distance('pete', 'peter'))
