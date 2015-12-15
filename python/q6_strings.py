# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    try:
      a=int(count)          
      if (count<0):                 #Checks for integer
        raise NotImplementedError
      elif (count>=10):             #more than 10
        print "many"
      else:                         #more than 0, less than 10
        print 'Number of donuts: %s' %(count)
    except NotImplementedError:
      print "Less than 0"
    except:
      print 'Not a number'

donuts(-40)
donuts (9)
donuts(10)
donuts('1')
donuts('t')

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    try:
      if (isinstance(s, basestring)==False):    #checks for string
        raise NotImplementedError
      if(len(s)<2):                   
        print ""
      else:                                   
        print s[0:2]+s[-2:len(s)]               #splits string
    except NotImplementedError:
      print 'not a string'

both_ends('hellohhh')
both_ends('123456789')
both_ends([1,2])


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    try:
      if (isinstance(s, basestring)==False):        #checks for string
        raise NotImplementedError
      temp=s[0]
      new_string=s.replace(temp,'*')                #replaces chars with *
      print new_string.replace('*',temp,1)          #replaces first * with char 
    except NotImplementedError:
      print 'not a string' 
      
fix_start('hellohejuhjh')
fix_start([1,1])

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    # a
    # b
    try:
      if (isinstance(a, basestring) & isinstance(b, basestring)==False):
        raise NotImplementedError
      else:
        print b[0:2]+a[2:len(a)]+' '+a[0:2]+b[2:len(b)]
    except NotImplementedError:
      print 'not a string'

mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('pezzy', 'firm')
mix_up(1,'jeuu')

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    try:
      if (isinstance(s, basestring)==False):
        raise NotImplementedError
      if(len(s)<3):                     #checks if length is less than 3
        print s
      elif(s[-3:len(s)]=="ing"):        #checks if it ends in "ing"
        print s+'ly'
      else:   
        print s+'ing'           
    except NotImplementedError:
      print 'not a string'

verbing('hail')
verbing('swiming')
verbing('do')
verbing([1,2])

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    try:
      if (isinstance(s, basestring)==False):
        raise NotImplementedError
      if((s.find('bad')>s.find('not')) & (s.find('not')>0)):      #Checks if "not" exists and if it comes before "bad"
        print s[0:s.find('not')]+'good'+s[s.find('bad')+3:len(s)]
      else:
        print s
    except NotImplementedError:
      print 'not a string'

not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")
not_bad("It's bad")
not_bad([12])

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    if(len(a)%2==1):
      x=1
    else:
      x=0
    if(len(b)%2==1):
      y=1
    else:
      y=0

    a_front=a[0:len(a)/2+x]
    a_back=a[len(a)/2+x:len(a)]
    b_front=b[0:len(b)/2+y]
    b_back=b[len(b)/2+y:len(b)]

    print a_front+b_front+a_back+b_back

front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')

