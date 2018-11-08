import json
import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class CLI:
    def __init__(self, username, password):
        self.driver = None
        self.username = username
        self.password = password

    def connect(self, webdriver_path='/usr/lib/chromium-browser/chromedriver'):
        if self.driver is not None:
            raise RuntimeError("driver already initialized")

        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": os.getcwd()}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(webdriver_path, options=options)

        self.driver.get('https://www.edaplayground.com/login')

        username_input = self.driver.find_element_by_name("j_username")
        username_input.send_keys(self.username)

        password_input = self.driver.find_element_by_name("j_password")
        password_input.send_keys(self.password)

        time.sleep(0.5)

        login_form = self.driver.find_element_by_name("loginForm")
        login_form.submit()

        time.sleep(0.5)

    def run_simulation(self, design="", testbench="", remove_results=True):
        if not self.driver:
            raise RuntimeError("driver not initialized")

        cwd = os.getcwd()

        if remove_results:
            os.system("rm -f {}/result*.zip".format(cwd))
            os.system("rm -rf {}/result".format(cwd))

        design = json.dumps(design)
        testbench = json.dumps(testbench)

        script = r"""        
        $('#testbenchLanguage').val('SystemVerilog/Verilog');
        $('#methodologyLibrary').val('701'); // UVM 1.2
        $('#otherLibrary').val('');
        $('#simulator').val('1301'); // VCS
        $('#vcsCompileOptions').val("-timescale=1ns/1ns +vcs+flush+all +warn=all -sverilog");
        $('#resultZip').click();

        var designEditor = designTabs.getActiveEditor();
        designEditor.setValue({});
                                             
        var testbenchEditor = testbenchTabs.getActiveEditor();
        testbenchEditor.setValue({});
        
        $('#runButton').click();
               
        """.format(design, testbench).strip()

        self.driver.execute_script(script)

        wait = WebDriverWait(self.driver, timeout=120, poll_frequency=0.5)

        def download_complete(driver, path="{}/result.zip".format(cwd)):
            size = 0
            last_size = -1

            while size != last_size:
                if os.path.isfile(path):
                    size = os.path.getsize(path)
                    last_size = size
                time.sleep(1)
            return True

        wait.until(download_complete, "download timed-out")

    def disconnect(self):
        if not self.driver:
            raise RuntimeError("driver not initialized")

        self.driver.quit()
