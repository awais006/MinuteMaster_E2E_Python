from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[id='email']")

        self.create_newbookcase_btn = "//button[text()='Create New Bookcase']"
        self.enter_bookcasename_popup_textbox = "//input[@id='bookcaseName']"
        self.create_bookcasename_popup_btn = "//div[contains(@class, 'MuiDialog-container')]//button[text()='Create New Bookcase']"
        self.success_alert = "//div[@role='alert' and contains(text(), 'Bookcase added successfully')]"
        self.bookcase_alreadyexists_alert = "//div[@role='alert' and contains(text(), 'Bookcase name already exists')]"
        self.addashelf_btn = "//button[text()='Add a Shelf']"
        self.enter_shelfname_popup_textbox = "//input[@id='shelfName']"
        self.create_bookshelf_popup_confirm_btn = "//div[@role='presentation']//button[text()='Confirm']"
        self.create_newagenda_link = "//p[text()='Create new agenda']//ancestor::a"
        self.agenda_title_textbox = "//input[@placeholder='Title']"
        self.agenda_meeting_link_textbox = "//input[@placeholder='MEETING LINK']"
        self.add_standard_agendaitems_btn = "//button[text()='Add Standard Agenda Items']"
        self.searchstandardwordingitems_dropdown = "//label[text()='Search Standard Wording Items']//parent::div"
        self.select_appointmentofchair_option = "//ul[@role='listbox']//li[text()='Appointment of Chair']"
        self.add_standard_agendaitem_popup_btn = "//div[contains(@class, 'MuiDialog-container')]//button[text()='Add Standard Agenda Items']"
        self.remove_first_empty_agenda_item = "//*[local-name()='svg' and @data-sentry-element='DeleteIcon']"
        self.publish_btn = "//button[text()='Publish']"
        self.popup_publish_btn = "//div[contains(@role, 'presentation')]//button[text()='Publish']"
        self.downloadpdf_btn = "//button[text()='Download PDF']"
        self.producemeetingminutes_btn = "//button[text()='Produce Meeting Minutes']"
        self.next_btn = "//button[text()='Next']"
        self.produceminutesdraftfromtranscript = "//span[text()='Produce Minutes Draft from Transcript (Quickest)']//parent::div"
        self.select_inputtype_btn = "//div[contains(@class, 'popup-container')]//button[text()='File']"
        self.file_type = "//input[@type='file' and contains(@accept,'.docx')]"
        self.selectcardtpe_btn = "//p[text()='Card Layout']//parent::div"
        self.saved_btn = "//div[text()='Saved']"

    def CreateNewTranscript(self, bookcasename: str, bookshelfname: str, agenda_title: str):
        self.page.locator(self.create_newbookcase_btn).click()
        self.page.locator(self.enter_bookcasename_popup_textbox).fill(bookcasename)
        self.page.locator(self.create_bookcasename_popup_btn).click()

        expect(self.page.locator(self.success_alert)).to_be_visible()

        self.page.locator(self.addashelf_btn).click()
        self.page.locator(self.enter_shelfname_popup_textbox).fill(bookshelfname)
        self.page.locator(self.create_bookshelf_popup_confirm_btn).click()

        self.page.locator(self.create_newagenda_link).click()
        self.page.locator(self.agenda_title_textbox).fill(agenda_title)
        self.page.locator(self.agenda_meeting_link_textbox).click()
        self.page.locator(self.remove_first_empty_agenda_item).click()
        self.page.locator(self.add_standard_agendaitems_btn).click()
        self.page.locator(self.searchstandardwordingitems_dropdown).click()
        self.page.locator(self.select_appointmentofchair_option).click()
        self.page.locator(self.add_standard_agendaitem_popup_btn).click()
        self.page.locator(self.publish_btn).click()
        self.page.locator(self.popup_publish_btn).click()

        downloadpdf_btn_elem = self.page.locator(self.downloadpdf_btn)
        downloadpdf_btn_elem.wait_for(timeout=360000)

        self.page.locator(self.producemeetingminutes_btn).click()
        self.page.locator(self.next_btn).click()
        self.page.locator(self.produceminutesdraftfromtranscript).click()

        #upload file
        file_input = self.page.locator(self.file_type)
        file_input.set_input_files("../testdata/Awais Transcript.docx")

        self.page.locator(self.selectcardtpe_btn).click()

        save_btn_elem = self.page.locator(self.saved_btn)
        save_btn_elem.wait_for(timeout=360000)

        expect(self.page.locator(self.saved_btn)).to_be_visible()