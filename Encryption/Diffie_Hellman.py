from random import randint

if __name__ == '__main__':

	# Both the persons will be agreed upon the 
	# public keys G and P 
	# A prime number P is taken 
	P = int(input("[?] Enter a prime number P: "))
	
	# A primitve root for P, G is taken
	G = int(input("[?] Enter a primitve root for P: "))
	
	
	print('[*] The Value of P is :%d'%(P))
	print('[*] The Value of G is :%d'%(G))
	
	# Alice will choose the private key a 
	a = int(input("Choose A Private Key for A: "))
	print('[*] The Private Key a for A is :%d'%(a))
	
	# gets the generated key
	x = int(pow(G,a,P)) 
	
	# Bob will choose the private key b
	b = int(input("Choose A Private Key for B: "))
	print('The Private Key b for B is :%d'%(b))
	
	# gets the generated key
	y = int(pow(G,b,P)) 
	
	
	# Secret key for Alice 
	ka = int(pow(y,a,P))
	
	# Secret key for Bob 
	kb = int(pow(x,b,P))
	
	print('Secret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))
