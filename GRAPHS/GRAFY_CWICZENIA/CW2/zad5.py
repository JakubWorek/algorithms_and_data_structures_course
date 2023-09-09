# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto
# jest otoczone murem i ma tylko dwie bramy - północną i południową. Z każdej bramy prowadzi dokładnie
# jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być
# połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
# zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
# miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze
# stolicy Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić
# algorytm, który stwierdza czy odpowiednia trasa gońca istnieje.

# wierzchołkami grafu będą oazy
# szukamy cyklu eulera

def trasaGonca(G, oazy):


oasis = [2, 4, 5, 7, 9]
graph = [[2, 4], [2, 9], [0, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]
print(trasaGonca(graph, oasis))