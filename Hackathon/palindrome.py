def palindrome(name):
    """ Extended slice syntax [begin:end:step] """
    if len(name) < 80:
        reverse = name[::-1]
        if name == reverse:
            print "Indeed"
        else:
            print "Not At All"
	    		
# MAIN
if __name__ == '__main__':
    name = raw_input()
    palindrome(name)

