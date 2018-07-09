"""
Johnny has a younger sister Anne, who is very clever and smart. As she came home from the kindergarten, she told his brother about the task that her kindergartener asked her to solve. The task was just to construct a triangle out of four sticks of different colours. Naturally, one of the sticks is extra. It is not allowed to break the sticks or use their partial length. Anne has perfectly solved this task, now she is asking Johnny to do the same.

The boy answered that he would cope with it without any difficulty. However, after a while he found out that different tricky things can occur. It can happen that it is impossible to construct a triangle of a positive area, but it is possible to construct a degenerate triangle. It can be so, that it is impossible to construct a degenerate triangle even. As Johnny is very lazy, he does not want to consider such a big amount of cases, he asks you to help him.

Input
The first line of the input contains four space-separated positive integer numbers not exceeding 100 — lengthes of the sticks.

Output
Output TRIANGLE if it is possible to construct a non-degenerate triangle. Output SEGMENT if the first case cannot take place and it is possible to construct a degenerate triangle. Output IMPOSSIBLE if it is impossible to construct any triangle. Remember that you are to use three sticks. It is not allowed to break the sticks or use their partial length.
"""
# check for the sum of every two lengths, if they are larger than any of the other two lengths, it is a triangle

def check_triangle_func(one, two, three):
    if (one + two > three) and (one + three > two) and (two + three > one):
        return True

def check_segment_func(one, two, three):
    if (one + two == three) or (one + three == two) or (two + three == one):
        return True

first, second, third, fourth = map(int, input().split())

if check_triangle_func(first, second, third) or check_triangle_func(first, second, fourth) or check_triangle_func(first, third, fourth) or check_triangle_func(second, third, fourth):
    print("TRIANGLE")
else:
    if check_segment_func(first, second, third) or check_segment_func(first, second, fourth) or check_segment_func(first, third, fourth) or check_segment_func(second, third, fourth):
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")
