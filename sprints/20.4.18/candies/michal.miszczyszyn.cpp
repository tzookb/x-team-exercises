#include <bits/stdc++.h>


int main() {
    int n;
    std::cin >> n;
    std::vector<int> ratings(n);
    std::vector<int> candies(n, 1);
    
    for (int i = 0; i < n; ++i) {
        std::cin >> ratings[i];
    }
    
    int numcandies = 1;
    for (int i = 1; i < n; ++i) {
        if (ratings[i] > ratings[i-1]) {
            ++numcandies;
        } else {
            numcandies = 1;
        }
        candies[i] = numcandies;
    }

    numcandies = 1;
    for (int i = n - 2; i >= 0; --i) {
        if (ratings[i] > ratings[i+1]) {
            ++numcandies;
        } else {
            numcandies = 1;
        }
        if (numcandies > candies[i]) {
            candies[i] = numcandies;
        }
    }
    
    long total = std::accumulate(candies.rbegin(), candies.rend(), 0L);

    std::cout << total;
    return 0;
}

