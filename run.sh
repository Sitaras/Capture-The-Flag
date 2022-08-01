#! /bin/bash
if (( $#  >= 1 ))
then
  for scriptNo in $@
  do
    if (($scriptNo == 4 ))
      then
        echo "Execution of Q4:"
        python3 ./q4/q4_padding_oracle.py ad8bb176da1f40a98385ad0ae9777c3208b78ae57a7fec84092b2cbbaf2ab1c0
    elif (($scriptNo == 5 ))
      then
        echo "Execution of Q5:"
        python3 ./q5/q5_buffer_overflow_send_file.py
    elif (($scriptNo == 6 ))
      then
        echo "Execution of Q6:"
        python3 ./q6/q6_buffer_overflow_system.py
    fi
  done
else
  echo "Execution of Q4:"
  python3 ./q4/q4_padding_oracle.py ad8bb176da1f40a98385ad0ae9777c3208b78ae57a7fec84092b2cbbaf2ab1c0
  echo "Execution of Q5:"
  python3 ./q5/q5_buffer_overflow_send_file.py
  echo "Execution of Q6:"
  python3 ./q6/q6_buffer_overflow_system.py
fi
