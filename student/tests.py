from django.test import TestCase, Client

from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUP(self):
        Student.objects.create(
            name = 'test',
            sex = 1,
            email = 'test@qq.com',
            profession = '测试',
            qq = '123456',
            phone = '13838383838',
        )

    def test_create_and_get_sex_diplay(self):
        student = Student.objects.create(
            name = 'handsome',
            sex = 1,
            email = 'someone@qq.com',
            profession = '程序员',
            qq = '121314',
            phone = '15159609096',
        )
        self.assertEqual(student.get_sex_display(), '男', '性别字段内容与展示不符！')

    def test_get_index(self):
        """测试首页可用性"""
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, '访问首页返回代码必须是200！')

    def test_post_student(self):
        """测试提交StudentForm"""
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex = 2,
            email = 'girl@qq.com',
            profession = '文秘',
            qq = '1314520',
            phone = '13145205200'
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, '数据提交未重定向，1、页面错误；2、测试数据未通过校验！')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, '添加的数据data未正确收录并展示！')


