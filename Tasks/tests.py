from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import TaskModel

class TaskFilterTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.login(username='testuser', password='pass123')

        TaskModel.objects.create(user=self.user, task_name='Buy groceries', task_status='Pending', task_priority='High')
        TaskModel.objects.create(user=self.user, task_name='Clean house', task_status='Completed', task_priority='Low')

    def test_filter_by_status(self):
        response = self.client.get(reverse('task-list'), {'task_status': 'Pending'})
        self.assertContains(response, 'Buy groceries')
        self.assertNotContains(response, 'Clean house')

    def test_filter_by_priority(self):
        response = self.client.get(reverse('task-list'), {'task_priority': 'High'})
        self.assertContains(response, 'Buy groceries')
        self.assertNotContains(response, 'Clean house')

    def test_filter_by_name(self):
        response = self.client.get(reverse('task-list'), {'task_name': 'groceries'})
        self.assertContains(response, 'Buy groceries')
        self.assertNotContains(response, 'Clean house')


class TaskAuthorizationTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        self.task = TaskModel.objects.create(user=self.user1, task_name='User1 Task')

    def test_logged_out_user_redirected(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_user_cannot_see_other_users_task(self):
        self.client.login(username='user2', password='pass123')
        response = self.client.get(reverse('task-list'))
        self.assertNotContains(response, 'User1 Task')


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.task = TaskModel.objects.create(
            user=self.user,
            task_name='Test Task',
            task_status='Pending',
            task_priority='High'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.task_name, 'Test Task')
        self.assertEqual(self.task.task_status, 'Pending')
        self.assertEqual(self.task.task_priority, 'High')

    def test_default_status_is_pending(self):
        task = TaskModel.objects.create(user=self.user, task_name='Another Task')
        self.assertEqual(task.task_status, 'Pending')

    def test_default_priority_is_medium(self):
        task = TaskModel.objects.create(user=self.user, task_name='Another Task')
        self.assertEqual(task.task_priority, 'Medium')

    def test_default_description(self):
        task = TaskModel.objects.create(user=self.user, task_name='Another Task')
        self.assertEqual(task.task_description, 'Add Task Description here')

    def test_task_update(self):
        self.task.task_status = 'Completed'
        self.task.save()
        updated_task = TaskModel.objects.get(id=self.task.id)
        self.assertEqual(updated_task.task_status, 'Completed')

    def test_task_delete(self):
        task_id = self.task.id
        self.task.delete()
        self.assertFalse(TaskModel.objects.filter(id=task_id).exists())

    def test_task_linked_to_user(self):
        self.assertEqual(self.task.user, self.user)