#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Tess Bursic

FIRST_VALUE = 10  # TODO: Replace 0 with the 1st value provided by Prof. Zhao
SECOND_VALUE = 5  # TODO: Replace 0 with the 2nd value provided by Prof. Zhao

print("Completed story problem:")
print(f"What value do you get when you raise FIRST_VALUE to the power of SECOND_VALUE?")

student_answer = 100000  # TODO: Replace 0 with your answer

correct_result = FIRST_VALUE^SECOND_VALUE  # TODO: Replace 0 with a function

if student_answer == correct_result:
    print(f"The correct value is {correct_result}. You answered the problem correctly!")
else:
    print(f"The correct value is {correct_result}. Your answer is incorrect. Try again next time!")
