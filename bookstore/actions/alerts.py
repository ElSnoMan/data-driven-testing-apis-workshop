from pylenium.driver import Pylenium
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert


class AlertActions:
    def __init__(self, py: Pylenium):
        self.py = py

    def wait_for_alert(self) -> Alert:
        return self.py \
            .wait(ignored_exceptions=[NoAlertPresentException]) \
            .until(lambda driver: driver.switch_to_alert())

    def accept(self) -> Pylenium:
        self.wait_for_alert().accept()
        return self.py
