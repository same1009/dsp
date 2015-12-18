import csv
import advanced_python_regex as apr

def csv_writer(path,list_emails):
  with open(path, "wb") as csv_file:
      writer = csv.writer(csv_file)
      for line in sorted(list_emails):
        print line
        writer.writerow([line])

def q5():
  print 'question 5'
  a=apr.parsedata()
  a.extract_emails()
  csv_writer("emails.csv",a.emails)

q5()