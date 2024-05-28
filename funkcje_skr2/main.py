# Agata Bartczak 285755
def count_different_bits(hex1, hex2):
    bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
    bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)
    
    diff_count = sum(bit1 != bit2 for bit1, bit2 in zip(bin1, bin2))
    
    return diff_count, len(bin1)

def main():

    hashes = ["md5sum", "sha1sum", "sha224sum", "sha256sum", "sha384sum", "sha512sum", "b2sum"]

    with open("hash.txt", "r") as file:
        lines = file.readlines()
    
    for i in range(0, len(lines), 2):
        hex1 = lines[i].strip().split()[0]
        hex2 = lines[i + 1].strip().split()[0]
        
        diff_count, all_count = count_different_bits(hex1, hex2)
        diff_percent = diff_count / all_count * 100
        
        print(f"cat hash-.pdf personal.txt | {hashes[i//2]}")
        print(f"cat hash-.pdf personal_.txt | {hashes[i//2]}")
        print(f"{lines[i].strip()}\n{lines[i + 1].strip()}")
        print(f"Liczba różniących się bitów: {diff_count} z {all_count}, procentowo: {diff_percent:.2f}%.")
        print()

if __name__ == "__main__":
    main()