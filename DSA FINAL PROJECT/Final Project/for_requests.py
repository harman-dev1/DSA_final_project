import pickle
email_list = []

class Node:
    def __init__(self, first_name="", last_name="", email="", password=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.next = None

class LinkedList:
    def __init__(self):
        self.LL = [None] * 10  # Array to hold linked lists at each index
        
    def already_sent_connection(self,email_of_login,email_of_friend):
        self.load_from_file("Pending_Requests.txt")
        self.save_to_file("Pending_Requests.txt")
        for i in range(10):
            if self.LL[i] is not None:
                first_node = self.LL[i]
                second_node = first_node.next
                print(first_node.email, " --------" , second_node.email)
                if (first_node.email == email_of_login and second_node.email == email_of_friend) or (first_node.email == email_of_friend and second_node.email == email_of_login):
                    return True
        return False
    def made_friend_None_connection(self,email_of_login,email_of_friend):
        self.load_from_file("Pending_Requests.txt")
        self.save_to_file("Pending_Requests.txt")
        for i in range(10):
            if self.LL[i] is not None:
                first_node = self.LL[i]
                second_node = first_node.next
                print(first_node.email, " --------" , second_node.email)
                if (first_node.email == email_of_login and second_node.email == email_of_friend) or (first_node.email == email_of_friend and second_node.email == email_of_login):
                    second_node = None
                    self.LL[i] = None
                    break
        self.save_to_file("Pending_Requests.txt")        
    
    def email_to_be_displayed(self, login_email):
        email_list = []
        for i in range(10):
            if self.LL[i] is not None:
                first_node = self.LL[i]
                second_node = first_node.next
                
                if first_node.email != login_email and second_node is not None and second_node.email == login_email:
                    email_list.append(first_node.email)
        return email_list
    
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            for linked_list in self.LL:
                pickle.dump(linked_list, file)


    def load_from_file(self, filename):
        self.LL = [None] * 10  # Reset LL
        try:
            with open(filename, 'rb') as file:
                for i in range(10):
                    self.LL[i] = pickle.load(file)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error during loading:", e)

           
    def insert_node_at_end(self, f_name1, l_name1, email1, password1, f_name2, l_name2, email2, password2):
        n_node1 = Node(f_name1, l_name1, email1, password1)
        n_node2 = Node(f_name2, l_name2, email2, password2)
        
        for i in range(10):
            if self.LL[i] is None:
                self.LL[i] = n_node1
                p = self.LL[i]
                while p.next is not None:
                    p = p.next
                p.next = n_node2
                break
    def print_node(self):
        for i in range(10):
            print(i)
            temp = self.LL[i]
            self.print_list(temp)

    @staticmethod
    def print_list(head):
        temp = head
        while temp is not None:
            print(temp.first_name, temp.last_name, temp.email, temp.password, end=" ")
            temp = temp.next
        print()
