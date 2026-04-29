class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> key;
        
        for (string i : strs){
            string temp = i;
            sort(temp.begin(), temp.end());
            key[temp].push_back(i);

        }    
        vector<vector<string>> result;
        for(auto j: key){
            result.push_back(j.second);
                
        }
        return result;
        
    }
};
