import sys # imports the sys module
import csv # imports the csv module
import getopt
import os

TBGLHAPI_FLAG_CODE_COVERAGE = 4096
TBGLHAPI_FLAG_CODE_REVIEW_MODEL_SELECTED_DURING_ANALYSIS = 2
TBGLHAPI_FLAG_CODE_REVIEW_SPECIFIC_MODEL = 4

class LDRA_GlhParser:
    glh_file_name = None
    TBglhapi_path = "C:\LDRA_Toolsuite\TBglhapi.exe"
    txt_file_fo = None
    
    def LDRA_GlhParser(self):
        pass
    
    def LDRA_GlhParser(self, glh_file_name_in, TBglhapi_path_in):
        self.LDRA_GlhParser(self)
        self.glh_file_name = glh_file_name_in
        self.TBglhapi_path = TBglhapi_path_in
        
    def setGlhFileName(self, glh_file_name_in):
        self.glh_file_name = glh_file_name_in
        
    def setTBglhapiPath(self, TBglhapi_path_in):
        self.TBglhapi_path = TBglhapi_path_in        
    
    def analyzeGlh(self, TBglhapi_path, target_file, flags=TBGLHAPI_FLAG_CODE_REVIEW_MODEL_SELECTED_DURING_ANALYSIS):
        if os.path.exists(TBglhapi_path) != True:
            print " TBglhapi.exe(%s) doesn't exist." % (TBglhapi_path)
            return False

        if os.path.exists(target_file) != True:
            print " GLH(%s) doesn't exist." % (target_file)
            return False

        TBglhapi_cmd = "%s result=%s flags=%d"
        os.system(TBglhapi_cmd % (TBglhapi_path, target_file, flags) )
        
        return True

    def loadTextFile(self):
        self.loadTextFile(self, self.glh_file_name)        
                        
    def loadTextFile(self, target_file):
        target_txt_file = target_file.replace(".glh", ".txt")
    
        try:
            self.txt_file_fo = open(target_txt_file, "r")
            self.target_name = target_txt_file.rstrip(".txt")
            return True
        except:
            print " Check whether %s exists." % (target_file)
            return False
