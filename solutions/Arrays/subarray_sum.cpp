// Title: Two Sum 
// Category: Arrays 
// Difficulty: Easy 
// Time Complexity: O(n) 
// Space Complexity: O(n) 
// Tags: Hash Map, Prefix Sum, Array Iteration
// Source: LeetCode 1

//Subarray Sum Equals K:
//Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals k.

#include<iostream>
#include<chrono>
using namespace std;
auto start = chrono::steady_clock::now();
int main()
{
    //int arr[] = {5, 2, 7, 0};  // subarrays are = {5, 2} {7, 0} {7}
    int ar2[] = {3, 4, 6, 1};  // subarrays are = {3, 4} {6, 1} 
    int k = 7;
    int size = sizeof(ar2)/sizeof(ar2[0]);
    cout << size << endl;
    int res = 0;
    for(int i=0; i<size; i++)
    {
        int sum = 0;
        for(int j = i; j<size; j++)
        {
            sum += ar2[j];
            if (sum == k)
                res++;
        }
    }

    cout << res << endl;


    cout << "\n";
    auto end = chrono::steady_clock::now();
    auto diff = end - start;
    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    return 0;
}


/* nav
  - Trees:
      - Inorder Traversal: Trees/inorder_traversal.md
      - BST Insert: Trees/bst_insert.md
  - Graphs:
      - BFS: Graphs/bfs.md
      - Dijkstra: Graphs/dijkstra.md
  - Dynamic Programming:
      - 0/1 Knapsack: Dynamic Programming/knapsack.md
      - Longest Increasing Subsequence: Dynamic Programming/lis.md
*/