# Jakub Worek 06.03.2023-11.03.2023
#
# Dowód poprawności:
# Jak się okazuje nie bez powodu ulubiony palindrom 
# cesarzowej Bajtocji jest nieparzystej długości.
# Idąc po kolei po każdej literze napisu traktujemy ją jako środek
# prawdopodobnego palindromu, ponieważ palindrom ten jest na pewno
# nieparzystej długości.
# Następnie puszczamy z tego środka dwa "wskaźniki na litery", które
# poruszają się, jeden w lewo po napisie, drugi w prawo po napisie
# i sprawdzamy czy tworzy się palindrom i zwiększamy sukcesywnie
# długość ostatecznego rezultatu.
#
# Przykład:
# a k o n t n o k n o n a b c d d c b a
# > > > > ^
#         _
#       < _ >
#     < < _ > >
#   < < < _ > > >
# koniec, bo a != k, ten palindrom ma długość 7
#
# Złożoność obliczeniowa:
# Badamy po kolei każdą literę i rozchodzące się z niej podciągi
# O(n^2)

from zad1testy import runtests


def ceasar( s ):
    n=len(s)
    # Minimalny wynik to 1, ponieważ ciąg złożony z jednej litery
    # jest palindromem
    wynik=1

    i=0
    while(i < n):
        lewy = i-1 # lewy "wskaźnik" po napisie
        prawy = i+1 # prawy "wskaźnik" po napisie
        # długość utworzonego w ten sposób słowa to:
        # prawy-lewy+1


        while( (lewy>=0) and (prawy < n) and (s[lewy] == s[prawy])):
            #wynik=max(prawy-lewy+1,wynik) WOLNIEJSZE OD IFA
            if(prawy-lewy+1 > wynik):
                wynik=prawy-lewy+1
            lewy-=1
            prawy+=1
        
        i+=1


    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )