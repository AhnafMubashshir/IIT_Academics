#include<bits/stdc++.h>
using namespace std;

class Graph
{
int V; 
list<int> *adj; 
bool isCyclicUtil(int v, bool visited[], bool *rs); 
public:
Graph(int V); 
void addEdge(int v, int w); 
bool isCyclic(); 
};

Graph::Graph(int V)
{
this->V = V;
adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
adj[v].push_back(w); 
}


bool Graph::isCyclicUtil(int v, bool visited[], bool *recStack)
{
if(visited[v] == false)
{
visited[v] = true;
recStack[v] = true;

list<int>::iterator i;
for(i = adj[v].begin(); i != adj[v].end(); ++i)
{
if ( !visited[*i] && isCyclicUtil(*i, visited, recStack) )
return true;
else if (recStack[*i])
return true;
}

}
recStack[v] = false; 
return false;
}

bool Graph::isCyclic()
{
bool *visited = new bool[V];
bool *recStack = new bool[V];
for(int i = 0; i < V; i++)
{
visited[i] = false;
recStack[i] = false;
}


for(int i = 0; i < V; i++)
if ( !visited[i] && isCyclicUtil(i, visited, recStack))
return true;

return false;
}

int main()
{
    Graph g(4);

    string str[10], T[4][4];
    int n, i, j, u, v;
    char ch;
    int adjMat[10][10]={};
    freopen("input.txt", "r", stdin);
    cin>>n;
    
    for(i=0; i<n; i++){
        cin>>str[i];
    }

    for(i=0; i<n; i++){
        for(j=i+1; j<n; j++){
            if(str[i][0]=='r' && str[j][0]=='r') continue;
            else if(str[i][1]==str[j][1]) continue;
            else{
                // cout<<str[i][2]<<" "<<str[j][2]<<endl;
                if(str[i][3]==str[j][3]){
                    ch= str[i][1];
                    u= (int) ch - 48;
                    ch= str[j][1];
                    v= (int) ch - 48;

                    g.addEdge(u, v);
                    //cout<<str[i][1]<<"-"<<str[j][1]<<" "<<str[i][0]<<" "<<str[j][0]<<endl;
                    break;
                }
            }
        }
    }

    // g.addEdge(2, 3);
    // g.addEdge(3, 1);
    // g.addEdge(2, 1);

    if(g.isCyclic()) cout << "Graph contains cycle";
    else cout << "Graph doesn't contain cycle";
}