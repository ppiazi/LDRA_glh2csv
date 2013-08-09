# 2013-08-07
# Soy
# python LDRA_glh2csv.py Calendar.txt

import sys # imports the sys module
import csv # imports the csv module
import datetime
import time

PATTERN_FILE_NAME = "      File: "
PATTERN_LDRA_RULE_NUMBER = "LDRA Rule Number:"
PATTERN_RULE_DESCRIPTION = "Rule Description:"
PATTERN_SRC_LINE_NUMBER = "Source Line Number:"

def set_globvar(prefix):
    global g_prefix_file_name
    g_prefix_file_name = prefix


def loadFile(target_file):
    global g_prefix_file_name
    fo = open(target_file, "r")
    set_globvar(target_file.rstrip(".txt"))
    startParse(fo)
    fo.close()


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
    

if __name__ == "__main__":
    print "Script for LDRA"
    if len(sys.argv) != 2:
        print "Hahaha"
    else:
        loadFile(sys.argv[1])
    print "Bye"
    
