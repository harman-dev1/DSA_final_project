#include<iostream>
using namespace std;

class Node{
    public:
    string email, password, first_name, last_name;
    int id;
    Node* l_child;
    Node* r_child;
    int height;
    Node() {
        l_child = NULL;
        r_child = NULL;
        height = 0;
    }
    Node(string email, string password, string first_name, string last_name, int id){
        this->email = email;
        this->password = password;
        this->first_name = first_name;
        this->last_name = last_name;
        this->id = id;

        this->height = 1;
        this->l_child = NULL;
        this->r_child = NULL;
    }

};

class AVL {
    public:
    Node* root;
    AVL() {
        root = NULL;
    }
    Node* r_insert_node(Node* , string, string ,string ,string, int);
    int height_of_node(Node*);
    int balanced_factor(Node*);
    Node* LLRotation(Node*);
    Node* RRRotation(Node*);
    Node* LRRotation(Node*);
    Node* RLRotation(Node*);
    void pre_order(Node*);
    void in_order(Node*);
    void post_order(Node*);
    int no_of_nodes(Node*);
};

Node* AVL::LLRotation(Node* p) {
    Node* pl = p->l_child;
    Node* plr = pl->r_child;

    pl->r_child = p;
    p->l_child = plr;

    p->height = height_of_node(p);
    pl->height = height_of_node(pl);


    if(p == root) {
        root = pl;
    }
    return pl;
}

Node* AVL::RRRotation(Node* p) {
    Node* pl = p->r_child;
    Node* plr = pl->l_child;

    pl->l_child = p;
    p->r_child = plr;

    p->height = height_of_node(p);
    pl->height = height_of_node(pl);

    if(p == root) {
        root = pl;
    }
    return pl;
}

Node* AVL::LRRotation(Node* p) {
    Node* pl = p->l_child;
    Node* plr = pl->r_child;

    p->l_child = plr->r_child;
    pl->r_child = plr->l_child;
    
    plr->r_child = p;
    plr->l_child = pl;

    p->height = height_of_node(p);
    pl->height = height_of_node(pl);
    plr->height = height_of_node(plr);

    if(root == p) {
        root = plr;
    }
    return plr;
}

Node* AVL::RLRotation(Node* p) {
    Node* pr = p->r_child;
    Node* prl = pr->l_child;

    p->r_child = prl->r_child;
    pr->l_child = prl->l_child;

    prl->r_child = pr;
    prl->l_child = p;

    p->height = height_of_node(p);
    pr->height = height_of_node(pr);
    prl->height = height_of_node(prl);

    if(root == p) {
        root = prl;
    }
    return prl;

}

int AVL:: height_of_node(Node* root) {
    int l_height;
    int r_height;
    l_height = root && root->l_child?root->l_child->height:0;
    r_height = root && root->r_child?root->r_child->height:0;
    return (max(l_height,r_height)+1);
}

int AVL::balanced_factor(Node* root) {
    int l_height;
    int r_height;
    l_height = root && root->l_child?root->l_child->height:0;
    r_height = root && root->r_child?root->r_child->height:0;
    return l_height-r_height;
}

Node* AVL:: r_insert_node(Node* root,string email, string password, string first_name, string last_name, int id) {
    if(root == NULL) {
        Node* new_node = new Node(email,password,first_name,last_name,id);
        root = new_node;
        return root;
    }
    if(id < root->id) {
        root->l_child = r_insert_node(root->l_child, email, password, first_name, last_name, id);
    }
    else if(id > root->id) {
        root->r_child = r_insert_node(root->r_child, email, password, first_name, last_name, id);
    }  
    root->height = height_of_node(root);
    if(balanced_factor(root) == 2 && balanced_factor(root->l_child) == 1) {
        return LLRotation(root);
    }
    if(balanced_factor(root) == -2 && balanced_factor(root->r_child) == -1) {
        return RRRotation(root);
    }
    if(balanced_factor(root) == 2 && balanced_factor(root->l_child) == -1)  {
        return LRRotation(root);
    }
    if(balanced_factor (root) == -2 && balanced_factor(root->r_child) == 1) {
        return RLRotation(root);
    }
    return root; 
}

Node* inorder_successor(Node* root) {
    Node* temp = root;
    while(temp && temp->l_child != NULL) {
        temp = temp->l_child;
    }
    return temp;
}

void AVL::pre_order(Node* root) {
    if(root == NULL) {
        return;
    }
    cout << root->email<< " " << root->password << " " << root->first_name << " " << root->last_name << " " << root->id << endl;
    pre_order(root->l_child);
    pre_order(root->r_child);
}


int AVL::no_of_nodes(Node* root) {
    if(root == NULL) {
        return 0;
    }
    int no_of_left_nodes = no_of_nodes(root->l_child);
    int no_of_right_nodes = no_of_nodes(root->r_child);
    return ((no_of_left_nodes + no_of_right_nodes) + 1);
}

main() {
    AVL a;
    int choice;
    int i = 0;
    string email, password, first_name, last_name;
    while(choice != 3) {
        cout << "1. Sign In" << endl;
        cout << "2. Sign Up" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter Choice :";
        cin >> choice;
        if(choice == 2) {
            cout << "Enter Your Email :";
            cin >> email;
            cout << "Enter Your Password :";
            cin >> password;
            cout << "Enter First Name :";
            cin >> first_name;
            cout << "Enter Last Name :";
            cin >> last_name;
            a.root =  a.r_insert_node(a.root,email,password,first_name,last_name,i);
            i +=1;
        }
    }
    cout << "Pre Order :";
    a.pre_order(a.root);
    cout << "\nNo Of Nodes: "<<a.no_of_nodes(a.root) << "\n";
    
}