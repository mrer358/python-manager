#!/usr/bin/python
import subprocess
import os
import time

def manager():
    a=raw_input('1).to see all users\n2).to see the all groups\n3).reset the password\n4).create a new user\n5).create new group and add users to groups\n6).list all mounts\n7).mount a folder\n8.) Add new commands to .profile of a certain user\n9).Exit:\t''\n')
    if a == '1':
        subprocess.call(['getent','passwd'])
        print '#####################################################################'
        go = raw_input('insert the user you want to see more info on hem:\t\n')
        os.system("clear")
        print '#####################################################################'
        manu = raw_input('1).show user groups\n2).show user id\n3).show user aliases\n4).add new alias\n5).change password\n6).back\n')
        os.system("clear")
        if manu == '1':
           yo = os.system("getent group"  "\t" "|grep" "\t" + go + "")
           print '####################################################'
           print'this is the groups number', (yo)

        elif manu == "2":
            subprocess.call('id')
        elif manu == "3":
            os.system("cat" "\t" "/root/.bashrc""")
        elif manu == "4":
            alias=raw_input("type new commend for the user")
            os.popen('alias' '\t' + alias + '')
            print "the command add to the alias"
        else: manager()


    elif a == '2':
        subprocess.call(['getent','group'])
        print '##############################################################'
        manuu=raw_input("what the user you want to see is group or in groups")
        os.system('id' '\t' + manuu+ "")
    elif a == '3':
        passwd2 = raw_input('insert the user you want to reset the password')
        os.popen('passwd' "\t" + passwd2 + "")

    elif a == '4':
        print "###############################################"
        print "#lock you have too options if you are chose 1 #"
        print "#create a user with noting only user!!!       #"
        print "#=============================================#"
        print "#and if you chose 2 your going to create user #"
        print "#and group plus home dirctory plus a password #"
        print "###############################################"
        users=raw_input("1.mated useradd\n2.adduser")
        os.system("clear")
        if users == '1':
            usee=raw_input('name')
            os.popen('useradd' "\t"  + usee + "")

        elif users == '2':
            gi=raw_input("insert the name of the user you want to create")
            os.popen('adduser' "\t"  + gi + "")
        else:
            print "bad way"
    elif a == '5':
        grouppnew=raw_input("1).to create a new  group\n2.to add user to group\n")
        if grouppnew == '1':
            hhgroup=raw_input('put the name of the group you  want to create:\t')
            os.popen('groupadd' '\t' + hhgroup + '')
        elif grouppnew == '2':
            infogrouup=raw_input('what the of the group you want to add:\t')
            infouser=raw_input('tpye name you want to add to the group:\t')
            os.popen('usermod' '\t' '-a' '\t' '-G' '\t' + infogrouup + '\t' + infouser + '')



    elif a == '6':
        subprocess.call(['mount'])
    elif a == "7":
        print "#################################################"
        print "# remember to check you hard disks with         #"
        print "# fdisk  to see the new                         #"
        print "# disks in the system ^_^ look on the device    #"
        print "# remember the device to use that in the future #"
        print "#                                               #"
        print "#################################################"
        print ''
        manuuu=raw_input("1.to use fdisk\n2.monut a folder")
        if manuuu == '1':
                subprocess.call(['fdisk','-l'])
        elif manuuu == '2':
            mountt=raw_input("plaese insert  dirctory of the device:\t")
            mounttt=raw_input("plaese insert the dirctory for mount to the folder:\t")
            os.popen('mount' '\t' + mountt + '\t' + mounttt + '')
            print'#######################################################'
            print  "you have mount you device to a dirctory in a folder"

    elif a == '8':
            addProfile = raw_input('what is the user you want to add a command?:\t')
            #os.system("cat" '\t' ".profile")
            #os.system('su' '\t' + addProfile + '')
            #os.system("cat" '\t' ".profile")
            #print '########################################################################################'
            #print '########################################################################################'
            #print '########################################################################################'
            os.system("nano" '\t' "/root/.bashrc")






    elif a == '9':
exit()
