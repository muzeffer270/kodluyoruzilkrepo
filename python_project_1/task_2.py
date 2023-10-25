# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

sample_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(sample_list_2):
    reversed_list = []
    for item in sample_list_2[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

output_2 = reverse_list(sample_list)
print(output_2)