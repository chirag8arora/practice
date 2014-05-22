import random


# class Agent():

#     def __init__(self, capability):
#         self.capability = capability


# class Task():

#     def __init__(self, difficulty):
#         self.difficulty = difficulty


def main(agents, tasks, budget):
    tasks_count = len(tasks)
    tasks = sorted(tasks)
    agents = sorted(agents)
    assignment = []

    while tasks:
        task = tasks.pop(0)
        while agents:
            agent = agents.pop(0)
            if task <= agent:
                assignment.append((task, agent))
                budget -= agent
                break
        if budget < 0:
            return False
    if len(assignment) == tasks_count:
        return assignment
    else:
        return False


if __name__ == '__main__':
    # agents
    # agents = []
    # for i in range(10):
    #     capability = random.randrange(10)
    #     agents.append(Agent(capability))

    # Tasks
    # tasks = []
    # for i in range(5):
    #     difficulty = random.randrange(10)
    #     tasks.append(Task(difficulty))
    agents = [1, 2, 2, 3, 5, 7, 15, 20]
    tasks = [2, 4, 3, 6, 2]
    budget = 19
    print main(agents, tasks, budget)
