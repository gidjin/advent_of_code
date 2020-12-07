from doit.action import CmdAction


def task_sync():
    """start docker-sync"""

    return {
        'actions': ['docker-sync start'],
        }


def task_test():
    """run tests for day"""

    for day in [1, 2, 3, 4, 5, 6]:
        yield {'name': f'day{day}',
               'verbosity': 2,
               'actions': [f'docker-compose -f docker-compose.yml -f docker-compose-dev.yml run --rm 2020day{day} pytest']}


def task_test():
    """run tests for day"""

    for day in [1, 2, 3, 4, 5, 6]:
        yield {'name': f'day{day}',
               'verbosity': 2,
               'actions': [f'docker-compose -f docker-compose.yml -f docker-compose-dev.yml run --rm 2020day{day} pytest']}
