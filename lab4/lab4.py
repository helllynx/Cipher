import bz2
import os


path = 'text/3'
zip_name = 'textzip.myzip'


fmt = '{:>15}  {:>15}'
print(fmt.format('len(data)', 'len(compressed)'))
print(fmt.format('-' * 15, '-' * 15))

with open(path+'.txt', 'rb') as file:
    bfile = file.read()

    output = bz2.BZ2File(zip_name, 'wb')
    try:
        output.write(bz2.compress(bfile))
    finally:
        output.close()

    # os.system('file '+zip_name)

    file.close()




with bz2.BZ2File(zip_name, 'rb') as file:

    output = open(path+'_decompressed.txt', 'wb')
    try:
        output.write(bz2.decompress(file.read()))
    finally:
        output.close()

    # os.system(path+'_decompressed.txt')

    file.close()


print("==============INPUT============")
os.system('hexdump '+path+".txt")
print("==============COMPRESS============")
os.system('hexdump '+zip_name)



original_data = b'This is the original text.'


for i in range(5):
    data = original_data * i
    compressed = bz2.compress(data)
    print(fmt.format(len(data), len(compressed)), end='')
    print('*' if len(data) < len(compressed) else '')
