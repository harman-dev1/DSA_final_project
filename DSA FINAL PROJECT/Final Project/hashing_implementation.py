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

    def add_edge(self, f_name1, l_name1, email1, password1, f_name2, l_name2, email2, password2):
        n_node1 = Vertex(f_name1, l_name1, email1, password1)
        n_node2 = Vertex(f_name2, l_name2, email2, password2)

        for i in range(10):
            if self.HG[i] is None:
                self.HG[i] = n_node1
                p = self.HG[i]
                while p.next:
                    p = p.next
                p.next = n_node2
                break
            elif self.HG[i].email == email1:
                p = self.HG[i]
                while p.next:
                    p = p.next
                p.next = n_node2
                break

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
        print()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for node in self.HG:
                temp = node
                while temp:
                    file.write(f"{temp.password},{temp.email},{temp.first_name},{temp.last_name}\n")
                    temp = temp.next

    def load_from_file(self, filename):
        self.HG = [None] * 10

        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                password = int(data[0])
                email = data[1]
                first_name = data[2]
                last_name = data[3]

                self.add_edge(first_name, last_name, email, password, "", "", "", 0)

def main():
    g1 = Graph()
    g1.add_edge("Harmain", "Iftikhar", "h@gmail.com", 1234, "Saboor", "Abdul", "s@gmail.com", 1234)
    g1.add_edge("Harmain", "Iftikhar", "h@gmail.com", 1234, "Ahamd", "Iftikhar", "a@gmail.com", 1234)
    g1.add_edge("Ahamd", "Abdul", "a@gmail.com", 1234, "Harmain", "Iftikhar", "h@gmail.com", 1234)
    g1.add_edge("Ahamd", "Abdul", "a@gmail.com", 1234, "Saboor", "Abdul", "s@gmail.com", 1234)

    g1.print_graph()
    g1.save_to_file("graph_data.txt")
    print("After loading from file printing data")

    # Clear the existing graph data
    #g1.load_from_file("graph_data.txt")
    g1.print_graph()

if __name__ == "__main__":
    main()