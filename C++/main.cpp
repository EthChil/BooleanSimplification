#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <boost/algorithm/string.hpp>

using namespace std;

int main() {
    string rawBool;

    vector<string> tokens;

    while(cin >> rawBool){
        if(!rawBool.find("+")) tokens.push_back(boost::algorithm::trim_copy(rawBool));
    }

    cout << tokens[1] << endl;
    vector< vector<int> > data;

    data.push_back(vector<int> (5, 40));

    if(data[0][0] > 0){
        cout << "TADA" << endl;
    }

    cout << data[0][0] << endl;

    return 0;
}