#include<iostream>
#include<map>
typedef long long ll;
using namespace std;
map<ll, ll> M, indegree;
int main() {
    int testCases = 0;
    while (1) {
        bool ans = true;
        ll a, b;
        ll edgeCnt = 0;
        ll nodeCnt = 0;
        M.clear();
        indegree.clear();
        while (scanf("%lld%lld", &a, &b), (a || b)) {
            if (a == -1 && b == -1) return 0;
            edgeCnt++;
            if (M.find(a) == M.end()) 
                M.insert({ a, nodeCnt++ });
        
            if (M.find(b) == M.end()) 
                M.insert({ b, nodeCnt++ });
        
            if (indegree.find(b) == indegree.end()) 
                indegree.insert({b, 0});
            
            else ans = false;
        }
        if (edgeCnt > 0 && M.size() != edgeCnt + 1) ans = false;
        if (ans) printf("Case %d is a tree.\n", ++testCases);
        else printf("Case %d is not a tree.\n", ++testCases);
    }
    return 0;
}