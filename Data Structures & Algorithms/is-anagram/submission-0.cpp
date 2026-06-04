class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size())
        return false;

        unordered_map<char,int> scount;
        unordered_map<char,int> tcount;

        for(int i=0;i<s.size();i++){
            scount[s[i]]++;
            tcount[t[i]]++;
        }
        for(int i=0;i<scount.size();i++){
            if(scount[i]!=tcount[i])
            return false;
        }
        return true;
    }
};
