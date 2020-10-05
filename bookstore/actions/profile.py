from pylenium.driver import Pylenium

from bookstore.actions.alerts import AlertActions


class ProfileActions:
    def __init__(self, py: Pylenium):
        self.py = py

    REMOVE_BOOK_ICON = '#delete-record-undefined'
    MODAL_OK_BUTTON = '#closeSmallModal-ok'

    def remove_first_book(self) -> 'ProfileActions':
        self.py.get(self.REMOVE_BOOK_ICON).click()
        self.py.get(self.MODAL_OK_BUTTON).click()
        AlertActions(self.py).accept()
        return self

    def remove_book_by_name(self, name) -> 'ProfileActions':
        row = self.py.getx(f"//*[@role='rowgroup' and contains(., '{name}')]")
        row.get(self.REMOVE_BOOK_ICON).click()
        self.py.get(self.MODAL_OK_BUTTON).click()
        AlertActions(self.py).accept()
        return self
