// bubble sort, insertion sort,merge sort,quick sort, counting sort,selection sort,radix sort

#include <iostream>
using namespace std;

template <class T>
class different_sorts
{
public:
    void bubble_sort(T arr[], int n)
    {
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    T temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    void insertion_sort(T arr[], int n)
    {
        for (int i = 1; i < n; i++)
        {
            int key = arr[i];
            int j = i;
            while (key < arr[j - 1])
            {
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = key;
        }
    }

    void count_sort(T arr[], int n)
    {
        T sorted_arr[n + 1];
        int temp_array[10];
        for (int i = 0; i < 10; i++)
        {
            temp_array[i] = 0;
        }
        for (int i = 0; i < n; i++)
        {
            temp_array[arr[i]]++;
        }
        for (int i = 1; i < 10; i++)
        {
            temp_array[i] += temp_array[i - 1];
        }
        int k = n - 1;
        int j = 0;
        while (j < n + 1)
        {
            sorted_arr[temp_array[arr[k]]] = arr[k];
            temp_array[arr[k]]--;
            k--;
            j++;
        }
        for (int i = 0; i < n + 1; i++)
        {
            sorted_arr[i] = sorted_arr[i + 1];
        }
        sorted_arr[n] = 0;
        for (int i = 0; i < n; i++)
        {
            arr[i] = sorted_arr[i];
        }
    }

    void radix_count_sort(T arr[], int n, int expo)
    {
        T sorted_arr[n + 1];
        T temp_array[10];
        for (int i = 0; i < 10; i++)
        {
            temp_array[i] = 0;
        }
        for (int i = 0; i < n; i++)
        {
            temp_array[((arr[i]) / expo) % 10]++;
        }
        for (int i = 1; i < 10; i++)
        {
            temp_array[i] += temp_array[i - 1];
        }
        int k = n - 1;
        int j = 0;
        while (j < n + 1)
        {
            sorted_arr[temp_array[(arr[k] / expo) % 10]] = arr[k];
            temp_array[(arr[k] / expo) % 10]--;
            k--;
            j++;
        }
        for (int i = 0; i < n + 1; i++)
        {
            sorted_arr[i] = sorted_arr[i + 1];
        }

        for (int i = 0; i < n; i++)
        {
            arr[i] = sorted_arr[i];
        }
    }

    void radix_sort(T arr[], int n, int max_num)
    {
        for (int expo = 1; max_num / expo > 0; expo *= 10)
        {
            radix_count_sort(arr, n, expo);
        }
    }

    void merge(T arr[], int low, int mid, int high)
    {
        int n1 = mid - low + 1;
        int n2 = high - mid;

        T l[n1];
        T r[n2];

        for (int a = 0; a < n1; a++)
        {
            l[a] = arr[low + a];
        }

        for (int b = 0; b < n2; b++)
        {
            r[b] = arr[mid + 1 + b];
        }

        int i = 0;
        int j = 0;
        int k = low;

        while (i < n1 && j < n2)
        {
            if (l[i] <= r[j])
            {
                arr[k] = l[i];
                i++;
                k++;
            }
            else
            {
                arr[k] = r[j];
                j++;
                k++;
            }
        }

        while (i < n1)
        {
            arr[k] = l[i];
            i++;
            k++;
        }

        while (j < n2)
        {
            arr[k] = r[j];
            j++;
            k++;
        }
    }

    void mergeSort(T arr[], int low, int high)
    {
        int mid;
        if (low < high)
        {
            mid = low + (high - low) / 2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid + 1, high);
            merge(arr, low, mid, high);
        }
    }

    void display(T arr[], int n)
    {
        for (int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main()
{
    different_sorts<int> b;

    int arr[] = {1, 7, 4, 9, 2, 3};
    int n = 6;

    b.display(arr, n);
    // b.bubble_sort(arr,n);
    // b.display(arr,n);
    // b.insertion_sort(arr, n);
    // b.display(arr, n);
    // b.count_sort(arr, n);
    // b.display(arr, n);
    // b.radix_sort(arr,n,9);
    // b.display(arr,n);
    b.mergeSort(arr,0,n-1);
    b.display(arr,n);

    return 0;
}