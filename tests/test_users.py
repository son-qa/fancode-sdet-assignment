from tests.conftest import instatiate_users


class Test_ToDo:

    # Test method to check completion rate of all users at once
    def test_check_todo_completion_for_fancode_city_users(self, instatiate_users):
        """Test function to check whether task completion for each user from Fancode city is 50% or more"""

        fancode_city = [(-40, 5), (5, 100)]

        test_result = []
        fancdoe_city_users = instatiate_users.get_users_lying_between(latitude=fancode_city[0],
                                                                      longitude=fancode_city[1])

        # When no fancode city users exists
        if not fancdoe_city_users:
            print('No users found hence passing the test')

        # When fancode city users exists
        else:
            for user in fancdoe_city_users:
                all_todo = user.todo.values()
                total_tasks = len(all_todo)
                completed_todo_count = sum([todo.completed for todo in all_todo])
                if completed_todo_count >= total_tasks / 2:
                    test_result.append(True)
                else:
                    print(f'For user {user.name} having id {user.id} task completion rate is not more than 50%\n'
                          f'total tasks = {total_tasks}, completed tasks = {completed_todo_count}')
                    test_result.append(False)

        assert all(test_result)
