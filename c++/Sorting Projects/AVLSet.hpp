// AVLSet.hpp
//
// ICS 46 Winter 2022
// Project #4: Set the Controls for the Heart of the Sun
//
// An AVLSet is an implementation of a Set that is an AVL tree, which uses
// the algorithms we discussed in lecture to maintain balance every time a
// new element is added to the set.  The balancing is actually optional,
// with a bool parameter able to be passed to the constructor to explicitly
// turn the balancing on or off (on is default).  If the balancing is off,
// the AVL tree acts like a binary search tree (e.g., it will become
// degenerate if elements are added in ascending order).
//
// You are not permitted to use the containers in the C++ Standard Library
// (such as std::set, std::map, or std::vector) to store the information
// in your data structure.  Instead, you'll need to implement your AVL tree
// using your own dynamically-allocated nodes, with pointers connecting them,
// and with your own balancing algorithms used.

#ifndef AVLSET_HPP
#define AVLSET_HPP

#include <functional>
#include "Set.hpp"



template <typename ElementType>
class AVLSet : public Set<ElementType>
{
public:
    // A VisitFunction is a function that takes a reference to a const
    // ElementType and returns no value.
    using VisitFunction = std::function<void(const ElementType&)>;

public:
    // Initializes an AVLSet to be empty, with or without balancing.
    explicit AVLSet(bool shouldBalance = true);

    // Cleans up the AVLSet so that it leaks no memory.
    ~AVLSet() noexcept override;

    // Initializes a new AVLSet to be a copy of an existing one.
    AVLSet(const AVLSet& s);

    // Initializes a new AVLSet whose contents are moved from an
    // expiring one.
    AVLSet(AVLSet&& s) noexcept;

    // Assigns an existing AVLSet into another.
    AVLSet& operator=(const AVLSet& s);

    // Assigns an expiring AVLSet into another.
    AVLSet& operator=(AVLSet&& s) noexcept;


    // isImplemented() should be modified to return true if you've
    // decided to implement an AVLSet, false otherwise.
    bool isImplemented() const noexcept override;


    // add() adds an element to the set.  If the element is already in the set,
    // this function has no effect.  This function always runs in O(log n) time
    // when there are n elements in the AVL tree.
    void add(const ElementType& element) override;


    // contains() returns true if the given element is already in the set,
    // false otherwise.  This function always runs in O(log n) time when
    // there are n elements in the AVL tree.
    bool contains(const ElementType& element) const override;


    // size() returns the number of elements in the set.
    unsigned int size() const noexcept override;


    // height() returns the height of the AVL tree.  Note that, by definition,
    // the height of an empty tree is -1.
    int height() const noexcept;


    // preorder() calls the given "visit" function for each of the elements
    // in the set, in the order determined by a preorder traversal of the AVL
    // tree.
    void preorder(VisitFunction visit) const;


    // inorder() calls the given "visit" function for each of the elements
    // in the set, in the order determined by an inorder traversal of the AVL
    // tree.
    void inorder(VisitFunction visit) const;


    // postorder() calls the given "visit" function for each of the elements
    // in the set, in the order determined by a postorder traversal of the AVL
    // tree.
    void postorder(VisitFunction visit) const;
    

private:
    // You'll no doubt want to add member variables and "helper" member
    // functions here.
    int sz;
    int depth;
    struct Node
    {
        Node* left;
        Node* right;
        ElementType element;
        
    };
    Node* root;
    void deleteNode(Node* n);
    void copynode(Node* n1, Node* n2);
    void insertion(const ElementType& element, Node*& n);
    void balanceTree(Node* n);
    void postorder_(VisitFunction visit, Node* n) const;
    void preorder_(VisitFunction visit, Node* n) const;
    void inorder_(VisitFunction visit, Node* n) const;
    int level(Node* n);
    bool balance = true;
};


template <typename ElementType>
AVLSet<ElementType>::AVLSet(bool shouldBalance)
{
    root = nullptr;
    balance = shouldBalance;
    sz = 0;
    depth = -1;
}


template <typename ElementType>
AVLSet<ElementType>::~AVLSet() noexcept
{
    deleteNode(root);
    sz = 0;
    depth = -1;
    root = nullptr;
}


template <typename ElementType>
AVLSet<ElementType>::AVLSet(const AVLSet& s)
{
    balance = s.balance;
    root = nullptr;
    sz = s.sz;
    depth = s.depth;
    copynode(root, s.root);
}


template <typename ElementType>
AVLSet<ElementType>::AVLSet(AVLSet&& s) noexcept
{
    root = nullptr;
    sz = 0;
    depth = -1;
    balance = true;
    std::swap(root, s.root);
    std::swap(sz, s.sz);
    std::swap(depth, s.depth);
    std::swap(balance, s.balance);
}


template <typename ElementType>
AVLSet<ElementType>& AVLSet<ElementType>::operator=(const AVLSet& s)
{
    deleteNode(root);
    root = nullptr;
    copynode(root,s.root);
    sz = s.sz;
    depth = s.depth;
    balance = s.balance;
    return *this;
}


template <typename ElementType>
AVLSet<ElementType>& AVLSet<ElementType>::operator=(AVLSet&& s) noexcept
{
    std::swap(root, s.root);
    std::swap(sz, s.sz);
    std::swap(depth, s.depth);
    std::swap(balance, s.balance);
    return *this;
}


