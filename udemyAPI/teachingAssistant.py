from playwright.sync_api import sync_playwright
from udemyAPI import apiConfigTeachingAssistant
import time


class teachingAssistantReports(apiConfigTeachingAssistant):
    def __init__(self,inherit) -> None:
        self.link=inherit.link
        self.page=inherit.page
        self.language=inherit.language
        self.assistantName=inherit.assistantName
        self.unansweredQ=set()
        self.unansweredQLen=None
        self.check=False
        self.links_=set()
        self._links_=set()
        self.comment_=set()
        self.page.goto(self.link)
        
    @property
    def getLinksUnAnswered(self):
        """
        This function returns the Links that's not been answered by a spesific teaching assistant.
        """
        return self.links_
    @getLinksUnAnswered.setter
    def getLinksUnAnswered(self,val):
        """
        This function adds the links in set() format.
        """
        self.links_.add(val)
    @property
    def getLinksAnswered(self):
        """
        This function returns the Links that's been answered by a spesific teaching assistant.
        """
        return self._links_
    @getLinksAnswered.setter
    def getLinksAnswered(self,val):
        """
        This function adds the links in set() format.
        """
        self._links_.add(val)

    @property
    def commentsByTeachingAssistant(self):
        """
        This function returns the Comments that's been made by a spesific teaching assistant.
        """
        return self.comment_
    @commentsByTeachingAssistant.setter
    def commentsByTeachingAssistant(self,val):
        """
        This function adds the links in set() format.
        """
        self.comment_.add(val)

    def waitUntilOptionLoaded(self,slep):
        time.sleep(slep)
    def filterByNewest(self):
        
        self.page.locator('xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/section/div[2]').click();self.waitUntilOptionLoaded(1)
        self.page.locator('xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/section/div[2]/div/div/div/ul/li[1]/button').click();self.waitUntilOptionLoaded(1)
    def fixedQuestionsChecker(self):
        check=self.page.locator("xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[2]/div[1]/h3").text_content(timeout=3500)
        if "Bu kurstaki öne çıkan sorular" in check or "Featured questions in this course" in check:
            self.check=True
        else:
            self.check=False
    def getComments(self,val):
        if str(val)=="1":
            try:
                try:
                    return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div[3]/div").text_content(timeout=3500)
                except:
                    return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[3]/div").text_content(timeout=3500)
            except:
                return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[3]/div").text_content(timeout=3500)
        else:
            return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[3]/div").text_content(timeout=3500)
    def getNameComment(self,val):
        try:
            if str(val)=="1":
                try:
                    return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/span/a").text_content(timeout=3500)
                except:
                    return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/span/a").text_content(timeout=3500)
            else:
                return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/span/a").text_content(timeout=3500)
        except:
            if str(val)=="1":
                return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/span[1]/a").text_content(timeout=3500)
            else:
                return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/span[1]/a").text_content(timeout=3500)
    def getTime(self,val):
        if self.check==True:
            return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[3]/div[2]/div/div[{str(val)}]/div[2]/div[2]").text_content(timeout=3500)
        else:
            return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[2]/div[2]/div[1]/div[{str(val)}]/div[2]/div[2]").text_content(timeout=3500)
    def currentTime(self,val):
        if self.language=="TR":
            wholeData=self.getTime(val)
            timeNumber=wholeData.split("·")[2].split("önce")[0].split(" ")[1].strip()
            timeType=wholeData.split("·")[2].split("önce")[0].split(" ")[2].strip()
            return timeNumber+" "+timeType
        elif self.language=="EN":
            wholeData=self.getTime(val)
            timeNumber=wholeData.split("·")[2].split("ago")[0].split(" ")[1].strip()
            timeType=wholeData.split("·")[2].split("ago")[0].split(" ")[2].strip()
            return timeNumber+" "+timeType
    def checkAssistantTag(self,val):
        return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div/div[3]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/span/span").text_content(timeout=3500)
    def returnToQuestionsPage(self):
        self.page.locator("xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/a").click()
    def getLinkFromURL(self):
        return self.page.url
    def getCommentID(self,val):
        if self.check==True:
            return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[3]/div[2]/div[1]/div[{str(val)}]/div[2]/div[1]/div[2]/div[2]/a/span").text_content(timeout=3500)
        elif self.check==False:
            return self.page.locator(f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[2]/div[2]/div[1]/div[{str(val)}]/div[2]/div[1]/div[2]/div[2]/a/span").text_content(timeout=3500)
    def returnTime(self,days):
        self._time_=self.currentTime(self.x)
        self._time_=self._time_.split(" ")
        if self.language=="TR":
            if self._time_[1]=="gün":
                if days<int(self._time_[0]):
                    return 1
                else:
                    return 0
            elif self._time_[1]=="saat":
                return  0
            elif self._time_[1]=="saniye":
                return  0
            elif self._time_[1]=="dakika":
                return 0
        elif self.language=="EN":
            if self._time_[1]=="day" or self._time_[1]=="days":
                if days<int(self._time_[0]):
                    return 1
                else:
                    return 0
            elif self._time_[1]=="minute" or self._time_[1]=="minutes":
                return  0
            elif self._time_[1]=="second" or self._time_[1]=="seconds":
                return  0
            elif self._time_[1]=="hour" or self._time_[1]=="hours":
                return 0
    def searchCourseLinks(self,val):
        if self.check==True:
            
            self.xPath=f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[3]/div[2]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/h4/a"
        elif self.check==False:
            self.xPath=f"xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[2]/div[2]/div[1]/div[{str(val)}]/div[2]/div[1]/div[1]/h4/a"
        return self.xPath
    def _teachingAssistantReports_(self,days):
        """
        This function retrieves the unanswered,answered and commented questions.
        """
        self.x=1
        self.commentID=1
        self.contentID=1
        self.checkForTeachingAssistant=list()
        self.filterByNewest()
        self.answered=False
        self.fixedQuestionsChecker()
        while True:
            if type(self.returnTime(days)).__name__=="int":
                if int(self.returnTime(days))==0:
                    if self.x%4==0:
                        
                        if self.check==True:
                            self.page.locator("xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[3]/div[2]/div[2]/button").click()
                        elif self.check==False:
                            self.page.locator("xpath=/html/body/div[1]/div[1]/div/div/main/div/div[3]/div/div/section/div/div[4]/div/div/div[2]/div[2]/div[2]/button").click()
                    if int(self.getCommentID(self.x))==0:
                        self.page.locator(self.searchCourseLinks(self.x)).click()
                        self.getLinksUnAnswered=self.getLinkFromURL()
                        self.returnToQuestionsPage()
                        time.sleep(1)
                        self.x+=1
                        continue
                    
                    elif int(self.getCommentID(self.x))>=1:
                        getCommentID=int(self.getCommentID(self.x))
                        self.page.locator(self.searchCourseLinks(self.x)).click()
                        while(self.commentID<=getCommentID):
                            if self.assistantName==self.getNameComment(self.commentID):
                                if "— Öğretim Asistanı" in self.checkAssistantTag(self.commentID) or "— Teaching Assistant" in self.checkAssistantTag(self.commentID):
                                    self.answered=True
                                    self.commentsByTeachingAssistant=self.getComments(self.commentID)
                                    self.commentID+=1
                                else:
                                    self.commentID+=1
                            else:
                                self.commentID+=1
                        if self.answered==False:
                            self.getLinksUnAnswered=self.getLinkFromURL()
                        elif self.answered==True:
                            self.getLinksAnswered=self.getLinkFromURL()
                            self.answered=False
                        self.commentID=1
                        self.returnToQuestionsPage()
                        time.sleep(1)
                        self.x+=1        
                else:
                    self.page.close()
                    break
            else:
                self.page.close()
                break
                
                
            

    
    

