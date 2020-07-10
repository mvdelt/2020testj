# i. 스택오버플로답변에서 argparse 예제코드 긁어온것. /2020.06.19.금욜.작성.
# - 이걸사용하면 커맨드라인 아규먼트로 리스트 넣어준걸 파싱할수있음.
# (커맨드라인 아규먼트들은 항상 string 으로 전달됨. 커맨드라인 아규먼트로 list 등 다른타입을 넣어주려면 파싱해야함.)

import argparse
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--lista",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=int,
  default=[1, 2, 3],  # default if nothing is provided
)
CLI.add_argument(
  "--listb",
  nargs="*",
  type=float,  # any type/callable can be used here
  default=[],
)

# parse the command line
args = CLI.parse_args()
# access CLI options
print("lista: %r" % args.lista)
print("listb: %r" % args.listb)
import sys
print('j) sys.argv:',sys.argv)


# You can then call it using

# $ python my_app.py --listb 5 6 7 8 --lista  1 2 3 4
# lista: [1, 2, 3, 4]
# listb: [5.0, 6.0, 7.0, 8.0]