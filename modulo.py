def caesarCipherEncryptor(string, key):
	new_letters, alphabet, new_key = [], list("abcdefghijklmnopqrstuvwxyz"), key % 25
	for l in string:
		index = alphabet.index(l)
		new_index = index + new_key
		if new_index < 25:
			new_letters.append(alphabet[new_index])
		else:
			new_letters.append(alphabet[new_index % 25])
	return ''.join(new_letters)

caesarCipherEncryptor('abc', 57)