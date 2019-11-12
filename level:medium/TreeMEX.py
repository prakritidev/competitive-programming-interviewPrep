'''
You have a tree T with n vertices. Consider an ordering P=(v1,…,vn) of vertices of T. We construct a sequence A(P)=(a1,…,an) using the following process:

Set all ai=−1.
Process vertices in order v1,…,vn. For the current vertex vi set ai=MEX(au1,…,auk), where u1,…,uk is the set of neighbours of vi.
For instance, let n=3 and T be the tree with edges (1,2) and (2,3). Then, for the ordering P=(1,2,3) we obtain the sequence A(P)=(0,1,0), while for the ordering P=(2,3,1) we obtain A(P)=(1,0,1).

Consider all n! orders P. How many different sequences A(P) can we obtain? Print the answer modulo 109+7.

Input:
The first line contains an integer T, denoting number of test cases.

The first line of each test case contains an integer n− the number of vertices in the tree (1≤n≤105).

The following n−1 lines describe the tree edges. Each of these lines contains two integers ui,vi describing an edge between ui and vi (1≤ui,vi≤n, ui≠vi).

Output:
Print the answer modulo 109+7.

Constraints
1≤T≤10
1≤n≤105
1≤ui,vi≤n
ui≠vi
Sample Input:
1
5
1 2
2 3
3 4
4 5
Sample Output:
6

EXPLANATION:
For the sample case, the possible sequences A(P) are (0,1,0,1,0), (0,1,2,0,1), (0,2,1,0,1), (1,0,1,0,1), (1,0,1,2,0), (1,2,0,1,0).

'''
