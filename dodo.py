from doit.action import CmdAction


def task_sync():
    """start docker-sync"""

    return {
        'actions': ['docker-sync start'],
        }


def task_test():
    """run tests for day"""

    day = 1
    while day <= 9:
        yield {'name': f'day{day}',
               'verbosity': 2,
               'actions': [f'docker-compose -f docker-compose.yml -f docker-compose-dev.yml run --rm 2020day{day} pytest']}
        day += 1
