
import csv
#import Stack
import LinkedList as listin
from collections import deque

def encryption(text, shift):
        encrypted_text = ""
        for char in text:
            shifted = ord(char) + (shift % 26)
            if char.isalpha():
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                    encrypted_text += chr(shifted)
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                    encrypted_text += chr(shifted)
            elif char.isdigit():
                if shifted > ord('9'):
                    shifted -= 10
                elif shifted < ord('0'):
                    shifted += 10
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

def decryption(text, shift):
    decrypted_text = ""
    for char in text:
        shifted = ord(char) - (shift % 26)
        if char.isalpha():
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        elif char.isnumeric():
            if shifted > ord('9'):
                shifted -= 10
            elif shifted < ord('0'):
                shifted += 10
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def read_from_csv(username, contact):
    with open('user_data.txt', mode='r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) >= 3:
                encrypted_username = data[0]
              
                decrypted_contact = decryption(data[1], 3)
                print(decrypted_contact)
                if username == encrypted_username and contact == decrypted_contact:
                    decrypted_email = decryption(data[2], 3)
                    return True, decrypted_email
    return False, None

    

def save_graph_to_csv(graph):
    with open("user_data.txt", mode="r", newline="") as file:
        existing_users = set(row[0] for row in csv.reader(file))

    with open("user_data.txt", mode="a", newline="") as file:
        writer = csv.writer(file)
        for vertex in graph.getVertices():
            if vertex.name not in existing_users:
                contact = encryption(vertex.contact, 3)
                email = encryption(vertex.email, 3)
                writer.writerow([vertex.name, contact, email])
                existing_users.add(vertex.name)



def load_graph_from_csv():
    graph = Graph()

    try:
        with open("user_data.txt", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    name, contact, email = row[0], decryption(row[1], 3), decryption(row[2], 3)
                    current_vertex = Vertex(name, contact, email, True)
                    graph.addVertex(current_vertex)
                else:
                    print(f"Skipping row: {row}. Insufficient data.")

    except FileNotFoundError:
        print("File not found. Initializing an empty graph.")

    return graph



class Vertex:
    def __init__(self, name, contact, email,created):
        self.inNeighbors = []
        self.outNeighbors = []
        self.name = name
        self.contact = contact
        self.email = email
        self.created = created
        self.callLog = Stack.myStack()
        self.linkedlist = listin.LinkList()
        self.inTime = None
        self.outTime = None
        self.status = "unvisited"
        self.favourite = []
        self.messages = []

    def hasOutNeighbor(self, name):
        return any(neighbor.name == name for neighbor in self.outNeighbors)

    def hasInNeighbor(self, name):
        return any(neighbor.name == name for neighbor in self.inNeighbors)

    def hasNeighbor(self, name):
        return self.hasInNeighbor(name) or self.hasOutNeighbor(name)

    def getOutNeighbors(self):
        return self.outNeighbors
    
    def removeOutNeighbor(self, neighbor):
        if neighbor in self.outNeighbors:
            self.outNeighbors.remove(neighbor)

    def getInNeighbors(self):
        return self.inNeighbors

    def addOutNeighbor(self, neighbor):
        self.outNeighbors.append(neighbor)

    def addInNeighbor(self, neighbor):
        self.inNeighbors.append(neighbor)

    def __str__(self):
        return f"({self.name}, {self.contact}, {self.email})"
    
    def call(self,neighbour,username,contact):
        for v in neighbour:
            if v.name == username and v.contact == contact:
                return v            
        return None
        

            

    

    
class Graph:
    def __init__(self):
        self.vertices = []

    def userExist(self, name, contact):
        check = False
        for vertex in self.vertices:
            if vertex.name == name and vertex.created == True:
                check =  True
                break

        if check:
             check = False
             for vertex in self.vertices:
                if vertex.contact == contact and vertex.created == True:
                    check =  True
                    break
        return check

    def addingContactUserExist(self, name, contact, check):
        for vertex in self.vertices:
            if vertex.name == name and vertex.contact == contact and vertex.created == check:
                return vertex  
        return False
    def addingContactNeighbourExist(self, name, contact, check,neighbour):
        for vertex in neighbour:
            if vertex.name == name and vertex.contact == contact and vertex.created == check:
                return vertex  
        return False
    
    def chkneighbours(self,name,contact,neighbours):
        for n in neighbours:
            if n.name == name and n.contact == contact:
                return n
            
        return None

    def newAccount(self,username,contact,email,created):
        if not self.userExist(username,contact):
            ourvertex = Vertex(username,contact,email,created)
            return ourvertex
        else:
            return None

      

    def addVertex(self,vertex):
        self.vertices.append(vertex)

    def getVertices(self):
        return self.vertices

    def addDiEdge(self,u,v):
        u.addOutNeighbor(v)
        v.addInNeighbor(u)

    def addBiEdge(self,u,v):
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)

    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            ret += [ [v, u] for u in v.outNeighbors ]
        return ret
    

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()

            if current_vertex not in visited:
                self.process_vertex(current_vertex)

                visited.add(current_vertex)
                for neighbor in current_vertex.getInNeighbors():
                    if neighbor not in visited:
                        queue.append(neighbor)

    def process_vertex(self, vertex):
        self.currentVertexInNeighbors.append(vertex)
    
    
    
    def __str__(self):
        ret = "CS261Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n\n\n"
        ret += "\t Edges:\n\t\t"
        for a,b in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + ") "
        ret += "\n"
        return ret
    
    def BFS_search(neighbour, searchName):
             
        for v in neighbour:
            if v.name == searchName:
                return v  
        return None
    

class calls:
    def __init__(self,vertex,datetime):
        self.vertex = vertex
        self.time = datetime

class message:
    def __init__(self,sender,reciever,message,time):
        self.sender = sender
        self.reciever = reciever
        self.message = message
        self.time = time
        

