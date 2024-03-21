#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <exception>

using namespace std;
template <typename T>

class LinkedList
{

public:

    struct Node
    {
        T data;
        Node* next;
        Node* prev;

    };

    /*==BEHAVIORS==*/
    void PrintForward() const;
    void PrintReverse() const;
    void PrintForwardRecursive(const Node* node) const;
    void PrintReverseRecursive(const Node* node) const;

    /*==ACCESSORS==*/
    unsigned int NodeCount() const;
    void FindAll(vector<Node*>& outData, const T& value ) const;
    const Node* Find(const T& data) const;
    Node* Find(const T& data);
    const Node* GetNode(unsigned int index) const;
    Node* GetNode(unsigned int index);
    Node* Head();
    const Node* Head() const;
    Node* Tail();
    const Node* Tail() const;

    /*==INSERTION==*/
    void AddHead(const T& data);
    void AddTail(const T& data);
    void AddNodesHead(const T* data, unsigned int count);
    void AddNodesTail(const T* data, unsigned int count);
    void InsertAfter(Node* node, const T& data);
    void InsertBefore(Node* node, const T& data);
    void InsertAt(const T& data, unsigned int index);

    /*==REMOVAL==*/
    bool RemoveHead();
    bool RemoveTail();
    unsigned int Remove(const T& data);
    bool RemoveAt(int index);
    void Clear();

    /*==Operators==*/
    const T& operator[](unsigned int index) const;
    T& operator[](unsigned int index);
    bool operator==(const LinkedList<T>& rhs) const;
    LinkedList<T>& operator=(const LinkedList<T>& rhs);

    /*==Construction / Destruction==*/
    LinkedList();
    LinkedList(const LinkedList<T>& rhs);
    ~LinkedList();

private:

    Node* ptrToHead;
    Node* ptrToTail;
    unsigned int countNodes;
};

/*==Construction / Destruction==*/

template <typename T>
LinkedList<T>::LinkedList()
{
    countNodes = 0;
    ptrToHead = nullptr;
    ptrToTail = nullptr;
}

template <typename T>
LinkedList<T>::LinkedList(const LinkedList& list)
{
    Node* newHead = new Node();

    ptrToHead = newHead;
    ptrToTail = newHead;
    ptrToHead -> data = list.ptrToHead -> data;

    Node* rhsNode = list.ptrToHead;
    Node* newNode = this -> ptrToHead;
    countNodes = list.countNodes;

    for (unsigned int i = 0; i < list.countNodes - 2; i++)
    {
        newNode -> next = new Node();
        newNode -> next -> prev = newNode;
        rhsNode = rhsNode -> next;
        newNode = newNode -> next;
        newNode -> data = rhsNode -> data;
    }

    newNode -> next = new Node();
    newNode -> next -> prev = newNode;
    rhsNode = rhsNode -> next;
    newNode = newNode -> next;
    newNode -> data = rhsNode -> data;
    ptrToTail = newNode;
}


template <typename T>
LinkedList<T>::~LinkedList()
{
    Clear();
}

/*==ACCESSORS==*/

template <typename T>
typename LinkedList<T>::Node* LinkedList<T>::Head()
{
    return ptrToHead;
}

template <typename T>
const typename LinkedList<T>::Node* LinkedList<T>::Head() const
{
    return ptrToHead;
}

template <typename T>
typename LinkedList<T>::Node* LinkedList<T>::Tail()
{
    return ptrToTail;
}

template <typename T>
const typename LinkedList<T>::Node* LinkedList<T>::Tail() const
{
    return ptrToTail;
}

template <typename T>
unsigned int LinkedList<T>::NodeCount() const
{
    return countNodes;
}

template <typename T>
void LinkedList<T>::FindAll(vector<Node*>& outData, const T& value ) const
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        if (tempNode -> data == value)
        {
            outData.push_back(tempNode);
        }
        tempNode = tempNode -> next;
    }
}

template <typename T>
const typename LinkedList<T>::Node* LinkedList<T>::GetNode(unsigned int index) const
{
    if (index >= countNodes)
    {
        throw std::out_of_range("An error has occurred.");
    }
    else if (index == 0)
    {
        return ptrToHead;
    }
    else if (index == countNodes - 1)
    {
        return ptrToTail;
    }
    else
    {
        Node* tempNode = ptrToHead;

        for (unsigned int i = 0; i < index; i++)
        {
            tempNode = tempNode -> next;
        }
        return tempNode;
    }
}

template <typename T>
typename LinkedList<T>::Node* LinkedList<T>::GetNode(unsigned int index)
{
    if (index > countNodes)
    {
        throw std::out_of_range("An error has occurred.");
    }
    else if (index == 0)
    {
        return ptrToHead;
    }
    else if (index == countNodes - 1)
    {
        return ptrToTail;
    }
    else
    {
        Node* tempNode = ptrToHead;

        for (unsigned int i = 0; i < index; i++)
        {
            tempNode = tempNode -> next;
        }
        return tempNode;
    }
}

