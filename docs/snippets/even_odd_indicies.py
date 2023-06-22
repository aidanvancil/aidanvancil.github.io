l = [2,7,4,9,6,1,6,3]
odd_indice = [j%2!=0 for j in l[1::2]]
even_indice = [j%2==0 for j in l[::2]]
total_indice = odd_indice + even_indice
print(all(total_indice))