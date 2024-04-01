##############################################################################
# CCO1100-01 Lab 4                                                           #
# answers to questions                                                       #
##############################################################################

#
# Q1: please fully parenthesize every subexpression by putting '(' and ')'.
# Failing to "fully" parenthesize every subexpression might lead to 0 point.
#
q1_a_answer = "(((var1*8)-var2)+(32/var3))"
q1_b_answer = "(var1-((6**4)*(var2**3)))"

#
# Q2: please replace 'None' by your answer (integer):
# Choose the first two operators to be evaluated,
# considering operator precedence and associativity, in order.
#
# a +(1) b *(2) c
# For example, given the expression above, if *(2) is evaluated first,
# then your answer should be q2_example_operator1 = 2, q2_example_operator2 = 1.
#
# (a) var1 *(1) var2 *(2) var3 -(3) var4
q2_a_operator1 = 1
q2_a_operator2 = 2
# (b) var1 *(1) var2 /(2) var3
q2_b_operator1 = 1
q2_b_operator2 = 2
# (c) var1 **(1) var2 **(2) var3
q2_c_operator1 = 2
q2_c_operator2 = 1

#
# Q3: please replace 'None' by your answer (Boolean: True or False):
#
q3_a_answer = True
q3_b_answer = True
q3_c_answer = True
q3_d_answer = False

#
# Q4: please replace the empty strings by your answer (string):
#
q4_a_answer = "24 " + "not in" + " nums"
q4_b_answer = "'Ellen' " + "in" + " names"
q4_c_answer = "last_name " + "is" + " 'Morris' " + "or" + \
                " last_name " + "is" + " 'Morrison'"

#
# Q5: please fill in the empty string with your answer (string):
#
q5_answer = "print('John Doe\n123 Main Street\nAnytown, Maryland 21009')"

#
# Q6: please fill in the empty string with your answer (string):
#
q6_answer = "print('It\'s raining today.')"

#
# Q7: please fill in the empty strings with your answer (string):
#
q7_a_answer = "2.0"
q7_b_answer = "2"
q7_c_answer = "2.0"

##############################################################################
# Grading code. Please do not touch any code below this line:                #
##############################################################################
SEP = '-' * 79
print(SEP)
print('CCO1100-01 Lab 4')
print('Answers to questions')
print(SEP)
print('Answer Q1:', q1_a_answer)
print('Answer Q1:', q1_b_answer)
print(SEP)
print('Answer Q2:', q2_a_operator1)
print('Answer Q2:', q2_a_operator2)
print('Answer Q2:', q2_b_operator1)
print('Answer Q2:', q2_b_operator2)
print('Answer Q2:', q2_c_operator1)
print('Answer Q2:', q2_c_operator2)
print(SEP)
print('Answer Q3:', q3_a_answer)
print('Answer Q3:', q3_b_answer)
print('Answer Q3:', q3_c_answer)
print('Answer Q3:', q3_d_answer)
print(SEP)
print('Answer Q4:', q4_a_answer)
print('Answer Q4:', q4_b_answer)
print('Answer Q4:', q4_c_answer)
print(SEP)
print('Answer Q5:', q5_answer)
print(SEP)
print('Answer Q6:', q6_answer)
print(SEP)
print('Answer Q7:', q7_a_answer)
print('Answer Q7:', q7_b_answer)
print('Answer Q7:', q7_c_answer)
print(SEP)
