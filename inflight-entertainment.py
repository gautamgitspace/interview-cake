#nested loop approach: outer - first_movie_length, inner - check for condition
#flight_length-first_movie_length = second_movie_length for every item in outer loop.
#this gives O(n^2)
"""
for item in m:
    fml = item
    for item2 in m:
        if (fl-fml==item2):
            return True
"""
#A better approach is to use set() which will give us constant-time lookups:
#this gives: O(n) time, and  O(n) space



def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_lengths_seen = set()
    for i in movie_lengths:
        second_movie_length = flight_length-i
        if second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(i)

movie_lengths = [2.5, 2.45, 2.35, 2.4, 2.67, 3.1, 2.33]
flight_length = 5
result = can_two_movies_fill_flight(movie_lengths,flight_length)
print result
