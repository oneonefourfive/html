import  re
p = r'\w+@\w+\.com'
r = r"\d+"
em  = '123a@a31231231.com'
m=re.match(p,em)
m=re.findall(p,em)
m=re.search(p,em)
m=re.sub(r,' ',em)

#m=re.split(r,em,maxsplit= 1)
print(m)