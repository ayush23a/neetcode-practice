class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> count;
        for (int i = 0; i<nums.size(); i++){
            count[nums[i]]++;
        }

        vector<pair<int, int>> v(count.begin(), count.end()); // copy map -> vector
        sort(v.begin(), v.end(), [](pair<int, int>& a, pair<int, int>& b){ 
            return a.second > b.second; 
            });

        vector<int> result;
        for(int i =0; i<k; i++){
            result.push_back(v[i].first);
        }
        return result;
    }
};
