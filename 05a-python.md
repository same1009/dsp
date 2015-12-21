# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> 
You can store values in both lists and tuples. Tuples are immutable while lists are mutable. Tuples is a sequence where the position have meaning while a list is generally dealt with on an individual element basis. Since keys have to be immutable, tuples will worl as keys in dictionaries. An long explanation can be found here: https://docs.python.org/2/faq/design.html

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 
You can store values in both lists and sets. You cannot store duplicate values in a set and there is no index in a set. The performance of sets are generally better due to sets using a hashtable. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 
A lambda function is a function that takes any number of arguments and returns the value of a single expression. An example of a lambda function is below: <br>
Dict={'a':10,'b':9,'c':7} <br>
sorted (Dict,key=lambda x:Dict[x])


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehensions are constructs that allow sequences to be built from other sequences. <br>
mylist=[1,2,3,4] <br>
squared=[x**2 for x in mylist if x%2==0] <br>
x**2 is the output expression<br>
x is the variable<br>
mylist is the input sequence<br>
the if statement is the optional predicate<br>
Below is an example of map and filter:<br>
filter(lambda x: x%2 == 0, mylist) <br>
map(lambda x: x**2, mylist) <br>
Filter applies a predicate to a sequence, and map modifies each member of a sequence. <br>
Set comprehensions allow sets to be constructed using the same principles as list comprehensions, the only difference is that resulting sequence is a set.<br>
{ x**2 for x in mylist if x%2==0 } <br>
Below is a example of a dictionary comprehensions:<br>
MyDict = {'a':1, 'b': 2, 'c': 3, 'd':4} <br>
mcase_frequency = { k: MyDict.get(k, 0) for k in MyDict.keys() if MyDict[k]%2==0}



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





