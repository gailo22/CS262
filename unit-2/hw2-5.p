
def gcd(a, b):
	if a == b : return a
	if a > b : return gcd(a-b,b)
	if a < b : return gcd(a,b-a)

print gcd(24,8)
print gcd(1362,1407)
print gcd(1875,1907)
print gcd(45,116)
