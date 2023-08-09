// HashSet.hpp
//
// ICS 46 Winter 2022
// Project #4: Set the Controls for the Heart of the Sun
//
// A HashSet is an implementation of a Set that is a separately-chained
// hash table, implemented as a dynamically-allocated array of linked
// lists.  At any given time, the HashSet has a "size" indicating
// how many elements are stored within it, along with a "capacity"
// indicating the size of the array.
//
// As elements are added to the HashSet and the proportion of the HashSet's
// size to its capacity exceeds 0.8 (i.e., there are more than 80% as many
// elements as there are array cells), the HashSet should be resized so
// that it is twice as large as it was before.
//
// You are not permitted to use the containers in the C++ Standard Library
// (such as std::set, std::map, or std::vector) to store the information
// in your data structure.  Instead, you'll need to use a dynamically-
// allocated array and your own linked list implemenation; the linked list
// doesn't have to be its own class, though you can do that, if you'd like.

#ifndef HASHSET_HPP
#define HASHSET_HPP

#include <functional>
#include "Set.hpp"



template <typename ElementType>
class HashSet : public Set<ElementType>
{
public:
    // The default capacity of the HashSet before anything has been
    // added to it.
    static constexpr unsigned int DEFAULT_CAPACITY = 10;

    // A HashFunction is a function that takes a reference to a const
    // ElementType and returns an unsigned int.
    using HashFunction = std::function<unsigned int(const ElementType&)>;

public:
    // Initializes a HashSet to be empty, so that it will use the given
    // hash function whenever it needs to hash an element.
    explicit HashSet(HashFunction hashFunction);

    // Cleans up the HashSet so that it leaks no memory.
    ~HashSet() noexcept override;

    // Initializes a new HashSet to be a copy of an existing one.
    HashSet(const HashSet& s);

    // Initializes a new HashSet whose contents are moved from an
    // expiring one.
    HashSet(HashSet&& s) noexcept;

    // Assigns an existing HashSet into another.
    HashSet& operator=(const HashSet& s);

    // Assigns an expiring HashSet into another.
    HashSet& operator=(HashSet&& s) noexcept;


    // isImplemented() should be modified to return true if you've
    // decided to implement a HashSet, false otherwise.
    bool isImplemented() const noexcept override;
    void rehash();

    // add() adds an element to the set.  If the element is already in the set,
    // this function has no effect.  This function triggers a resizing of the
    // array when the ratio of size to capacity would exceed 0.8, in which case
    // the new capacity should be determined by this formula:
    //
    //     capacity * 2 + 1
    //
    // In the case where the array is resized, this function runs in linear
    // time (with respect to the number of elements, assuming a good hash
    // function); otherwise, it runs in constant time (again, assuming a good
    // hash function).  The amortized running time is also constant.
    void add(const ElementType& element) override;


    // contains() returns true if the given element is already in the set,
    // false otherwise.  This function runs in constant time (with respect
    // to the number of elements, assuming a good hash function).
    bool contains(const ElementType& element) const override;


    // size() returns the number of elements in the set.
    unsigned int size() const noexcept override;


    // elementsAtIndex() returns the number of elements that hashed to a
    // particular index in the array.  If the index is out of the boundaries
    // of the array, this function returns 0.
    unsigned int elementsAtIndex(unsigned int index) const;


    // isElementAtIndex() returns true if the given element hashed to a
    // particular index in the array, false otherwise.  If the index is
    // out of the boundaries of the array, this functions returns false.
    bool isElementAtIndex(const ElementType& element, unsigned int index) const;


private:
    HashFunction hashFunction;
    int sz;
    int cap;
    struct Node
    {
        ElementType element;
        Node* next;
    };
    Node** hash;
    // You'll no doubt want to add member variables and "helper" member
    // functions here.
};



namespace impl_
{
    template <typename ElementType>
    unsigned int HashSet__undefinedHashFunction(const ElementType& element)
    {
        return 0;
    }
}


template <typename ElementType>
HashSet<ElementType>::HashSet(HashFunction hashFunction)
    : hashFunction{hashFunction}
{
    
    cap = DEFAULT_CAPACITY;
    sz = 0;
    hash = new Node*[cap];
    for(int i = 0; i<cap; i++)
    {
        hash[i] = nullptr;
    }

}


template <typename ElementType>
HashSet<ElementType>::~HashSet() noexcept
{
    for(int i =0; i< cap;i++)
    {
        Node* node = hash[i];
        while(node != nullptr)
        {
            Node* temp = node;
            node = node -> next;
            delete temp;
        }
    }
    delete[] hash;
}


