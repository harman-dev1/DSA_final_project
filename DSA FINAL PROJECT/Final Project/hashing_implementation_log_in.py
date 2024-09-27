class Node:
    def __init__(self, first_name="", last_name="", email="", password=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.next = None

class HashTable:  
    def __init__(self):
        self.HT = [None] * 10

    def hash(self, key):
        return key % 10

    def insert(self, first_name, last_name, email, password):
        hash_table_index = self.hash(password)
        new_node = Node(first_name, last_name, email, password)
        if self.HT[hash_table_index] is None:
            self.HT[hash_table_index] = new_node
        else:
            p = self.HT[hash_table_index]
            q = self.HT[hash_table_index]
            while p is not None and p.password < password:
                q = p
                p = p.next
            if password <= q.password:
                new_node.next = q
                self.HT[hash_table_index] = new_node
            else:
                new_node.next = q.next
                q.next = new_node
        self.save_to_file("SignUp.txt")
                

    def unique_email(self, email):
        for index in range(len(self.HT)):
            temp = self.HT[index]
            while temp:
                if temp.email.lower() == email.lower():
                    return False
                temp = temp.next

        return True
    
    def check_user(self,head,email):
        temp = head
        while temp:
            if temp.email == email:
                return temp
            temp = temp.next
        return None
        
    def user_for_searching(self,email_of_search_user):
        from mainpage_ui import email
        if email_of_search_user == email:
            return "Same"
        self.load_from_file("SignUp.txt")
        for i in range(10):
            temp = self.HT[i]
            if temp:
                found_node = self.check_user(temp,email_of_search_user)
                if found_node:
                    return found_node
        self.print_hash_table()
        return "Not Found"

    def search(self, password, email):
        self.load_from_file("SignUp.txt")
        hash_table_index = self.hash(password)
        p = self.HT[hash_table_index]
        while p and password >= p.password:
            if p.password == password and p.email == email:
                return p
            p = p.next
        return None

    def delete_from_hash_table(self, password, email):
        hash_table_index = self.hash(password)
        temp = self.HT[hash_table_index]
        if temp.password == password and temp.email == email:
            d_node = temp
            self.HT[hash_table_index] = temp.next
            del d_node
        else:
            while temp.next and temp.next.password != password and temp.next.email == email:
                temp = temp.next
            d_node = temp.next
            temp.next = temp.next.next
            del d_node
    
    
    def print_node(self, head):
        temp = head
        if head is None:
            print("-1")
            return
        while temp is not None:
            print(f"{temp.password} {temp.email} {temp.first_name} {temp.last_name}")
            temp = temp.next
        print()

    def print_hash_table(self):
        for i in range(10):
            print(f"index: {i}")
            temp = self.HT[i]
            self.print_node(temp)
    
    def people_you_may_know(self, email):
        people_connection = []
        for i in range(10):
            temp = self.HT[i]
            while temp is not None:
                if temp.email != email and temp.email not in people_connection:
                    people_connection.append(temp.email)
                temp = temp.next  # Move to the next node
        return people_connection
    
    def update_user(self, check_original_email, new_email, new_first_name, new_last_name, password):
        self.load_from_file("SignUp.txt")
        print(check_original_email, new_email, new_first_name, new_last_name)
        for i in range(10):
            temp = self.HT[i]
            while temp is not None:
                if temp is not None and temp.email == check_original_email:
                    if new_first_name is not None:
                        temp.first_name = new_first_name
                    if new_last_name is not None:
                        temp.last_name = new_last_name
                    if new_email is not None:
                        temp.email = new_email
                    temp.password = password
                    self.save_to_file("SignUp.txt")  
                    return True  
                temp = temp.next
        return False
    
    def save_to_file(self, filename):
       with open(filename, 'w') as file:  
           for node in self.HT:
               temp = node
               while temp:
                   file.write(f"{temp.password},{temp.email},{temp.first_name},{temp.last_name}\n")
                   temp = temp.next

    def load_from_file(self, filename):
        self.HT = [None] * 10
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    password = int(data[0])
                    email = data[1]
                    first_name = data[2]
                    last_name = data[3]

                    self.insert(first_name, last_name, email, password)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print("Error during loading:", e)