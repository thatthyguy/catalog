import os, sys

def full_file_listing(directory):
    for f in os.listdir(directory):
        if ".pdf" in f:
            print os.path.join(directory, f)

if __name__ == '__main__':

    directory = str(sys.argv[1])
    print "Listing files now..."
    full_file_listing(directory)
