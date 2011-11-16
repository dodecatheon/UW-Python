#!/usr/bin/env python
"""
Assignment for week 6, Tues Nov 15, bring exercise to turn in (hardcopy)

Write a function unlisted_words that takes two string arguments, a
sample string and a reference string, and returns a list of all the
words that appear in the sample string that do not appear in the
reference string.  A word is a string of alphabetic characters (with
no spaces, numbers, or punctuation), where case is not significant (so
python, Python and PYTHON are the same word).  The output list must
not contain duplicates, each word must appear only once.

Write the function in a module also called unlisted_words that
contains a short sample string and a short reference string for
testing (so it is obvious from the returned list whether the function
is working correctly).  The module calls the function on these strings
and prints the returned list.

The module also reads a large sample string and a large reference
string (from a file or a web page, for example), calls the function on
them, and prints the output.  You may choose the sources for the
reference and sample strings yourself, or you may use these: sample:
http://staff.washington.edu/jon/uw_python/fall_2011/big.txt reference:
http://staff.washington.edu/jon/uw_python/fall_2011/words
"""
import re
def words(s, alphanumeric=False):
    "s is a string.  Returns set of lowercase words in s"
    if alphanumeric:
        # restrict word characters to a through z
        return set(re.findall(r'[a-z]+',s.lower()))
    else:
        # allow any \w word character
        return set(re.findall(r'\w+',s.lower()))

def unlisted_words(sample, reference):
    """\
sample is the string containing words to be tested.
reference is the string containing the words to be checked as reference.
Returns a list of words (sorted) that appear in the sample but not in
the reference string.
"""
    l = list(words(sample) - words(reference))
    l.sort()
    return l

# Make the sample strings "private" to this module by prefixing them with
# a single underscore.
_s = 'MaRy haD a LiTTle LamB'
_r = """\
This is a long string of words, some of which may be present in the sample
string.  I had better include at least one or two little commonalities
"""

def test_unlisted_words(sample=_s,
                        reference=_r):
    "Run unlisted_words on a small test"
    sl = len(sample)
    if sl > 40:
        sl = 40
    print "First 40 chars of sample:", sample[:sl]
    print "Words of sample that are not in the reference string:"
    print unlisted_words(sample, reference)

def big_test(f1='big.txt', f2='words'):
    test_unlisted_words(open(f1).read(),
                        open(f2).read())

if __name__ == "__main__":
    # commandline execution, for debugging
    import sys
    if len(sys.argv) == 3:
        test_unlisted_words(s=sys.argv[1], t=sys.argv[2])
    else:
        test_unlisted_words()
else:
    # imported execution as per spec:
    test_unlisted_words()
    
