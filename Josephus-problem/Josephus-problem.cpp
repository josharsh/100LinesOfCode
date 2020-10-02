#include<iostream.h>
using namespace std;
struct node
{
    int data;
    struct node *next;
};
class linked
{
    public:
    node *beg, *end;
    linked()
    {
        beg=end=NULL;
    }
    void add(int n)
    {
        node *temp= new node;
        temp->data=n;
        temp->next=NULL;
        if(beg==NULL && end==NULL)
        beg=end=temp;
        else
        {
            end->next=temp;
            end=temp;
            temp->next=beg;
        }
    }
    void del(node *beforedel)
    {
        node *temp;
        temp=beforedel->next;
        beforedel->next=temp->next;
        delete temp;
    }
    
    
};
int main() 
{
    linked l;
    int n, i=1;
    cin>>n;
    for(; i<=n; i++)
    l.add(i);
    node *start;
    start=l.beg;
    while(start->next!=start)
    {
        node *t ;
        t= start;
        cout<<start->data<<" kills "<<start->next->data<<"\n";
        l.del(t);
        if(start->next!=start)
        cout<<start->data<<" passes knife to "<<start->next->data<<"\n";
        start=start->next;
    }
    cout<<start->data<<" Survives";
    return 0;
}