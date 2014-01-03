# 2014-01-03 ppiazi    Create - v0.1
#                        ex) python LDRA_glh2csv_dc.py

import sys # imports the sys module
import csv # imports the csv module
import getopt
import os
import datetime
import time

import LDRA_glh2csv_core

class LDRA_DynamicCoverageParser(LDRA_glh2csv_core.LDRA_GlhParser):
    def LDRA_DynamicCoverageParser(self):
        self.LDRA_glh2csv_code.LDRA_GlhParser(self)
        
    def startParse(self):
        if self.txt_file_fo == None:
            print "File Object is not ready."
            return False


if __name__ == "__main__":
    ins = LDRA_DynamicCoverageParser()
