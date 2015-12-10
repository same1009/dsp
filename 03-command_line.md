# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
```
pwd - print working directory 
cd - change directory
ls  - list directory contents
     -a all
     -A almost all
     -l long format
     -d details about directory
     -r reverse order
mkdir - create directories
cp - copy files and directory
     -i interactive
     -u update
     -v verbose
mv - move/rename files and directory
cat - displays/copies/combined files
rm - remove files and directories
     -i interactive
     -u update
     -v verbose
less - program is view text files
find - find file
locate - find files by name
xargs - Accepts input from standard in- put and converts it into an argument list for a specified command
wildcards
* Matches any character
? Matches single character
[abc..] Matches characters that are a member in the set
[!abc..] Matches characters that are not a member in the set
[[:class:]] Matches character that are in the class
classes
[:alpha:] - Matches any alphabetic character
[:digit:] - Matches any numeral
[:lower:] - Matches any lowercase letter
[:upper:] - Matches any uppercase letter
```
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > 
```
'ls' lists files and directory 
-a lists all entries
-l lists the long format
-lh lists it in human readable format. 
```

---


---

What does `xargs` do? Give an example of how to use it.

> > 
```
xargs - Accepts input from standard input and converts it into an argument list for a specified command
find /temp -name "*.tmp" | xargs rm
The above will find all .tmp files in the temp folder and feed it into rm. This will remove all .tmp files 
in the /temp folder.
```

---

