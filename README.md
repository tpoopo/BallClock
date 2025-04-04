# Retrieve Project 
Available for cloning on GitHub: https://github.com/tpoopo/BallClock/

# Run Project
Navigate to BallClock/src directory

Use Python3 to run ball_clock_runner.py with command line args (see below)

# Ball Clock Usage
Mode 1: ball_clock_runner [list of integers specifying balls] [-m 1]
    
    % python3 ball_clock_runner 30 45 -m 1

Mode 2: ball_clock_runner [list of integers specifying balls] -t <integer for number of minutes to run> -m 2

    % python3 ball_clock_runner 30 -t 325 -m 2

# Ball Clock

Movement has long been used to measure time. For example, the ball clock is a simple device which keeps track of the passing minutes by moving ball-bearings. Each minute, a rotating arm removes a ball bearing from the queue at the bottom, raises it to the top of the clock and deposits it on a track leading to indicators displaying minutes, five-minutes and hours. These indicators display the time between 1:00 and 12:59, but without ‘a.m.’ or ‘p.m.’ indicators. Thus 2 balls in the minute indicator, 6 balls in the five-minute indicator and 5 balls in the hour indicator displays the time 5:32. Unfortunately, most commercially available ball clocks do not incorporate a date indication, although this would be simple to do with the addition of further carry and indicator tracks. However, all is not lost! As the balls migrate through the mechanism of the clock, the order they are found in can be used to determine the time elapsed since the clock had some specific ordering. The length of time which can be measured is limited because the orderings of the balls eventually begin to repeat. Your program must compute the time before repetition, which varies according to the total number of balls present.

Operation of the Ball Clock

Every minute, the least recently used ball is removed from the queue of balls at the bottom of the clock, elevated, then deposited on the minute indicator track, which is able to hold four balls. When a fifth ball rolls on to the minute indicator track, its weight causes the track to tilt. The four balls already on the track run back down to join the queue of balls waiting at the bottom in reverse order of their original addition to the minutes track. The fifth ball, which caused the tilt, rolls on down to the five-minute indicator track. This track holds eleven balls. The twelfth ball carried over from the minutes causes the five-minute track to tilt, returning the eleven balls to the queue, again in reverse order of their addition. The twelfth ball rolls down to the hour indicator. The hour indicator also holds eleven balls, but has one extra fixed ball which is always present so that counting the balls in the hour indicator will yield an hour in the range one to twelve. The twelfth ball carried over from the five-minute indicator causes the hour indicator to tilt, returning the eleven free balls to the queue, in reverse order, before the twelfth ball itself also returns to the queue.

Guidelines

The exercise should be completed in Python. You’re welcome to do it in multiple languages to show aptitude, but we would like to see the test in Python. No permutation or LCM algorithms are allowed. A full simulation is required. Please ensure that your code moves each ball.

Implementation

Valid numbers are in the range 27 to 127. Clocks must support two modes of computation.

The first mode takes a single parameter specifying the number of balls and reports the number of balls given in the input and the number of days (24-hour periods) which elapse before the clock returns to its initial ordering.

Sample Input

30 45

Output for the Sample Input

30 balls cycle after 15 days.

45 balls cycle after 378 days.

The second mode takes two parameters, the number of balls and the number of minutes to run for. If the number of minutes is specified, the clock must run to the number of minutes and report the state of the tracks at that point in a JSON format.

Sample Input

30 325

Output for the Sample Input

{“Min”:[],“FiveMin”:[22,13,25,3,7],“Hour”:[6,12,17,4,15],“Main”

[11,5,26,18,2,30,19,8,24,10,29,20,16,21,28,1,23,14,27,9]}