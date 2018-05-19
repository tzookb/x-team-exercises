def share_candies_direction(grades, candies):
    for i in xrange(len(grades)):
        if i > 0 and grades[i] > grades[i - 1] and candies[i] <= candies[i - 1]:
            candies[i] = candies[i - 1] + 1
        if i < n - 1 and grades[i] > grades[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
        i = i + 1
    return candies


def candies(n, grades):
    candies_per_kid = [1] * n
    candies_per_kid = share_candies_direction(grades, candies_per_kid)
    grades.reverse()
    candies_per_kid.reverse()
    candies_per_kid = share_candies_direction(grades, candies_per_kid)
    return candies_per_kid