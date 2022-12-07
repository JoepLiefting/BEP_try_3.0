import heapq
import pandas as pd
class priorityQueue:
    def __init__(self):
        self.cities = []
    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    def pop(self):
        return heapq.heappop(self.cities)[1]
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False
    def check(self):
        print(self.cities)

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

emissions = {}

def makedict():
    file = open("emissions_all_vehicles.txt", 'r')
    for string in file:
        line = string.split('-')
        ct1 = line[0]
        ct2 = line[1]
        dist = float(line[2])
        emissions.setdefault(ct1, []).append(ctNode(ct2, dist))
        emissions.setdefault(ct2, []).append(ctNode(ct1, dist))

# bomen doorbouwen

def makehuristikdict():
    h = {}
    with open("total_emissions.txt", 'r') as file:
        for line in file:
            line = line.strip().split("-")
            node = line[0].strip()
            sld = float(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)
        if (current == end):
            break
        for new in emissions[current]:
            g_cost = distance[current] + float(new.distance)
            #print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                #print(f_cost)
                q.push(new.city, f_cost)
                path[new.city] = current
    printoutput(start, end, path, distance, expandedList)

def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("A-star Algorithm for emissions in route")
    print("\tDelta => Nuremberg")
    print("=======================================================")
    print("List of Cities that are Expanded : " + str(expandedlist))
    print("Total Number of Cities that are Expanded : " + str(len(expandedlist)))
    print("=======================================================")
    print("Cities in Final path : " + str(finalpath))
    print("Total Number of cities in final path are : " + str(len(finalpath)))
    print("Total Cost : " + str(distance[end]))
    print(str(finalpath[0]))

def main():
    src = "Euromax"
    dst = "Nuremberg"
    makedict()
    astar(src, dst)

if __name__ == "__main__" :
    main()

#(Op elke locatie kies je de mogelijkheden naar elke volgende locatie, miss cost lager aan barge geven met factor 10 bijv.
# Euromax1,Euromax, 0 voor elk punt 1 en 2 combi
#straks heb je een route maar als voor een punt niet in tijdsslot past pak je een truck
#miss heeft geen zin om costs meer te doen want dan rekent hij terug en pakt andere beste optie
#Dus je krijgt je final path, en moet in timewindow kunnen dus bij elkaar optellen)

# insert van request p en d voor src en dst
# for str(finalpath):
#     kies de eerste en tweede p en d locatie van str(finalpath) en zet deze gelijk aan de p en d in vehicle file,
#     dan zien als t matcht met ap en bp en pop vehicle als voldoet en ga naar volgende p en d in finalpath,
#     als geen een vehicle voldoet kies train voor zelfde locaties, anders kies truck
#     dan hetzelfde met de 2e en 3e locatie maar skip als bijv. delta = delta1 dan 4e en 5e tot einde van str finalpath.