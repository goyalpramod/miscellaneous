//linear and binary search
#include <iostream>
using namespace std;

template <class T>
class Search
{
public:
    void linear_search(T array[], T n, int size)
    {
        int isElement = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == n)
            {
                isElement = 1;
                cout << "The element " << n << " is at " << i + 1 << " position" << endl;
            }
        }
        if (isElement == 0)
        {
            cout << "No such element exists" << endl;
        }
    }

    void binary_search(T array[], T n, int size, int low, int high)
    {
        if(low > high){
            cout<<"No such element exists"<<"\n";
        }else{
            int mid = (low + high) / 2;
            if (array[mid] == n)
            {
                cout << "The element exists at index "<<mid<<"\n";
            }
            else if (n > array[mid])
            {
                low = mid + 1;
                binary_search(array,n,size,low,high);
            }
            else
            {
                high = mid - 1;
                binary_search(array,n,size,low,high);
            }
        }
    }
};

int main()
{
    Search<int> s1;
    int size = 5;
    int n = 9;
    int arr[] = {1, 5, 8, 3, 2};

    s1.linear_search(arr, n, size);

    Search<int> s2;
    int size2 = 5;
    int n2 = 7;
    int arr2[] = {1, 3, 5, 7, 9};

    s2.binary_search(arr2, n2, size2, 0, size2 - 1);

    return 0;
}