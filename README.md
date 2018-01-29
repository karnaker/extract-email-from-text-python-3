# Extract email addresses from TXT and output to CSV
Extract email addresses from a text file and output as a list in a CSV file.
Works with python 3.

**Known bug:**
Large text files may see the following error:
```
Traceback (most recent call last):
  File "extract_emails_from_text.py", line 58, in <module>
    print (email)
IOError: [Errno 0] Error
```

**Forks and References:**
* [Forked from Frederic Pierron ](https://github.com/fredericpierron/extract-email-from-text-python-3)
* [Base script used by Frederic Pierron ](https://gist.github.com/dideler/5219706)
