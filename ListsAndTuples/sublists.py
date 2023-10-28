thelist = [1,4,1,2]

sublistset = [thelist[i:j] for i in range(len(thelist)) for j in range(i+1,len(thelist)+1)]

print(sublistset)
