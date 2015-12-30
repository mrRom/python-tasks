import sys
import re
import subprocess

def is_running(name):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(name, x):
            return True
    return False

def process_file(arg_list):
    cr_list = []
    er_list = []
    warn_list = []
    inf_list = []
    deb_list = []

    def process_single_file(fpath):
        f_cr_list = []
        f_er_list = []
        f_warn_list = []
        f_inf_list = []
        f_deb_list = []
        with open(fpath, 'r') as ffile:
            for line in ffile.readlines():
                if line.startswith("CRITICAL"):
                    f_cr_list.append(line.split(" - "))
                elif line.startswith("ERROR"):
                    f_er_list.append(line.split(" - "))
                elif line.startswith("WARNING"):
                    f_warn_list.append(line.split(" - "))
                elif line.startswith("INFO"):
                    f_inf_list.append(line.split(" - "))
                elif line.startswith("DEBUG"):
                    f_deb_list.append(line.split(" - "))
        """printing count of logs by level"""
        print "File name: " + fpath
        print "CRITICAL: " + str(len(f_cr_list))
        print "ERROR: " + str(len(f_er_list))
        print "WARN: " + str(len(f_warn_list))
        print "INFO: " + str(len(f_inf_list))
        print "DEBUG: " + str(len(f_deb_list))
        print "========================"
        cr_list.extend(f_cr_list)
        er_list.extend(f_er_list)
        warn_list.extend(f_warn_list)
        inf_list.extend(f_inf_list)
        deb_list.extend(f_deb_list)

    for fpath in arg_list:
        process_single_file(fpath)
    """printing count of logs in all files by level"""
    print "All files:"
    print "CRITICAL: " + str(len(cr_list))
    print "ERROR: " + str(len(er_list))
    print "WARN: " + str(len(warn_list))
    print "INFO: " + str(len(inf_list))
    print "DEBUG: " + str(len(deb_list))
    print "========================"

    """Iterating through the created lists in order, sorting processes by quantity of messages and adding 
        new component_name to the list_of_component_names if component_name doesn't exist in the list_of_component_names"""
    list_of_component_names = []
    def verify_processes(lev_list):
        "count_dict - is a dict with COMPONENT_NAME as a key and quantity of logs of appropriate level as a value"
        count_dict = {}
        for l in lev_list:
            if l[2] in count_dict.keys():
                count_dict[l[2]] = count_dict[l[2]] + 1
            else:
                count_dict[l[2]] = 1
        list_of_tuples = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
        for l in list_of_tuples:
            if l[0] in list_of_component_names:
                continue
            else:
                list_of_component_names.append(l[0])

    #Adding processes to the list by log level importance
    verify_processes(cr_list)
    verify_processes(er_list)
    verify_processes(warn_list)
    verify_processes(inf_list)
    verify_processes(deb_list)
    
    #printing COMPONENT_NAME of logs in the file
    print "Component Names, sorted by importance of messages:"
    for l in list_of_component_names:
        print l
    print "========================"

    """Adding + or - beside COMPONENT_NAME if process's still running"""
    print "Running or not:"
    result_list = []
    for l in list_of_component_names:
        if is_running(l):
            result_list.append(l + "   +")
        else:
            result_list.append(l + "   -")
     
    for i in result_list:
        print i

if __name__ == '__main__':
    #arg_list = ["1.txt", "2.txt", "3.txt"]
    arg_list = sys.argv[1::]
    print arg_list
    process_file(arg_list)
