# 2013-08-07 Soy    Create - v0.1
#                    ex) python LDRA_glh2csv.py Calendar.txt
# 2013-08-09 ppiazi Modified - v0.2
#                    ex) python LDRA_glh2csv.py Calendar.glh

import sys # imports the sys module
import csv # imports the csv module
import os
import datetime
import time

PATTERN_FILE_NAME = "      File: "
PATTERN_LDRA_RULE_NUMBER = "LDRA Rule Number:"
PATTERN_RULE_DESCRIPTION = "Rule Description:"
PATTERN_SRC_LINE_NUMBER = "Source Line Number:"

def set_globvar(prefix):
    global g_prefix_file_name
    g_prefix_file_name = prefix

def analyzeGlh(target_file):
    if os.path.exists(target_file) != True:
        print " %s doesn't exist." % (target_file)
        return False

    TBglhapi_cmd = "C:\LDRA_Toolsuite\TBglhapi.exe result=%s flags=2"
    os.system(TBglhapi_cmd % (target_file) )
    return True

def loadFile(target_file):
    global g_prefix_file_name
    target_txt_file = target_file.replace(".glh", ".txt")
    try:
        fo = open(target_txt_file, "r")
        set_globvar(target_txt_file.rstrip(".txt"))
        startParse(fo)
        fo.close()
        return True
    except:
        print " Check whether %s exists." % (target_file)
        return False
 

def startParse(fo):
    result_list = ["LDRA Rule Number", "Rule Description", "File", "Source Line Number"]
 
    for line in fo.readlines():
        if PATTERN_FILE_NAME in line:
            column1 = line.lstrip("      File: ").replace("\n", "")
        if PATTERN_LDRA_RULE_NUMBER in line:
            column2 = line.lstrip("LDRA Rule Number:        ").replace("\n", "")
        if PATTERN_RULE_DESCRIPTION in line:
            column3 = line.lstrip("Rule Description:        ").replace("\n", "")
        if PATTERN_SRC_LINE_NUMBER in line:
            column4 = line.lstrip("Source Line Number:      ").replace("\n", "")
            dict = {'column1': column1, 'column2': column2, 'column3': column3, 'column4': column4}
            new = [column2, column3, column1, column4]
            result_list.extend(new)
     
    csv_list = [result_list[index:index+4] for index in xrange(0, len(result_list), 4)]
    writeFile(csv_list)

            
def writeFile(csv_list):
    a = datetime.datetime.now()
    loadtime = int(time.time())
    CSV_FILE_NAME = g_prefix_file_name + '_' + str(loadtime) + '.csv'
    print a, CSV_FILE_NAME
    outputfile = open(CSV_FILE_NAME, "w")
    
    writer = csv.writer(outputfile, dialect='excel', lineterminator='\n')
    for index in xrange(0, len(csv_list), 1):
        writer.writerow(csv_list[index])
        
    outputfile.flush()   
    outputfile.close()
    
def printUsage():
    print " LDRA_glh2csv.exe [glh file name]"
    print "   ex) LDRA_glh2csv.exe test.glh"

if __name__ == "__main__":
    print "LDRA_glh2csv v0.2"
    if len(sys.argv) != 2:
        printUsage()
    else:
        print "1. Ivoking TBglhapi.exe..."
        ret = analyzeGlh(sys.argv[1])
        if ret == False:
            sys.exit(-1)

        print "\n2. Making CSV file..."
        ret = loadFile(sys.argv[1])

        if ret == True:
            print " Done!"
        else:
            print " >.<"
    
