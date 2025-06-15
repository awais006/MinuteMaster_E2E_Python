from datetime import datetime

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_create_new_transcript(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("awaism826@gmail.com", "Nothing-11")

    current_url = login_page.get_current_url()
    assert current_url == "https://staging.minute-master.com/bookcase"

    home_page = HomePage(page)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    bookcasename = f"bookcase_{timestamp}"
    bookshelfname= f"bookshelf_{timestamp}"
    agendatitlename = f"agendatitle_{timestamp}"

    home_page.CreateNewTranscript(bookcasename, bookshelfname, agendatitlename)