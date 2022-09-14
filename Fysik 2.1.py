import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./20)
  
g = 9.82 #gravitationens aceleration

slowprint("2.1 Beräkna krafterna som bockarna utövar på brädan i figuren (se bild)")
print()

m = float(input("Vad är plankans vikt? "))
l = float(input("Vad är avståndet till mittpunkten från en av bockarna? "))
print()

print("Givet: \nMassa planka =", m, "kg \nKraft =", m*g, "N \nAvstånd =", l, "m")
print()
slowprint("Sökt: Krafterna som bockarna utövar på brädan")
print()
print("Lösning: \nF=m*g =", m, "*", g, "=", m*g, "N")
F=m*g
print("M=F*l =", F, "*", l, "=", F*l, "Nm")
M=F*l
print("Kraft mot plankan från bocken = M/totalt avstånd (3.5m) =", M, "/ 3,5 ≈", round(M/3.5, 1), "N")
print()
slowprint("För att beräkna kraften från den andra bocken, starta om programmet och mata in avståndet till mittpunkten")