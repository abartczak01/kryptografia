import hashlib

with open("personal.txt", "r") as personal_file:
    personal_content = personal_file.read().strip()


def calculate_hashes(content):
    hash_functions = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha224": hashlib.sha224(),
        "sha256": hashlib.sha256(),
        "sha384": hashlib.sha384(),
        "sha512": hashlib.sha512(),
        "blake2b": hashlib.blake2b(),
    }

    results = {}
    for name, hash_func in hash_functions.items():
        hash_func.update(content.encode('utf-8'))
        results[name] = hash_func.hexdigest()

    return results

hashes = calculate_hashes(personal_content)

with open("hash.txt", "w+") as hash_file:
    for name in sorted(hashes, key=lambda x: len(hashes[x])):
        hash_file.write(f"{hashes[name]}\n")

print("Skróty zostały obliczone i zapisane do pliku hash.txt")
