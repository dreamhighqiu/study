#-*-coding:utf-8-*-
import configparser
from .VarConfig import pageElementLocatorPath
class ParseConfigfile(object):
    def __init__(self):
        self.cf =configparser.ConfigParser()
        print(pageElementLocatorPath)
        self.cf.read(pageElementLocatorPath)

    def getItemSection(self,sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return  optionsDict
    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)

        return value
if __name__ == "__main__":
    pc = ParseConfigfile()
    print (pc.getItemSection("email"))

    print (pc.getOptionValue("email","port"))
    print(pc.getOptionValue("base_data", "fv_url"))




