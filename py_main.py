def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= verify_answer(my_answers,answers)
    print("{}".format(results))

    count_results = get_result_count(results);

    if count_results[0]/len(answers) > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_results[0]) + " out of "+str(len(answers))+"."
    elif count_results[1]/len(answers) >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_results[0]) + " out of "+str(len(answers))+"."

def get_result_count(results):
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    return [count_correct, count_incorrect]

def verify_answer(my_answers,answers):
    results = []
    i=0;
    while i < len(answers):
        print("{} == {}\n".format(my_answers[i],answers[i]))
        if my_answers[i] == answers[i]:
            results.append(True)
        else:
            results.append(False)
        i+=1
    return results

print(check_answers(['a','b','c','d','e','f','g','h'],['a','b','c','d','e','f','h','h']))
print(check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"]))


"""
Step 2- Another Solution
"""
def check_answer2(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers2(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer2(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."

print(check_answers2(['a','b','c','d','e','f','g','h'],['a','b','c','d','e','f','h','h']))
print(check_answers2([1,2,3,4,5],["badger","badger","badger","badger","badger"]))