template <typename ElementType>
bool AVLSet<ElementType>::isImplemented() const noexcept
{
    return true;
}
template <typename ElementType>
void AVLSet<ElementType>::insertion(const ElementType& element, Node*& n)
{
    
    if(n == nullptr)
    {
        Node* node = new Node;
        node-> element = element;
        node->left = nullptr;
        node->right = nullptr;
        n = node;
        depth = 0;
    }
    else if(element < n->element)
    {
        insertion(element, n->left);
        if(balance)
        {
            int weight = level(n->left) - level(n->right);
            if(weight >= 1)
            {
                if(element < n->element)
                {
                    Node* temp = n->left;
                    n->left = temp->right;
                    temp->right = n;
                    n = temp;
                }
                else
                {
                    Node* temp = n->left->right;
                    n->left->right = temp->left;
                    temp->left = n->left;
                    n->left = temp;
                    Node* temp1 = n->left;
                    n->left = temp1->right;
                    temp1->right = n;
                    n = temp1;
                }
            }
        }
        
    }
    else if(element > n->element)
    {
        insertion(element, n->right);
        if(balance)
        {
            int weight = level(n->left) - level(n->right);
            if(weight <= -1)
            {
                if(element > n->element)
                {
                    Node* temp = n->right;
                    n->right = temp->left;
                    temp->left = n;
                    n = temp;
                }
                else
                {
                    Node* temp1 = n->right->left;
                    n->right->left = temp1->right;
                    temp1->right = n->right;
                    n->right = temp1;
                    Node* temp = n->right;
                    n->right = temp->left;
                    temp->left = n;
                    n = temp;
                }
            }
        }
        
    }

    depth = std::max(level(n->left),level(n->right));
}

template <typename ElementType>
void AVLSet<ElementType>::add(const ElementType& element)
{
    insertion(element, this->root);
    sz++;

}

template <typename ElementType>
void AVLSet<ElementType>::balanceTree(Node* n)
{
    int weight = level(n->left) - level(n->right);
    std::cout<< level(n->left) << " " << level(n->right) <<std::endl;
    std::cout<< "balance this shit" << std::endl;
    if(weight >= 1)
    {
        
        if(n->left->element > n->element)
        {
            Node* temp = n->left;
            n->left = temp->right;
            temp->right = n;
            n = temp;
        }
        else
        {
            Node* temp = n->left->right;
            n->left->right = temp->left;
            temp->left = n->left;
            n->left = temp;
            Node* temp1 = n->left;
            n->left = temp1->right;
            temp1->right = n;
            n = temp1;
            
        }
    }
    else if(weight<= -1)
    {
        
        if(n->right->element < n->element)
        {
            Node* temp = n->right;
            n->right = temp->left;
            temp->left = n;
            n = temp;
        }
        else
        {
            std::cout<< "yo" << std::endl;
            Node* temp1 = n->right->left;
            n->right->left = temp1->right;
            temp1->right = n->right;
            n->right = temp1;
            Node* temp = n->right;
            n->right = temp->left;
            temp->left = n;
            n = temp;
        }
    }
            
}

template <typename ElementType>
bool AVLSet<ElementType>::contains(const ElementType& element) const
{
    Node* temp = root;
    while(temp != nullptr)
    {
        if(element < temp->element)
        {
            temp = temp->left;
        }
        else if (element > temp->element)
        {
            temp = temp->right;
        }
        else if (element == temp->element)
        {
            return true;
        }
    }
    return false;
}


template <typename ElementType>
unsigned int AVLSet<ElementType>::size() const noexcept
{
    return sz;
}


template <typename ElementType>
int AVLSet<ElementType>::height() const noexcept
{
    return depth;
}

template <typename ElementType>
void AVLSet<ElementType>::deleteNode(Node* n)
{
    if(n != nullptr)
    {
        deleteNode(n->left);
        deleteNode(n->right);
        delete n;
    }
}
template <typename ElementType>
int AVLSet<ElementType>::level(Node* n) 
{
   int height = 0;
   if (n != nullptr) 
   {
    int left_height = level(n->left);
    int right_height = level(n->right);
    int max_height = std::max(left_height, right_height);
    height = max_height + 1;
   }
   return height;
}


template <typename ElementType>
void AVLSet<ElementType>::copynode(Node* n1, Node* n2)
{
    
    if(n2 != nullptr)
    {
        n1 = new Node;
        n1->element = n2->element;
        n1->left = n2->left;
        n1->right = n2->right;
        if(n2->left != nullptr)
        {
            copynode(n1->left, n2->left);
        }
        if(n2->right != nullptr)
        {
            copynode(n1->right, n2->right);
        }
    }
}
template <typename ElementType>
void AVLSet<ElementType>::preorder_(VisitFunction visit, Node* n) const
{
    if(n != nullptr)
    {
        visit(n->element);
        preorder_(visit, n->left);
        preorder_(visit, n->right);
    }
}
template <typename ElementType>
void AVLSet<ElementType>::preorder(VisitFunction visit) const
{
    preorder_(visit, root);
}

template <typename ElementType>
void AVLSet<ElementType>::inorder_(VisitFunction visit, Node* n) const
{
    if(n != nullptr)
    {
        inorder_(visit, n->left);
        visit(n->element);
        inorder_(visit, n->right);
    }
}
template <typename ElementType>
void AVLSet<ElementType>::inorder(VisitFunction visit) const
{
    inorder_(visit, root);
}

template <typename ElementType>
void AVLSet<ElementType>::postorder_(VisitFunction visit, Node* n) const
{
    if(n != nullptr)
    {
        postorder_(visit, n->left);
        postorder_(visit, n->right);
        visit(n->element);
    }
}
template <typename ElementType>
void AVLSet<ElementType>::postorder(VisitFunction visit) const
{
    postorder_(visit, root);
}



#endif

