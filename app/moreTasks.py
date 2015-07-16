def count_words(arr):
    n = len(arr)
    defalut_data = {}

    for i in range(0, n):
        br = 0
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                br += 1
        default_data.update({arr[i]: br})
return default_data


def unique_words_count(arr):
    b = set(arr)
    return len(b)


def nan_expand(times):
    s = []
    br = 0
    while br < times:
        s.append("Not a ")
        br += 1
    s.append("NaN")
str1 = ''.join(s)
return str1

if __name__ == "__main__":
    nan_expand()


def iterations_of_nan_expand(expanded):
    br = 0
    for i in expanded:
        if "Not a" in expanded:
            br += 1
return br


# def prime_factorization(n):


def group(group1):
    n = len(group1)
    q = []
    q1 = []
    for i in range(0, n):
    	br = 0
    	for j in range(i + 1, n):
    		if group1[i] == group1[i + 1]:
    			br += 1
    		if group[i] != group[i + 1]:
    			z = 0
    			for i1 in range(0, br):
    				q.insert(z, i)
    				z += 1
    	q1.append(q)
 return q1

 def max_consecutive(items):
 	str1=items
 	br1=0
 	n=len(items)
 	for i in range (0,n):
 		br=0
 		for j in range(i+1,n):
 			if(str1[i]==str1[j]):
 				br+=1
 			if(str1[i]!=str1[j]):
 				if (br1<br):
 					br1=br
 					break
return br1

def groupby(func, seq):
	dictionary={} #dictionary.update({i:str1})!
	s=[]
	#for element in seq:
		#y=func(seq)
		#for i in seq:
		#strip -> maha space-ove
		
	#	y=func(element)
	#	for 
     y=max(seq)
     z=func(max)
     for element in range (0,z-1):
     	position=0
     	if element>= seq[element]:
     		if seq[element]%element==0:
     			s.insert(position,seq[element])
     			position+=1
     		if element<seq[element]:
     			if seq[element]%element==0:
     				s.insert(position,seq[element])
     				position+=1
     	

















