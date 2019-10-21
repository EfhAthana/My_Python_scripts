#Να γραφεί πρόγραμμα σε γλώσσα C το οποίο θα διαβάζει τις βαθμολογίες για ένα συγκεκριμένο μάθημα 5 φοιτητών σε ένα μονοδιάστατο πίνακα Α. 
#Θα υπολογίζει και θα εμφανίζει το πλήθος των φοιτητών οι οποίοι έχουν βαθμό λιγότερο από 5 και τους φοιτητές που αρίστευσαν και έχουν βαθμό μεγαλύτερο ή ίσο από 8,5.


A = []

for i in range(5):
	x = float(input("dwse bathmologia: "))
	A.append(x)


counterless = 0
counterexcellent = 0 
for i in A:
	if (Α[i] < 5):
		counterless = counterless + 1
	elif (A[i] >= 8.5):
		counterexcellent = counterexcellent +1


print("to plithos twn foititwn pou kopikan einai: ",counterless,"\nto plithos twv foititwn poy aristeusan einai: ",counterexcellent)


	