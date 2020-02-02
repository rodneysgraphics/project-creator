from sys import argv
import sys


from random import choice
#from living_things import *
#import mods

i=0

foo = ['a', 'b', 'c', 'd', 'e']
goo = ['f', 'g', 'h', 'h', 'i']
hoo = ['j', 'k', 'l', 'm', 'n']

make_project = ['HTML','Python','Javascript','PHP','3D','SQLite']
inco = ['HTML','CSS','Python','PHP','SQLite','website']
obje = ['numbers','strings','dates','arrays','bollean','loop','While_Loop','if_Statements']

while i < 9:
	i = i + 1
	print ""
	print "Make a project using",
	print choice(make_project) , 
	print "incoperating",
	print choice(inco) ,
	print "intergrating with",
	print choice(make_project) ,
	print "using",
	print choice(obje),
	print ""

