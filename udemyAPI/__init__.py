from playwright.sync_api import sync_playwright
class apiConfigStandard():
    def __init__(self,page,link,language) -> None:
        """
        This init function takes page,link and language as variable.
        first argument takes the playwright setup variable
        the second one takes the course link(the link in teaching assistant panel)
        the last option is the language. EN and TR supported. It's the language of your udemy panel
        ---------------------------------------------------------------------------------------------
        Note:apiConfigStandard returns;
            1)Questions that's not been read by anyone.
            2)Questions that's not been answered by anyone.
            3)Questions that's not been answered by any teaching assistant(the difference is in here it looks for every teaching assistant in the course, but in apiConfigTeachingAssistant, it looks for a spesific teaching assistant.)
        ---------------------------------------------------------------------------------------------
        """
        
        self.createWarning();self.createWarning_();self._createWarning_()      
        self.link=link
        self.page=page
        self.language=language
        if language.upper()!="TR" and language.upper()!="EN":
            raise Exception("You didn't provide an available language. Currently, available languages are: TR and EN")
        else:
            self.language=language
    def __help__(self):
        """
        You can check the github page for a detailed usage of this API
        """
    def createWarning(self):
        print("This API is Unofficial and created by Aziz Kaplan")
    def createWarning_(self):
        print("Github:https://github.com/AzizKpln")
    def _createWarning_(self):
        print("Linkedin:https://www.linkedin.com/in/aziz-k-074604170/")

class apiConfigTeachingAssistant():
    def __init__(self,page,link,language,assistantName) -> None:
        """
        This init function takes page,link,language and teaching assistant name as variable.
        first argument takes the playwright setup variable
        the second one takes the course link(the link in student panel)
        the third option is the language. EN and TR supported. It's the language of your udemy panel
        the last option takes the teaching assistant name.
        ---------------------------------------------------------------------------------------------
        Note:apiConfigTeachingAssistant returns;
            1)Links of questions that's answered by a spesific teaching assistant in a spesific time.
            2)Links of questions that's unanswered by a spesific teaching assistant in a spesific time.
            3)Comments that's been made by a spesific teaching assistant in a spesific time.
        ---------------------------------------------------------------------------------------------
        """
        self.createWarning();self.createWarning_();self._createWarning_()      
        self.link=link
        self.page=page
        self.language=language
        self.assistantName=assistantName
        if language.upper()!="TR" and language.upper()!="EN":
            raise Exception("You didn't provide an available language. Currently, available languages are: TR and EN")
        else:
            self.language=language
    def createWarning(self):
        print("This API is Unofficial and created by Aziz Kaplan")
    def createWarning_(self):
        print("Github:https://github.com/AzizKpln")
    def _createWarning_(self):
        print("Linkedin:https://www.linkedin.com/in/aziz-k-074604170/")