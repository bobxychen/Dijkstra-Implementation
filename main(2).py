# Dijkstra Algorithm Implmentation
# Does it really work? It seems like it but


#################################################
#Starting Parameters
#################################################
Input = {"A":[1,1],"B":[5,1],"C":[5,5],"D":[0,0], "F":[99,4]}

starting_point = "D"
destination_point = "C"
direct = ['AC','DC','FB','DF','DB'] #list of links to destroy
#################################################


weights = {}

for i,items in enumerate(Input.items()):
    k,v = items
    for k1,v1 in Input.items()[i+1:]:
        eachx, eachy = v
        each1x, each1y = v1
        #print eachx,eachy,each1x,each1y
        
        weights["".join(sorted(k + k1))] = ((eachx-each1x) ** 2 + (eachy-each1y) ** 2) ** 0.5  #2 point distance formula

print weights
print ""

for each in direct: #fist must destroy direct links etc
    try:
        del weights[each]
    except KeyError:
        del weights[each[::-1]]
        
#now to implement a thing to find the route from D -> C

backtrack = weights.keys() #cloning it for later

print weights
print float("inf")

points = {x:float("inf") for x in Input}
points[starting_point] = 0
print points


been_to = []
not_been_to = Input.keys()

while not_been_to: #when there are still points left
    next_point = min(not_been_to, key = points.get)  #this gets the lowest value that hasnt been visited yet
    #print min(points, key = points.get)
    print "min_poiint " +min(not_been_to, key = points.get)
    #if next_point == destination_point:
        #break

    for each in weights.keys(): #using .keys() to avoid chaning dictioary size
        if next_point in each:
            #therefore other one is
            destination = each.replace(next_point,"")
            potential_cost = weights[each] + points[next_point]
            
            if potential_cost < points[destination]:
                points[destination] = potential_cost
            del weights[each]
            
            #print weights
            #print points
            
    been_to.append(next_point)
    not_been_to.remove(next_point)
    #print not_been_to
    #print next_point
    
print "FINAL Cost to each node:"
print points
print ""

print "FINAL Points been to:"
print been_to
print ""

stops = []
each = destination_point
stops.append(destination_point)

while each != starting_point:
    has_each = [x.replace(each,"") for x in backtrack if each in x]
    #print "has each " + str(has_each)
    prev_stop = min(has_each, key = points.get)
    
    stops.append(prev_stop)
    each = prev_stop

print "FINAL Path:"
print stops[::-1]
            
        

        
        
        
        
        
        
        
        
        
        

        