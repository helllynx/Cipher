## Lab 4

David A. Huffman


```angular2html
import heapq
import os


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


    def __lt__(self, other):
        if (other == None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        if(self.freq > other.freq):
            return True

    def __gt__(self, other):
        if (other == None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        if(self.freq < other.freq):
            return True


class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # functions for compression:

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if (len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print("Compressed")
        return output_path

    """ functions for decompression: """

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            try:
                byte = file.read(1)
                while (byte!=0):
                    byte = ord(byte)
                    bits = bin(byte)[2:].rjust(8, '0')
                    bit_string += bits
                    byte = file.read(1)
            except:
                pass

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output.write(decompressed_text)

        print("Decompressed")
        return output_path
```


 **Test hexdump for small file**
 
 ```angular2html
==============INPUT============
0000000 b1d0 b5d0 b3d0 83d1 82d1 d020 d0bd d0b5
0000010 d0b2 d1b5 d080 d1bd d08b 20b5 b4d0 bdd0
0000020 b5d0 b2d0 bdd0 8bd1 b5d0 d120 d082 d0b5
0000030 d0bd 2eb8 0a0d b2d0 8bd1 81d1 bed0 bad0
0000040 d020 20b8 b2d0 bdd0 8fd1 82d1 b5d0 bdd0
0000050 d020 d0ba d0be d0bb d0be d0ba d0be d1bb
0000060 d08c d1bd d08b 20b9 b7d0 bed0 b2d0 0d2e
0000070 d00a d0be d0b7 d1b0 d080 d0b5 d1bd 208b
0000080 86d1 b5d0 80d1 bad0 bed0 b2d0 bdd0 8bd1
0000090 b5d0 d120 d181 d182 d083 d0bf d0b5 d0bd
00000a0 2cb8 0a0d b8d0 85d1 d020 d0ba d0b0 d0bc
00000b0 d0b5 d1bd 208c b6d0 b8d0 b2d0 e220 9480
00000c0 d020 20b8 b6d0 b4d0 91d1 82d1 d120 d082
00000d0 d0b2 d0be d1b8 2085 88d1 b0d0 b3d0 bed0
00000e0 b2d0 002e                              
00000e3
==============COMPRESS============
0000000 5a42 3968 4131 2659 5953 90e0 423c 0000
0000010 7f1b c3ff d462 d55b 2450 757e 5c44 4330
0000020 af48 c81c 8418 f425 2068 0038 4ff0 5c00
0000030 1a02 a058 7400 0d38 0019 8306 0340 0040
0000040 3468 9906 000d d3c8 2146 a8e9 d370 504f
0000050 a0c9 a101 18a0 4383 4646 2083 8106 07a0
0000060 0da8 d301 a450 2379 fa81 c2b2 e0aa 153b
0000070 630e 6464 4ac4 4277 88a2 d300 ee99 969a
0000080 18dd 342b 2f17 2bbc ab9b 87a5 0aa5 b631
0000090 d914 b112 6fba 9114 6a6a e410 9cba 057a
00000a0 b490 5712 1907 8943 c3cc 5d15 24ba 744c
00000b0 2b9a 8bcf b0cf f4e7 3726 837f 65ab 0625
00000c0 2af2 e469 5541 837c a0d5 109e f72d b07d
00000d0 0184 708d c53f 91dc 144e 3824 0f24 8010
00000e0
```

