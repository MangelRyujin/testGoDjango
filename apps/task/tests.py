from django.test import TestCase
from apps.task.models import Task
# Create your tests here.

class TaskModelTest(TestCase):
    
    def test_create_task(self):
        task = Task.objects.create(title="Test Task 1", description="This is a test task create by MangelRyujin.", state="pendiente")
        self.assertEqual(task.title, "Test Task 1")
        self.assertEqual(task.description, "This is a test task create by MangelRyujin.")
        self.assertEqual(task.state, "pendiente")
        
    def test_edit_task(self):
        task = Task.objects.create(title="Test Task 1", description="Initial description", state="pendiente")
        
        updated_task_title = "Updated Test Task 1"
        updated_task_description = "This is an updated description by MangelRyujin."
        updated_task_state = "en progreso"
        task.title = updated_task_title
        task.description = updated_task_description
        task.state = updated_task_state
        task.save()
        
        self.assertEqual(task.title, updated_task_title)
        self.assertEqual(task.description, updated_task_description)
        self.assertEqual(task.state, updated_task_state)