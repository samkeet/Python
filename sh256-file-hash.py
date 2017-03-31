import hashlib

def getHash():
	m = hashlib.sha256()
	file = input("Enter file name: ")
	source_hash = input("Enter SHA256 from source: ")
	with open(file, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			m.update(chunk)
	if source_hash == m.hexdigest():
		print("Valid")
	else:
		print("Corrupt File")

if __name__ == '__main__':
	getHash()