template <typename T>
const typename LinkedList<T>::Node* LinkedList<T>::Find(const T& data) const
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        while (tempNode -> data == data)
        {
            return GetNode(i);
        }
        tempNode = tempNode -> next;
    }
    return nullptr;
}

template <typename T>
typename LinkedList<T>::Node* LinkedList<T>::Find(const T& data)
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        while (tempNode -> data == data)
        {
            return GetNode(i);
        }
        tempNode = tempNode -> next;
    }
    return nullptr;
}

/*==BEHAVIORS==*/

template <typename T>
void LinkedList<T>::PrintForward() const
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        if (tempNode != nullptr)
        {
            cout << tempNode -> data << endl;
        }
        tempNode = tempNode -> next;
    }
}

template <typename T>
void LinkedList<T>::PrintReverse() const
{
    Node* tempNode = ptrToTail;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        if (tempNode != nullptr)
        {
            cout << tempNode -> data << endl;
        }
        tempNode = tempNode -> prev;
    }
}

template <typename T>
void LinkedList<T>::PrintForwardRecursive(const Node* node) const
{
    if (node != nullptr)
    {
        cout << node -> data << endl;
        PrintForwardRecursive(node -> next);
    }
}

template <typename T>
void LinkedList<T>::PrintReverseRecursive(const Node* node) const
{
    if (node != nullptr)
    {
        cout << node->data << endl;
        PrintReverseRecursive(node->prev);
    }
}

/*==INSERTION==*/

template <typename T>
void LinkedList<T>::AddHead(const T& data)
{
    Node* newHead = new Node;
    newHead -> data = data;
    newHead -> next = nullptr;
    newHead -> prev = nullptr;

    if(ptrToHead == nullptr)
    {
        ptrToHead = newHead;
        ptrToTail = newHead;
    }
    else
    {
        newHead -> next = ptrToHead;
        ptrToHead -> prev = newHead;
        ptrToHead = newHead;
    }
    countNodes++;
}

template <typename T>
void LinkedList<T>::AddTail(const T& data)
{
    Node *newTail = new Node;
    newTail -> data = data;
    newTail -> next = nullptr;
    newTail -> prev = nullptr;

    if (ptrToTail == nullptr)
    {
        ptrToHead = newTail;
    }
    else
    {
        ptrToTail -> next = newTail;
        newTail -> prev = ptrToTail;
    }
    ptrToTail = newTail;
    countNodes++;
}

template <typename T>
void LinkedList<T>::AddNodesHead(const T* data, unsigned int count)
{
    for (unsigned int i = count - 1; i > 0; i--)
    {
        AddHead(data[i]);

        if (i == 1)
        {
            AddHead(data[i - 1]);
        }
    }
}

template <typename T>
void LinkedList<T>::AddNodesTail(const T* data, unsigned int count)
{
    for (unsigned int i = 0 ; i < count; i++)
    {
        AddTail(data[i]);
    }
}

template <typename T>
void LinkedList<T>::InsertAt(const T& data, unsigned int index)
{
    if (index > countNodes)
    {
        throw std::out_of_range("An error has occurred.");
    }
    else if (index == 0)
    {
        AddHead(data);
    }
    else if (index == countNodes)
    {
        AddTail(data);
    }
    else
    {
        Node* newInsertNode = new Node();
        Node* tempPrev;
        Node* tempNext;
        Node* tempNode = ptrToHead;
        newInsertNode -> data = data;

        for (unsigned int i = 1; i < index; i++)
        {
            tempNode = tempNode -> next;
        }

        tempPrev = tempNode;
        tempNext = tempNode -> next;
        tempPrev -> next = newInsertNode;
        tempNext -> prev = newInsertNode;
        newInsertNode -> next = tempNext;
        newInsertNode -> prev = tempPrev;

        countNodes++;
    }
}

template <typename T>
void LinkedList<T>::InsertAfter(Node* node, const T& data)
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        if (node == GetNode(i))
        {
            InsertAt(data, i + 1);
            break;
        }
        tempNode = tempNode -> next;
    }
}

template <typename T>
void LinkedList<T>::InsertBefore(Node* node, const T& data)
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < countNodes; i++)
    {
        if (node == GetNode(i))
        {
            InsertAt(data, i);
            break;
        }
        tempNode = tempNode -> next;
    }
}

/*==REMOVAL==*/

template <typename T>
bool LinkedList<T>::RemoveHead()
{
    if (countNodes == 0)//
    {
        return false;
    }
    else if (countNodes == 1)
    {
        delete ptrToHead;
        ptrToHead = nullptr;
        ptrToTail = nullptr;
        countNodes--;
        return true;
    }
    else
    {
        ptrToHead = ptrToHead -> next;
        delete ptrToHead -> prev;
        ptrToHead -> prev = nullptr;
        countNodes--;
        return true;
    }
}

