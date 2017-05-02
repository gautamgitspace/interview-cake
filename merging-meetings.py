"""
algo - if end_first >= start_second:
            start = start_first
            end = end_second
So, we could compare every meeting to every other meeting in this way,
merging them or leaving them separate. => O(n^2)
What if we sorted our list of meetings by start time?
Then any meetings that could be merged would always be adjacent!
So we could sort our meetings, then walk through the sorted list and see if
each meeting can be merged with the one after it.
Sorting takes O(nlgn) time in the worst case. If we can then do the merging in one pass,
that's another O(n) time, for O(nlgn) overall.
if input is sorted, we can avoid sorting and it takes O(n) for time and O(n) for space
"""
def condensed_meeting_times(meetings):
    sorted_meetings = sorted(meetings)
    print sorted_meetings
    condensed_meetings = [sorted_meetings[0]]
    
    for current_start, current_end in sorted_meetings[1:]:
        print "c_s & c_e: ", current_start, current_end
        last_merged_start, last_merged_end = condensed_meetings[-1]
        print "l_m_s & l_m_e: ", last_merged_start, last_merged_end

        if current_start <= last_merged_end:
            condensed_meetings[-1] = (last_merged_start, max(last_merged_end, current_end))
        else:
            condensed_meetings.append((current_start, current_end))

    return condensed_meetings


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
result = condensed_meeting_times(meetings)
print result
