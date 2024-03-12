#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <queue>
using namespace std;
struct Node{
    char symbol;
    unsigned freq;
    Node *left;
    Node *right;

    Node(char symbol, unsigned freq) : symbol(symbol), freq(freq), left(nullptr), right(nullptr) {}
};

struct comp{
    bool operator()(Node *l, Node *r){
        return l->freq > r->freq;
    }
};

void printCodes(Node *root, string str, unordered_map<char, string> &huffmanCodes){
    if (!root){
        return;
    }
    printCodes(root->left, str + "0", huffmanCodes);
    printCodes(root->right, str + "1", huffmanCodes);
    if (!root->left && !root->right){
        huffmanCodes[root->symbol] = str;
    }
}
unordered_map<char, string> generateHuffmanCodes(istream &input) {
    unordered_map<char, unsigned> freq;
    string line;
    while (getline(input, line)) {
        for (char c : line) {
            if (isalpha(c) || isspace(c)) {
                freq[toupper(c)]++;
            }
        }
    }

    priority_queue<Node *, vector<Node *>, comp> pq;
    for (const auto &pair : freq) {
        pq.push(new Node(pair.first, pair.second));
    }
    while (pq.size() > 1) {
        Node *left = pq.top();
        pq.pop();
        Node *right = pq.top();
        pq.pop();

        Node *mergedNode = new Node('$', left->freq + right->freq);
        mergedNode->left = left;
        mergedNode->right = right;

        pq.push(mergedNode);
    }
    Node *root = pq.top();
    unordered_map<char, string> huffmanCodes;
    queue<pair<Node *, string>> q;
    q.push({root, ""});
    while (!q.empty()) {
        Node *current = q.front().first;
        string currentCode = q.front().second;
        q.pop();
        if (current->left) {
            q.push({current->left, currentCode + "0"});
        }
        if (current->right) {
            q.push({current->right, currentCode + "1"});
        }
        if (!current->left && !current->right) {
            huffmanCodes[current->symbol] = currentCode;
        }
    }
    delete root;
    return huffmanCodes;
}
int main(){
    string file;
    cout<<"Enter file name: ";//Your input text file goes here
    getline(cin, file);
    ifstream input (file);
    string ofile;
    cout<<"Enter your output file name, where your codes will be saved: ";//Your output text file goes here
    getline(cin, ofile);
    ofstream outputFile(ofile);
    unordered_map<char, string> huffmanCodes = generateHuffmanCodes(input);
    for (const auto &pair : huffmanCodes) {
        cout << pair.first << " " << pair.second << "\n";
        outputFile << pair.first << " " << pair.second << "\n";
    }
    return 0;
}
