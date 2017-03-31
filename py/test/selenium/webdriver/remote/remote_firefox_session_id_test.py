# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_session_id_reuse():
    """Test session ID re-use

    Create new browser object, open google.com
    with session_id create new browser object and search

    This assumes a selenium server is running on localhost
    """
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    url = 'http://localhost:4444/wd/hub'

    browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor=url
    )
    browser.get('http://google.com')

    session_id = browser.session_id

    browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor=url,
        session_id=session_id
    )

    elem = browser.find_element_by_name('q')
    elem.send_keys('python selenium webdriver')
    elem.send_keys(Keys.RETURN)
    sleep(3)
    browser.quit()

    return

