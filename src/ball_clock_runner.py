"""
Ball CLock Runner Additional Usage Info:
  Mode 1: ball_clock_runner <list of integers specifying balls> [-m 1]
\tex: "% ball_clock_runner 30 45 -m 1"
  Mode 2: ball_clock_runner <list of integers specifying balls> -t <integer for number of minutes to run> -m 2
\tex: "ball_clock_runner 30 -t 325 -m 2"
"""

from ball_clock import ClockControl
import argparse


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "balls",
        type=int,
        nargs="+",
        help="List of integers specifying balls for ball clock (between 27 and 127)",
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        default=1,
        help="Mode of Ball Clock Program -- 1 or 2 (default 1).",
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        default=325,
        help="Number of minutes to run ball clock using mode 2 (default 325).",
    )
    args = parser.parse_args()
    mode = args.mode
    if mode == 1:
        for b in args.balls:
            if 27 <= b <= 127:
                clock_controller = ClockControl(b)
                clock_controller.mode_one()
            else:
                print("Invalid ball number -- should be between 27 and 127")
    elif mode == 2:
        for b in args.balls:
            if 27 <= b <= 127:
                print(
                    "Running Ball Clock Mode 2 with {} balls for {} minutes".format(
                        args.time, b
                    )
                )
                clock_controller = ClockControl(b)
                clock_controller.mode_two(args.time)
            else:
                print("Invalid ball number -- should be between 27 and 127")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
