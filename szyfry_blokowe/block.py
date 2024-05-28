import hashlib
import random
from PIL import Image

# Agata Bartczak 285755

class ImageEncryptor:
    def __init__(self, input_image_path, block_size):
        self.input_image = Image.open(input_image_path).convert('L')
        self.block_size = block_size
        self.image_data = self.input_image.tobytes()
        self.size = self.input_image.size
        self.key = self._random_key()

    def _random_key(self):
        return bytearray([random.randint(0, 255) for _ in range(self.block_size ** 2)])

    def _take_block(self, x, y):
        block = bytearray(self.block_size * self.block_size)
        for i in range(self.block_size):
            for j in range(self.block_size):
                pos = (x + i) * self.size[1] + y + j
                if pos < self.size[0] * self.size[1]:
                    block[i * self.block_size + j] = self.image_data[pos]
        return block

    def _build_block(self, encrypted, x, y, encrypted_block):
        for i in range(self.block_size):
            for j in range(self.block_size):
                elem = encrypted_block[i * self.block_size + j]
                pos = (x + i) * self.size[1] + y + j
                if pos < self.size[0] * self.size[1]:
                    encrypted[pos] = elem

    def save_image(self, encrypted_image, path):
        img = Image.new('L', self.size)
        img.frombytes(bytes(encrypted_image))
        img.save(path)

    def ecb_encrypt(self):
        encrypted_image = bytearray(self.size[0] * self.size[1])
        for x in range(0, self.size[0], self.block_size):
            for y in range(0, self.size[1], self.block_size):
                encrypted_block = self._encrypt_block(self._take_block(x, y))
                self._build_block(encrypted_image, x, y, encrypted_block)
        return encrypted_image

    def cbc_encrypt(self):
        initialization_vector = bytearray([random.randint(0, 255) for _ in range(self.block_size * self.block_size)])
        hash_obj = hashlib.shake_256()
        encrypted_image = bytearray(self.size[0] * self.size[1])
        for x_position in range(0, self.size[0], self.block_size):
            for y_position in range(0, self.size[1], self.block_size):
                block = self._take_block(x_position, y_position)
                encrypted_block = self._encrypt_block(block)
                xor_result = bytearray([x ^ y for x, y in zip(encrypted_block, initialization_vector)])
                hash_obj.update(xor_result + self.key)
                initialization_vector = hash_obj.digest(self.block_size * self.block_size)
                self._build_block(encrypted_image, x_position, y_position, xor_result)
        return encrypted_image

    def _encrypt_block(self, block):
        return bytearray([x ^ y for x, y in zip(block, self.key)])


encryptor = ImageEncryptor(input_image_path="plain.bmp", block_size=8)

encryptor.save_image(encryptor.ecb_encrypt(), 'ecb_crypto.bmp')
encryptor.save_image(encryptor.cbc_encrypt(), 'cbc_crypto.bmp')