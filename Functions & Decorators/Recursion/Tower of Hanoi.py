def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    print("Move disk", n, "from", source, "to", destination)
    
    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, "A", "B", "C")

print("Total number of moves =", 2 ** n - 1)

'''
Enter number of disks: 4
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Move disk 3 from A to B
Move disk 1 from C to A
Move disk 2 from C to B
Move disk 1 from A to B
Move disk 4 from A to C
Move disk 1 from B to C
Move disk 2 from B to A
Move disk 1 from C to A
Move disk 3 from B to C
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Total number of moves = 15
'''
