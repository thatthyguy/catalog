import os, sys

# To start, let's just list every file in a directory

directory = str(sys.argv[1])
print "Listing files now..."

for f in os.listdir(directory):
    print f
