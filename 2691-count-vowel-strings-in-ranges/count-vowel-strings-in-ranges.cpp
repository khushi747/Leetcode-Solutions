class Solution {
public:
    bool isvowel(char &ch){
        ch = tolower(ch);
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n=words.size();
        int q=queries.size();
        vector <int> result(q);
        vector <int> cumsum(n);
        int sum=0;
        
        for(int i=0;i<n;i++){
            if(isvowel(words[i][0]) && isvowel(words[i].back())){
                sum++;
            }
            cumsum[i]=sum;
        }
        for(int j=0;j<q;j++){
            int left=queries[j][0];
            int right=queries[j][1];
            result[j]=cumsum[right]-(left>0?cumsum[left-1]:0);
        }
        return result;
    }
};