template <typename ElementType>
HashSet<ElementType>::HashSet(const HashSet& s)
    : hashFunction{impl_::HashSet__undefinedHashFunction<ElementType>}
{
    
    cap = s.cap;
    sz = s.sz;
    hash = new Node*[cap];
    for(int i = 0; i< cap; i++)
    {
        hash[i] = nullptr;
        Node* node = s.hash[i];
        while(node != nullptr)
        {
            Node* copy = new Node;
            copy->element = node->element;
            copy->next = hash[i];
            hash[i] = copy;
            node = node->next;
        }

    }
}


template <typename ElementType>
HashSet<ElementType>::HashSet(HashSet&& s) noexcept
    : hashFunction{impl_::HashSet__undefinedHashFunction<ElementType>}
{
    cap = DEFAULT_CAPACITY;
    sz = 0;
    hash = new Node*[cap];
    for(int i = 0; i< cap; i++)
    {
        hash[i] = nullptr;
    }
    std::swap(cap, s.cap);
    std::swap(sz, s.sz);
    std::swap(hash, s.hash);
}


template <typename ElementType>
HashSet<ElementType>& HashSet<ElementType>::operator=(const HashSet& s)
{
    
    if (this != &s)
    {
        
        cap = s.cap;
        sz = s.sz;
        Node** copy_hash = new Node*[cap];
        
        for(int i = 0; i < cap; i++)
        {
            copy_hash[i] = nullptr;
            Node* node = s.hash[i];
            while(node != nullptr)
            {
                Node* copy = new Node;
                copy->element = node->element;
                copy->next = hash[i];
                hash[i] = copy;
                node = node->next;
            }
        }
        for(int i =0; i< cap;i++)
        {
            Node* node = hash[i];
            while(node != nullptr)
            {
                Node* temp = node;
                node = node -> next;
                delete temp;
            }
        }
        delete[] hash;
        hash  = copy_hash;
    }
    return *this;
}


template <typename ElementType>
HashSet<ElementType>& HashSet<ElementType>::operator=(HashSet&& s) noexcept
{
    std::swap(sz, s.sz);
    std::swap(cap, s.cap);
    std::swap(hash, s.hash);

    return *this;
}


template <typename ElementType>
bool HashSet<ElementType>::isImplemented() const noexcept
{
    return true;
}


template <typename ElementType>
void HashSet<ElementType>::add(const ElementType& element)
{
    if(contains(element) == false)
    {
        unsigned int index = hashFunction(element) % cap;
        Node* node = new Node;
        node->element = element;
        node->next = hash[index];
        hash[index] = node;
        sz++;

        if(sz > cap*0.8)
        {
            rehash();
        }
    }
    
}
template <typename ElementType>
void HashSet<ElementType>::rehash()
{
	int newcap = ((cap * 2) + 1); 
	Node **newhash = new Node* [newcap]; 
	for(int i = 0; i < newcap; i++)
	{
		newhash[i] = nullptr;
	}
	for(unsigned int i = 0; i < cap; i++) 
	{
		Node *node = hash[i];
		while(node != nullptr)
		{
            int newkey = hashFunction(node->element) % newcap;
            Node* current = new Node;
            Node* temp = node;
            current -> element = node -> element;
            current -> next = newhash[newkey];
            newhash[newkey] = current;
            node = node->next;
			delete temp; //Delete the current node
		}
	}
	delete[] hash; 
    hash = newhash;
}

template <typename ElementType>
bool HashSet<ElementType>::contains(const ElementType& element) const
{
    unsigned int key = hashFunction(element) % cap;
    Node* node = hash[key];
    while(node != nullptr)
    {
        if(node->element == element)
        {
            return true;
        }
        else
        {
            node = node->next;
        }
    }
    return false;
}


template <typename ElementType>
unsigned int HashSet<ElementType>::size() const noexcept
{
    return sz;
}


template <typename ElementType>
unsigned int HashSet<ElementType>::elementsAtIndex(unsigned int index) const
{
    if(index >= cap)
    {
        return 0;
    }
    Node* node = hash[index];
    int element_num = 0;
    while(node != nullptr)
    {
        node = node->next;
        element_num++;
    }
    return element_num;
}


template <typename ElementType>
bool HashSet<ElementType>::isElementAtIndex(const ElementType& element, unsigned int index) const
{
    if(index >= cap)
    {
        return false;
    }
    Node* node = hash[index];
    while(node != nullptr)
    {
        if(node->element == element)
        {
            return true;
        }
        else
        {
            node = node->next;
        }

    }
    return false;
    
}



#endif

