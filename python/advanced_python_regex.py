import csv

class ParseCSV:

  def __init__(self):
    self.raw_data='faculty.csv'
    self.parsed_data=[]
    self.degrees_freq={}
    self.titles_freq={}
    self.emails=[]
    self.domains={}

  def read_data(self):
    with open(self.raw_data,'r') as f: #open file in read only mode
      csvreader=csv.reader(f)
      for row in csvreader:
        self.parsed_data.append([r.strip() for r in row])

  def diff_degrees(self):
    degree_index=self.parsed_data[0].index('degree')
    list_of_degrees=[x[degree_index]for x in self.parsed_data[1:]]
    
    # is PhD and Ph.D the same??
    # remove '.', separate multiple degrees
    for i in list_of_degrees:
      for j in i.split():
        temp=j.strip().replace('.','')
        self.degrees_freq[temp]=self.degrees_freq.get(temp,0)+1
        # if temp in self.degrees_freq.keys():
        #   self.degrees_freq[temp]=self.degrees_freq[temp]+1
        # else:
        #   self.degrees_freq[temp]=1

  def diff_titles(self):
    title_index=self.parsed_data[0].index('title')
    list_of_titles=[x[title_index]for x in self.parsed_data[1:]]
    for i in list_of_titles:
      temp=i[0:i.find('Professor')+len('Professor')]
      self.titles_freq[temp]=self.titles_freq.get(temp,0)+1
      # if (temp in self.titles_freq.keys()):
      #   self.titles_freq[temp]=self.titles_freq[temp]+1
      # else:
      #   self.titles_freq[temp]=1

  def extract_emails(self):
    email_index=self.parsed_data[0].index('email')
    list_of_emails=[x[email_index]for x in self.parsed_data[1:]]
    self.emails=list_of_emails
  
  def extract_domains(self):
    for i in self.emails:
      temp= i[i.find('@')+1:]
      self.domains[temp]=self.domains.get(temp,0)+1
      # if (temp in self.domains.keys()):
      #   self.domains[temp]=self.domains[temp]+1
      # else:
      #   self.domains[temp]=1

def parsedata():
  a=ParseCSV()
  a.read_data()
  return a

def q_1234(a):
  a.diff_degrees()
  print 'Question 1'
  print a.degrees_freq
  a.diff_titles()
  print 'Question 2'
  print a.titles_freq
  a.extract_emails()
  print 'Question 3'
  print a.emails
  a.extract_domains()
  print 'Question 4'
  print a.domains

if __name__ == "__main__":
  parse_obj=parsedata()
  q_1234(parse_obj)


