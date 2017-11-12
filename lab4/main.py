from huffman import HuffmanCoding

#input file path
path = "/home/yenq/MIET/LABS/Cipher/lab4/text/3.txt"

h = HuffmanCoding(path)

output_path = h.compress()


h.decompress(output_path)
