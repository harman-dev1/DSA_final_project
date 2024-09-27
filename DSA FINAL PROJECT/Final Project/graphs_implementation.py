class Vertex:
    def __init__(self, first_name="", last_name="", email="", password=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.next = None

class Graph:
    def __init__(self):
        self.HG = [None] * 10

    def is_email_exists(self, email):
        for i in range(10):
            temp = self.HG[i]
            while temp:
                if temp.email == email:
                    return True
                temp = temp.next
        return False
    
    def check_already_friend(self,email_of_login,email_of_friend):
        self.load_from_file("Friends_connection.txt")
        for i in range(10):
            if self.HG[i] is not None:
                p = self.HG[i]
                q = p.next
                while q:
                    if (p.email == email_of_login and q.email == email_of_friend) or (p.email == email_of_friend and q.email == email_of_login):
                        return True
                    q = q.next
        return False
                        
        
    
    def add_edge(self, f_name1, l_name1, email1, password1, f_name2, l_name2, email2, password2):
        n_node1 = Vertex(f_name1, l_name1, email1, password1)
        n_node2 = Vertex(f_name2, l_name2, email2, password2)
        found = "NO"
        for i in range(10):
            if self.HG[i] is not None:
                if self.HG[i].email == email1:
                    p = self.HG[i]
                    while p.next:
                        p = p.next
                    p.next = n_node2
                    found = "Yes"
                    break
        self.save_to_file("Friends_connection.txt")           
                    
               
        if found == "NO":
            for i in range(10):
                if self.HG[i] is None:
                    self.HG[i] = n_node1
                    p = self.HG[i]
                    while p.next:
                        p = p.next
                    p.next = n_node2
                    break
                '''elif self.HG[i].email == email1:
                    p = self.HG[i]
                    while p.next:
                        p = p.next
                    p.next = n_node2
                    break'''
            self.save_to_file("Friends_connection.txt")
            
    def all_friends_of_login_user(self,email):
        self.load_from_file("Friends_connection.txt")
        list_of_friends = []
        for i in range(10):
            if self.HG[i] is not None:
                p = self.HG[i]
                q = p.next
                while q:
                    if (p.email == email):
                        list_of_friends.append(q.email)
                    q = q.next
                if(list_of_friends != []):
                    return list_of_friends
        return list_of_friends      

    def print_graph(self):
        for i in range(10):
            temp = self.HG[i]
            self.print_node(temp)

    def print_node(self, head):
        temp = head
        if not head:
            return
        while temp:
            print(f"{temp.first_name} {temp.last_name} {temp.email} {temp.password} ", end="")
            temp = temp.next
        print("Next Node\n")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for i in range(10):
                temp = self.HG[i]
                while temp:
                    file.write(f"{temp.password},{temp.email},{temp.first_name},{temp.last_name}\n")
                    temp = temp.next
                file.write("END\n")  # Add a marker to denote the end of nodes at each index

    def load_from_file(self, filename):
        self.HG = [None] * 10
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                index = -1
                for line in lines:
                    if line.strip() == "END":
                        index += 1
                        continue
                    data = line.strip().split(',')
                    password = int(data[0])
                    email = data[1]
                    first_name = data[2]
                    last_name = data[3]
                    vertex = Vertex(first_name, last_name, email, password)
                    
                    if self.HG[index] is None:
                        self.HG[index] = vertex
                    else:
                        temp = self.HG[index]
                        while temp.next:
                            temp = temp.next
                        temp.next = vertex
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print("Error during loading:", e)
def main():
    g1 = Graph()
    g1.add_edge("Harmain", "Iftikhar", "h@gmail.com", 1234, "Saboor", "Abdul", "s@gmail.com", 1234)
    g1.add_edge("Harmain", "Iftikhar", "h@gmail.com", 1234, "Ahamd", "Iftikhar", "a@gmail.com", 1234)
    g1.add_edge("Ahamd", "Abdul", "a@gmail.com", 1234, "Harmain", "Iftikhar", "h@gmail.com", 1234)
    g1.add_edge("Ahamd", "Abdul", "a@gmail.com", 1234, "Saboor", "Abdul", "s@gmail.com", 1234)

    g1.print_graph()
    g1.save_to_file("graph_data.txt")
    print("After loading from file printing data")

if __name__ == "__main__":
    main()