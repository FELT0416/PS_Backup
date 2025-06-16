#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<vector<long long>> dp(32, vector<long long>(32, 0));
  dp[0][0]=1;

  for(int i=0; i<31; i++){
    for(int j=0; j<31; j++){
      if (i!=0){
        dp[i][j]+=dp[i-1][j+1];
      }
      if (j!=0){
        dp[i][j]+=dp[i][j-1];
      }
     }
  }
  
  int n;
  cin>>n;
  while(n!=0){ 
    cout<<dp[n][0]<<"\n";
    cin>>n;
  }

  return 0;
}