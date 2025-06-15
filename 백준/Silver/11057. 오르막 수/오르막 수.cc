#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  
  vector<vector<int>>dp;
  dp.push_back({1,1,1,1,1,1,1,1,1,1});
    
  for (int i=0; i<n-1; i++){
    vector<int> temp;
    int t=0;
    for (int j=0; j<10;j++){
      t+=dp[i][j]%10007;
      temp.push_back(t);
    }
    dp.push_back(temp);
  }
  int ans = 0;
  for (int i=0; i<10; i++){
    
     ans = (ans+dp[n-1][i])%10007;
  }
  cout<<ans;

    return 0;
}

