#include <iostream>

using namespace std;

int main(){
    int n, d, start, end;
    int i, curr = 0, tmp = 0;

    n = 97;
    d = 53;
    start = -92;
    end = 441;

    curr = start;
    for(i = 1; i < n-1; i++){
        cout << curr << " " << tmp << " " << curr + tmp << endl;
        tmp = (n - i - 1) * -d;
        if(curr + tmp > end)
            break;
        curr += d;
    }

    cout << curr << " " << tmp << " " << curr + tmp << endl;
    cout << curr + tmp - end << endl; 
}
