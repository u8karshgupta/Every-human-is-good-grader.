# conditional statements
p = "I am a human being."                                                                   # statement a
q = "I am good."                                                                            # statement b
r = "Good graders study well."                                                              # statement c
s = "Humans love graders."                                                                  # statement d
t = "Every human does not study well."                                                      # statement e
u = "Is every human good grader?"                                                           # to be proven

# boolean values of condotional statements
p_truth_value = 0
q_truth_value = 0
r_truth_value = 0
s_truth_value = 0
t_truth_value = 0
u_truth_value = 0
u_truth_values = []                                                                         # list to store all truth values of truth table
answer = 1;

# generating truth table with boolean values of conditional statements
p_truth_value = 0
for p_truth_value in range(0,2):
    q_truth_value = 0
    for q_truth_value in range(0,1):
        r_truth_value = 0
        for r_truth_value in range(0,2):
            s_truth_value = 0
            for s_truth_value in range(0,1):
                t_truth_value = 0
                for t_truth_value in range(0,2):
                    u_truth_value = 0
                    for u_truth_value in range(0,2):
                        answer = ((not ((p_truth_value) and (r_truth_value and t_truth_value))) or (u_truth_value))
                        u_truth_values.append(bool(answer))
                        u_truth_value+=1
                    t_truth_value+=1
                s_truth_value+=1
            r_truth_value+=1
        q_truth_value+=1
    p_truth_value+=1

# calculating tautology or fallacy or contradiction
for i in u_truth_values:
    answer*=i

# printing answer based on truth table
print(u)
if answer == 1:
    print("The given statement is a Tautology for given information. Hence the answer is Yes.")
elif answer == 0:
    print("The given statement is a Contradictoion for given information. Hence the answer is No.")
