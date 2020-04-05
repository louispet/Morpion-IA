# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:51:51 2020

@author: louis
"""
'''Le plateau de jeu est un vecteur. Plus simple à gérer'''

def NewGame():
	return ['.','.','.','.','.','.','.','.','.']

'''On gère l'affichage à Partir du vecteur '''
def AfficherGame(s):

	print('\n'+str(s[0])+'|'+str(s[1])+'|'+str(s[2]))
	print("-|-|-")
	print(str(s[3])+'|'+str(s[4])+'|'+str(s[5]))
	print("-|-|-")
	print(str(s[6])+'|'+str(s[7])+'|'+str(s[8]))

'''On voit si la place ou mettre le O est déjà prise'''
def TestPlay(s,nb):
    retour = True
    if (s [nb]!= '.'):
        retour = False
    return retour
        

def Actions(s):
	tab=[]
	for i in range(len(s)):
		if s[i]=='.':
			tab.append(i)
	return tab

''' On place le X ou le O sur la grille de jeu'''
def Resultat(s,a,maxi):
	if maxi:
		s[a]='X'
	else:
		s[a]='O'
	return s

''' On voit si c'est nul si il n'y a plus de point et que personne n'a gagné'''
def est_nulle(s):
	valeur=True
	for i in s:
		if i== '.':
			valeur=False
	return valeur

''' On retourne si la partie est finie 1 si l'IA gagne sinon -1'''
def partieFinie(s):
	resultat=None
	if Terminal_Test(s)==1:
		resultat=1
	elif Terminal_Test(s)==-1:
		resultat=-1
	elif est_nulle(s):
		resultat=0
	return resultat

'''On vérifie si une ligne/colonne/diag est complété avec la même valeur puis on voit si c'est l'IA ou le joueur'''
def Terminal_Test(s):
	res='.'
	if (s [0]!= '.' and  s [0]== s [3]== s [6]):
		res=s[0]
	if (s [0]!= '.' and  s [0]== s [1]== s [2]):
		res=s[0]
	if (s [0]!= '.'and  s [0]== s [4]== s [8]):
		res=s[0]
	if (s [1]!='.'and  s [1]== s [4]== s [7]):
		res=s[1]
	if (s [2]!= '.' and  s [2]== s [5]== s [8]):
		res=s[2]
	if (s [2]!= '.' and  s [2]== s [4]== s [6]):
		res=s[2]
	if (s [3]!= '.' and  s [3]== s [4]== s [5]):
		res=s[3]
	if (s [6]!= '.' and  s [6]== s [7]== s [8]):
		res=s[6]
	if(res=='X'):
		return 1
	elif(res=='O'):
		return -1
	else:
		return 0

def retour(s, action):
    s[action] = '.'
    return s



def MeilleurCoup(s,maxi):
	actions = Actions(s)
	best=-2	
	rang=0
	for i in range(len(actions)):
		val=minmax(Resultat(s,actions[i],maxi),not maxi)
		retour(s,actions[i])
		if(val>best):
			best=val
			rang=i
	return actions[rang]

	
	

def minmax(s,maxi):
	finPartie=partieFinie(s)
	if(finPartie!= None):
		return finPartie
	actions = Actions(s)
	if maxi:
		best = float('-inf')
		for action in actions:
			val = minmax(Resultat(s,action,maxi), not maxi)
			retour(s, action)
			best = max(best, val)
	else:
		best = float('inf')
		for action in actions:
			val = minmax(Resultat(s,action,maxi), not maxi)
			retour(s, action)
			best = min(best, val)
	return best

def Play_minimax():
    g=NewGame()
    while (partieFinie(g)==None):
        n=False
        while (n==False):
            entreeligne=eval(input("Sur quelle ligne placer le 'O' : "))
            entreecolone=eval(input("Sur quelle colone : "))
            entree=3*(entreeligne-1)+entreecolone-1
            n=TestPlay(g,entree)
            g=Resultat(g,entree,False)
            AfficherGame(g)
        if(partieFinie(g)==None):
            a=MeilleurCoup(g,True)
            g=Resultat(g,a,'X')
            AfficherGame(g)
    Fin=partieFinie(g)
    if(Fin==1):
        print("Ia X a gagné")
    elif(Fin==-1):
        print("Ia X a gagné")
    elif(Fin==0):
        print("Match nul")

def max_alpha_beta(s, alpha, beta):
    maxv = -2
    px = None
    

    result = Terminal_Test(s)

    if result == -1:
            return (-1, 0)
    elif result == 1:
            return (1, 0)
    elif result == 2:
            return (0, 0)

    
    for i in range(0, 9):
            if s[i] == '.':
                
                s[i] = 'O'
                (m, min_i) = min_alpha_beta(s,alpha, beta)
                
                if m > maxv:
                    maxv = m
                    px = i
                    
                s[i] = '.'

               
                if maxv >= beta:
                    return (maxv, px)

                if maxv > alpha:
                    alpha = maxv

    return (maxv, px)
    
def min_alpha_beta(s, alpha, beta):
    minv = 2
    qx = None
    
    result = Terminal_Test(s)

    if result == -1:
            return (-1, 0)
    elif result == 1:
            return (1, 0)
    elif result == 2:
            return (0, 0)

    for i in range(0, 9):
        if s[i] == '.':
            s[i] = 'X'
            (m, max_i) = max_alpha_beta(s,alpha, beta)
            if m < minv:
                minv = m
                qx = i
                    
            s[i] = '.'

            if minv <= alpha:
                return (minv, qx)

            if minv < beta:
                beta = minv

    return (minv, qx)

def play_alpha_beta():
    g=NewGame()
    while True:
        cpt=1
        AfficherGame(g)
        result = Terminal_Test(g)
        if (partieFinie(g) != None):
            Fin=partieFinie(g)
            if(Fin==1):
                print("X a gagné")
            elif(Fin==-1):
                print("O a gagné")
            elif(Fin==0):
                print("Match nul")
            
            return
        if (cpt%2!=0):
            cpt=cpt+1
            (m,qx) = min_alpha_beta(g,-2, 2)
            print('Aide au joueur, mouvement recommandé pour X = {}'.format(qx))

            px = int(input('Quelle place insérer le X : '))
            qx = px
            if TestPlay(g,px):
                g[px] = 'X'  
            else:
                print('Mouvement impossible')
        if (cpt%2==0):
            cpt=cpt+1
            (m,px) = max_alpha_beta(g,-2, 2)
            
            g[px] = 'O'
            
           
# Main Program
if __name__ == "__main__":
    #
    a=int(input("Pour algo minimax tapez 1\nPour elagage alpha beta 2\nVotre choix : "))
    assert(a!=1 or a!=2),'Le nombre saisit est différent de 1 ou 2 :( '
    if(a==1):
        Play_minimax()
    if(a==2):
        print('Pour jouer il faudra placer le pion en indiquant sa place comprise entre 0 et 8')
        play_alpha_beta()


        
        










