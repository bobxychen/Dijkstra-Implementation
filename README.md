# Dijkstra-Implementation
A seemingly working/correct implementation of Dijkstra's Algorithm on the coordinate plane

### About
An implementation of Dijkstra's algorithm to find the shortest path between 2 nodes in a graph, here implemented as points in a cartesain plane. This was developed by me, however I cannot confirm the extent of it's correctness (it's worked so far but there are probably cases not covered).

### Usage
To use it, modify the file "main(2).py" directly under the title where it says "Starting Parameters".

**Input** is a dictionary that takes in a labeled point (eg "A", "B", "C") and also it's coordinates e.g ("A":[1,1],"B":[5,1],"C":[5,5]). This will form the basis of the program as this defines which "nodes" the program can explore

**Starting Point** is the point at which the program will start, given as a single point e.g "A"
**Destination Point** is the point at which the program will try to navigate to from the Starting Point e.g "C"

**Direct** is a list of "lines" or connections (edges of map) that you do not want the program to use, such as going directly from the start ot destination, or other not useful variations. It is important as with the current version of the application, it will generate all possible links between nodes (feature may be added to manually add connections)

Then run: 
'''bash
python main(2).py
'''

### Note

This has not been throughly tested, but has worked in my (non-extensive) testing.
