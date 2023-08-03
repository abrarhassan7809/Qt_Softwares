from ui_interface import *
from Custom_Widgets.Widgets import *
from function import AppFunctions
import os
import sys

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QSettings()

        loadJsonStyle(self, self.ui)
        self.show()

        self.settings.setValue("THEME", "Default-Dark")
        QAppSettings.updateAppSettings(self)

        db_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/app_db.db'))
        self.app_functions = AppFunctions()
        self.app_functions.create_tables(db_folder)

        self.ui.showUserFromBtn.clicked.connect(self.add_user)
        self.display_all_users()

    def add_user(self):
        user_name = self.ui.userName.text()
        email = self.ui.email.text()
        phone_no = self.ui.phoneNo.text()

        db_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/app_db.db'))
        self.app_functions.add_user(db_folder, user_name, email, phone_no)
        self.display_all_users()

    def display_all_users(self):
        db_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/app_db.db'))
        users = self.app_functions.get_all_users(db_folder)
        self.app_functions.display_users(self.ui.tableWidget, users)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

