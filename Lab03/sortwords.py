def sortwords(wordstring):
    wordlist = wordstring.split("-")
    wordlist = sorted(wordlist)
    ans = ""
    for word in wordlist:
        ans += word+"-"
    return ans[0:-1]
        

wordstring = input("Enter hyphen separated list of words: ")
print("Sorted:",sortwords(wordstring))
