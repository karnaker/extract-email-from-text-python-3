# Extracts email addresses from one or more plain text files.
# Outputs the email addresses to a list in a CSV file.
# Example command line use: winpty python extract_emails_from_text.py test.txt
#
# Notes:
# - Does not check for duplicates (which can easily be done in the terminal).
#
# Original file: Dennis Ideler <ideler.dennis@gmail.com>
# Modified file: Frederic Pierron <fpierron@gmail.com>
# Author of current file: Vikram Karnaker

from optparse import OptionParser
import os.path
import time
import re

#removed the ' from re.compile string, otherwise it adds the ' to the email
#regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
#                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
#                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

regex = re.compile(("([a-z0-9!#$%&*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def file_to_str(filename):
    """Returns the contents of filename as a string."""
    with open(filename) as f:
        return f.read().lower() # Case is lowered to prevent regex mismatches.

def get_emails(s):
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def add_to_file(myFile, email):
	"""Save in a text file the emails extracted """
	with open(myFile,"a") as emailsfile:
            emailsfile.write(email+"\n")

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    # No options added yet. Add them here if you ever need them.
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isfile(arg):
            # create file to export emails
            extensionTime = time.strftime("%H%M%S")
            myFile = "emailList_"+extensionTime+".csv"
            # regex emails
            for email in get_emails(file_to_str(arg)):
                print (email)
                add_to_file(myFile, email)

        else:
            print ('"{}" is not a file.'.format(arg))
            parser.print_usage()
