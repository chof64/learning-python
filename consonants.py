paragraph = """
This planet has—or rather had—a problem, which was this:
most of the people living on it were unhappy for pretty much of the time.
Many solutions were suggested for this problem, but most of these were
largely concerned with the movements of small green pieces of paper, which
is odd because on the whole it wasn't the small green pieces of paper that
were unhappy.
"""

vowels = 0
consonants = 0

for i in paragraph:
  if i in "aeiou":
    vowels += 1
  if i in "bcdfghjklmnpqrstvwxyz":
    consonants += 1

print("The number of vowels is: ", vowels)
print("The number of consonants is: ", consonants)
