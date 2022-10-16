from playwright.sync_api import sync_playwright
import time
from udemyAPI import apiConfigStandard

class UdemyQuestionAnswers(apiConfigStandard):
    def __init__(self,inherit) -> None:
        self.link=inherit.link
        self.page=inherit.page
        self.language=inherit.language
        self._links=set()
        self._courseID=None
        self.unansweredQ=set()
        self.unansweredQLen=None
        self.page.goto(self.link)
        
    @property
    def getLinks(self):
        """
        This function is used to return the links that's been found.
        """
        return self._links
    @getLinks.setter
    def getLinks(self,val):
        """
        This function is used to add the links that's been found in set().
        """
        self._links.add(val)
    @property
    def courseID(self):
        return self._courseID
    @courseID.setter
    def courseID(self,val):
        self._courseID=val
    def appendLinks(self):
        self.page.locator(".question-header--row--1Noup > div:nth-child(2)").click()
        if self.language=="TR":self.getLinks=self.page.locator('button:has-text("Mesaj dizisi bağlantısını kopyala")').get_attribute("data-clipboard-text")
        elif self.language=="EN":self.getLinks=self.page.locator('button:has-text("Copy thread link")').get_attribute("data-clipboard-text")
    def filterCourse(self):
        if type(self.courseID).__name__!="int":
            self.page.close()
            raise Exception("You didn't provide an available courseID. Please make sure that your data is 'int'")
        if self.courseID<=0:
            self.page.close()
            raise Exception("You didn't provide an available courseID. Please make sure that your data is higher than 0")
        try:
            self.page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div").click(timeout=10000)
            time.sleep(0.5)
            self.page.locator(f"xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/ul/li[{self.courseID}]/button").click(timeout=10000)
            time.sleep(1)
        except:
            self.page.close()
            raise Exception("You didn't provide an available courseID")
    def noAnswerByTeacingAssistants(self,days):
        """
        This function is used to find the questions that's not been answered by any teaching assistants..
        """
        self.filterCourse()
        x=1
        errID=0
        pageID=4
        self.page.locator("label.udlite-toggle-input-container:nth-child(1) > svg:nth-child(2)").click()
        self.page.locator("label.udlite-toggle-input-container:nth-child(4) > svg:nth-child(2)").click()
        while True:
            try:
                Qhour=self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(x)}) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)").text_content(timeout=5000)
                self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(x)}) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)").click(timeout=5000)
                if "saat" in Qhour and int(Qhour.split(" ")[0])<=24 or "hour" in Qhour and int(Qhour.split(" ")[0])<=24 or "hours" in Qhour and int(Qhour.split(" ")[0])<=24:
                    self.appendLinks()
                elif "gün" in Qhour and int(Qhour.split(" ")[0])<=days or "day" in Qhour and int(Qhour.split(" ")[0])<=days or "days" in Qhour and int(Qhour.split(" ")[0])<=days:
                    self.appendLinks()
                elif "dakika" in Qhour and int(Qhour.split(" ")[0])<=60 or "minute" in Qhour and int(Qhour.split(" ")[0])<=60 or "minutes" in Qhour and int(Qhour.split(" ")[0])<=60:
                    self.appendLinks()
                else:
                    if errID>=5:
                        self.page.close()
                        break
                    errID+=1
                x+=1
            except:
                self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(pageID)}) > a:nth-child(1)").click()
                pageID+=1
                continue

    def appendLinks(self):
        self.page.locator(".question-header--row--1Noup > div:nth-child(2)").click()
        if self.language=="TR":self.getLinks=self.page.locator('button:has-text("Mesaj dizisi bağlantısını kopyala")').get_attribute("data-clipboard-text")
        elif self.language=="EN":self.getLinks=self.page.locator('button:has-text("Copy thread link")').get_attribute("data-clipboard-text")
    def unReadQuestions(self,days):
        
        """
        This function is used to find the questions that's not been read by anyone..
        """
        self.filterCourse()
        x=1
        errID=0
        pageID=4
        
        self.page.locator(".view-mode-button-group--btns--2jLrb > div:nth-child(1)").click()
        while True:
            try:
                Qhour=self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(x)}) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)").text_content(timeout=5000)
                if "saat" in Qhour and int(Qhour.split(" ")[0])<=24 or "hour" in Qhour and int(Qhour.split(" ")[0])<=24 or "hours" in Qhour and int(Qhour.split(" ")[0])<=24:
                    self.appendLinks()
                elif "gün" in Qhour and int(Qhour.split(" ")[0])<=days or "day" in Qhour and int(Qhour.split(" ")[0])<=days or "days" in Qhour and int(Qhour.split(" ")[0])<=days:
                    self.appendLinks()
                elif "dakika" in Qhour and int(Qhour.split(" ")[0])<=60 or "minute" in Qhour and int(Qhour.split(" ")[0])<=60 or "minutes" in Qhour and int(Qhour.split(" ")[0])<=60:
                    self.appendLinks()
                else:
                    if errID>=5:
                        self.page.close()
                        break
                    errID+=1
                x+=1
            except:
                self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(pageID)}) > a:nth-child(1)").click()
                pageID+=1
                continue
    def unAnsweredQuestions(self,days):
        """
        This function is used to find the questions that's not been answered by anyone..
        """
        self.filterCourse()
        x=1
        errID=0
        pageID=6
       
        self.page.locator("label.udlite-toggle-input-container:nth-child(1) > svg:nth-child(2)").click()
        self.page.locator("label.udlite-toggle-input-container:nth-child(3) > svg:nth-child(2)").click()
        while True:
            try:
                Qhour=self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(x)}) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)").text_content(timeout=5000)
                self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(x)}) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)").click(timeout=5000)
                if "saat" in Qhour and int(Qhour.split(" ")[0])<=24 or "hour" in Qhour and int(Qhour.split(" ")[0])<=24 or "hours" in Qhour and int(Qhour.split(" ")[0])<=24:
                    self.appendLinks()
                elif "gün" in Qhour and int(Qhour.split(" ")[0])<=days or "day" in Qhour and int(Qhour.split(" ")[0])<=days or "days" in Qhour and int(Qhour.split(" ")[0])<=days:
                    self.appendLinks()
                elif "dakika" in Qhour and int(Qhour.split(" ")[0])<=60 or "minute" in Qhour and int(Qhour.split(" ")[0])<=60 or "minutes" in Qhour and int(Qhour.split(" ")[0])<=60:
                    self.appendLinks()
                else:
                    if errID>=5:
                        self.page.close()
                        break
                    errID+=1
                x+=1
            except:
                self.page.locator(f"div.user-communication-card--card-container--2asrQ:nth-child({str(pageID)}) > a:nth-child(1)").click()
                pageID+=1
                continue
        