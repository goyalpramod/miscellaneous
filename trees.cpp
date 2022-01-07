#include <bits/stdc++.h>
using namespace std;

struct node{
    int data;
    node *left;
    node *right;
};

node *newNode(int data){
    node *newNode = new node();
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

node *insert(node *root,int data){
    if(root == NULL){
        root = newNode(data);
    }else if(data <= root->data){
        root->left = insert(root->left,data);
    }else{
        root->right = insert(root->right,data);
    }
    return root;
}

void levelOrder(node *root){
    if(root == NULL)return;
    queue<node*> q;
    q.push(root);
    while(!q.empty()){
        node *current = q.front();
        cout<<current->data<<" ";
        if(current->left != NULL) q.push(current->left);
        if(current->right != NULL) q.push(current->right);
        q.pop();
    }
}

void preOrder(node *root){
    if(root == NULL) return;
    cout<<root->data<<" ";
    preOrder(root->left);
    preOrder(root->right);
}

void inOrder(node *root){
    if(root == NULL) return;
    preOrder(root->left);
    cout<<root->data<<" ";
    preOrder(root->right);
}

void postOrder(node *root){
    if(root == NULL) return;
    preOrder(root->left);
    preOrder(root->right);
    cout<<root->data<<" ";
}

bool isLesser(node *root,int value){
    if(root == NULL) return true;
    if(root->data <= value &&
       isLesser(root->left,value)&&
       isLesser(root->right,value))
       return true;
    else
        return false;
}

bool isGreater(node *root,int value){
    if(root == NULL) return true;
    if(root->data >= value &&
       isGreater(root->left,value)&&
       isGreater(root->right,value))
       return true;
    else
        return false;
}

bool isBST(node *root){
    if(root == NULL)return true;
    if(isLesser(root->left,root->data)&&
       isGreater(root->right,root->data)&&
       isBST(root->left)&&
       isBST(root->right))
       return true;
    else
        return false;
}

bool search(node *root,int data){
    if(root == NULL) return false;
    if(root->data == data) return true;
    else if( data < root->data){
        return search(root->left,data);
    }else{
        return search(root->right,data);
    }
}

int min(node *root){
    if(root == NULL){
        return -1;
    }
    if(root->left == NULL){
        return root->data;
    }else{
        return min(root->left);
    }
}

int height(node *root){
    if(root == NULL){
        return -1;
    }else{
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        return max(leftHeight,rightHeight) + 1;
    }
}

node *delete_node(node *root,int data){
    if(root == NULL)return root;
    else if(data<root->data) root->left = delete_node(root->left,data);
    else if(data>root->data) root->right = delete_node(root->right,data);
    else{
        if(root->left == NULL && root->right == NULL){
            delete root;
            root = NULL;
         
        }else if(root->left == NULL){
            node *temp = root;
            root = root->right;
            delete temp;
        }else if(root->right == NULL){
            node *temp = root;
            root = root->left;
            delete temp;
        }else{
            node *temp = root;
            temp = temp->right;
            while(temp->left!=NULL){
                temp = temp->left;
            }
            root->data = temp->data;
            root->right = delete_node(root->right,temp->data);
        }
    }
    return root;
}

node *getSuccessor(node *root,int data){
    
}

int main(){
    node *root = NULL;
    root = insert(root,15);
    root = insert(root,10);
    root = insert(root,20);
    root = insert(root,12);
    root = insert(root,30);
    root = insert(root,8);
    root = insert(root,6);

    bool ans = search(root,22);
    if(ans){
        cout<<"Found"<<'\n';
    }else{
        cout<<"Not Found"<<'\n';
    }

    int min_element = min(root);
    cout<<min_element<<'\n';

    int height_tree = height(root);
    cout<<"The height of the tree is "<<height_tree<<'\n';

    return 0;
}