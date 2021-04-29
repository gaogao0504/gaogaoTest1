from pythoncode import MainPage


class TestADDmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_addmember(self):
        ele = self.main.goto_contact().click_add_member().add_member().get_member()
        assert ele == 1


