# 2013-08-07 Soy    Create - v0.1
#                    ex) python LDRA_glh2csv.py Calendar.txt
# 2013-08-09 ppiazi Modified - v0.3
#                   - Get argument with -i and -e option
#                    ex) python LDRA_glh2csv.py -i Calendar.glh
# 2013-11-20 ppiazi Modified - v0.4
#                   - Save a csv file where LDRA_glh2csv.py is located

import sys # imports the sys module
import csv # imports the csv module
import getopt
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

def analyzeGlh(TBglhapi_path, target_file):
    if os.path.exists(TBglhapi_path) != True:
        print " TBglhapi.exe(%s) doesn't exist." % (TBglhapi_path)
        return False

    if os.path.exists(target_file) != True:
        print " GLH(%s) doesn't exist." % (target_file)
        return False

    TBglhapi_cmd = "%s result=%s flags=2"
    os.system(TBglhapi_cmd % (TBglhapi_path, target_file) )
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
    
    s = os.path.split(g_prefix_file_name)
        
    CSV_FILE_NAME = s[1] + '_' + str(loadtime) + '.csv'
    print a, CSV_FILE_NAME
    outputfile = open(CSV_FILE_NAME, "w")
    
    writer = csv.writer(outputfile, dialect='excel', lineterminator='\n')
    for index in xrange(0, len(csv_list), 1):
        writer.writerow(csv_list[index])
        
    outputfile.flush()   
    outputfile.close()
    
def printUsage():
    print " LDRA_glh2csv.exe -i <Glh filename> -e <Location of TBglhapi.exe>"
    print "   ex) LDRA_glh2csv.exe -i test.glh"
    print "   ex) LDRA_glh2csv.exe -i test.glh -e C:\LDRA_Toolsuite\TBglhapi.exe"

if __name__ == "__main__":
    print "LDRA_glh2csv v0.4"

    if len(sys.argv) == 1:
        printUsage()
        sys.exit(-1)

    TBglhapi_path = "C:\LDRA_Toolsuite\TBglhapi.exe"
    glh_file = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:e:")
    except getopt.GetoptError:
        printUsage()
        sys.exit(-1)

    for opt, arg in opts:
        #print opt + "  " + arg
        if opt == '-h':
            printUsage()
            sys.exit(-1)
        elif opt in "-i":
            glh_file = arg
        elif opt in "-e":
            TBglhapi_path = arg

    if ( glh_file == "" ):
        printUsage()
        sys.exit(-1)

    print "Target GLH FILE : %s" % (glh_file)
    print "TBglhapi PATH   : %s" % (TBglhapi_path)
    
    print "1. Ivoking TBglhapi.exe..."
    ret = analyzeGlh(TBglhapi_path, glh_file)
    if ret == False:
        sys.exit(-1)

    print "\n2. Making CSV file..."
    ret = loadFile(glh_file)

    if ret == True:
        print " Done!"
    else:
        print " >.<"
    