template <typename T>
bool LinkedList<T>::RemoveTail()
{
    if (countNodes == 0)
    {
        return false;
    }
    else if (countNodes == 1)
    {
        delete ptrToTail;
        ptrToHead = nullptr;
        ptrToTail = nullptr;
        countNodes--;
        return true;
    }
    else
    {
        ptrToTail = ptrToTail -> prev;
        delete ptrToTail -> next;
        ptrToTail -> next = nullptr;
        countNodes--;
        return true;
    }
}

template <typename T>
unsigned int LinkedList<T>::Remove(const T& data)
{
    int count = 0;

    Node* tempNode = ptrToHead;

    for(unsigned int i = 0; i < countNodes; i++)
    {
        if (tempNode -> data == data)
        {
            tempNode = tempNode -> next;
            RemoveAt(i);
            count++;
            i--;
        }
        else
        {
            tempNode = tempNode -> next;
        }
    }
    return count;
}

template <typename T>
bool LinkedList<T>::RemoveAt(int index)
{
    if ((unsigned)index > countNodes - 1 || (unsigned) index < 0 || countNodes == 0)
    {
        return false;
    }
    else if (index == 0)
    {
        RemoveHead();
        countNodes--;
        return true;
    }
    else if ((unsigned) index == countNodes)
    {
        RemoveTail();
        countNodes--;
        return true;
    }
    else if (countNodes == 1)
    {
        Node* tempNode = GetNode(0);
        tempNode -> next = nullptr;
        tempNode -> prev = nullptr;
        delete tempNode;
        countNodes--;
        return true;
    }
    else
    {
        Node* tempNode = GetNode(index);
        Node* nextNode = tempNode -> next;
        Node* prevNode = tempNode -> prev;
        prevNode -> next = nextNode;
        nextNode -> prev = prevNode;
        tempNode -> next = nullptr;
        tempNode -> prev = nullptr;
        delete tempNode;
        countNodes--;
        return true;
    }
}

template <typename T>
void LinkedList<T>::Clear()
{
    Node* tempNode = ptrToHead;

    for (unsigned int i = 1; i < countNodes; i++)
    {
        tempNode = tempNode -> next;
        delete tempNode -> prev;
    }
    delete tempNode;
    ptrToHead = nullptr;
    ptrToTail = nullptr;
    countNodes = 0;
}

/*==Operators==*/

template <typename T>
const T& LinkedList<T>::operator[](unsigned int index) const
{
    if (index > countNodes || index < 0)
    {
        throw std::out_of_range("An error has occurred.");
    }

    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < index; i++)
    {
        tempNode = tempNode -> next;
    }
    return tempNode -> data;
}

template <typename T>
T& LinkedList<T>::operator[](unsigned int index)
{
    if (index > countNodes || index < 0)
    {
        throw std::out_of_range("An error has occurred.");
    }

    Node* tempNode = ptrToHead;

    for (unsigned int i = 0; i < index; i++)
    {
        tempNode = tempNode -> next;
    }
    return tempNode -> data;
}

template <typename T>
bool LinkedList<T>::operator==(const LinkedList<T>& rhs) const
{
    bool result;
    Node* newNode = ptrToHead;
    Node* rhsNode = rhs.ptrToHead;

    if (countNodes != rhs.countNodes)
    {
        return false;
    }
    else
    {
        for (unsigned int i = 0; i < countNodes; i++)
        {
            if (newNode -> data != rhsNode -> data)
            {
                return false;
            }
            else
            {
                newNode = newNode -> next;
                rhsNode = rhsNode -> next;
                result = true;
            }
        }
    } return result;
}

template <typename T>
LinkedList<T>& LinkedList<T>::operator=(const LinkedList<T>& rhs)
{
    Clear();

    Node* newHead = new Node();

    ptrToHead = newHead;
    ptrToTail = newHead;
    ptrToHead -> data = rhs.ptrToHead -> data;

    Node* rhsNode = rhs.ptrToHead;
    Node* newNode = this -> ptrToHead;
    countNodes = rhs.countNodes;

    for (unsigned int i = 0; i < rhs.countNodes - 2; i++)
    {
        newNode -> next = new Node();
        newNode -> next -> prev = newNode;
        rhsNode = rhsNode -> next;
        newNode = newNode -> next;
        newNode -> data = rhsNode -> data;
    }

    newNode -> next = new Node();
    newNode -> next -> prev = newNode;
    rhsNode = rhsNode -> next;
    newNode = newNode -> next;
    newNode -> data = rhsNode -> data;
    ptrToTail = newNode;

    return *this;
}

