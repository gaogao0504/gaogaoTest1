# 添加成员


class AddMember:
    def add_member(self):
        # 局部倒入，避免循环导入
        from pythoncode.homework.web_Enterpriselogin.contact_page import Contact
        return Contact()
