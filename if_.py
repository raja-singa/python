#!/usr/bin/python
angka1 = raw_input("Masukkan nilai pertama : ")
angka1 = int(angka1)

angka2 = raw_input("Masukkan nilai kedua : ")
angka2 = int(angka2)

if angka1 == angka2 :
	print "%d sama dengan %d"%(angka1,angka2)
if angka1 != angka2 :
	print "%d tidak sama dengan %d"%(angka1,angka2)
if angka1 < angka2 :
	print "%d kurang dari %d"%(angka1,angka2)
if angka1 > angka2 :
	print "%d lebih dari %d"%(angka1,angka2)
if angka1 <= angka2 :
	print "%d kurang / sama dengan %d"%(angka1,angka2)
if angka1 >= angka2 :
	print "%d lebih / sama dengan %d"%(angka1,angka2)

