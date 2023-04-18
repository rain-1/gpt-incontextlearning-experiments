import lib

def problem_set_1():
    for _ in range(30):
        lib.generate_shot(easy=True)
    lib.generate_shot(easy=True, with_solution_key=True)

# GPT-4 can fail at this task
def problem_set_2():
    for _ in range(30):
        lib.generate_shot(easy)
    lib.generate_shot(easy, with_solution_key=True)

problem_set_1()
