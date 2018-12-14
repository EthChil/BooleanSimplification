#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>

using namespace std;

int main() {
    string rawBool;

    vector<string> tokens;

    vector< vector<int> > terms;

    while(cin >> rawBool){
        if(rawBool.find("=") != string::npos) break;
        if(rawBool.find("+") == string::npos) {
            vector<int> term;

            for(int i = 0; i < rawBool.size(); i++){
                if(term[int(rawBool[i]) - 65] == nullptr) term.push_back()
                term.insert(int(rawBool[i]) - 65, )
            }
        }
    }

    for(int i = 0; i < tokens.size(); i++) cout << tokens[i] << endl;
    vector< vector<int> > data;

    data.push_back(vector<int> (5, 40));

    if(data[0][0] > 0){
        cout << "TADA" << endl;
    }

    cout << data[0][0] << endl;

    return 0;
}