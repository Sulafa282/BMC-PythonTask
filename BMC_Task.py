#Sulafa Abu Saleh
#interview - python task


import threading
import sys
from ftplib import FTP

#get the input from command line arguments
inputList=sys.argv


pairsList=inputList[1]

#the pairs are split by comma and space
pairsAsaString=pairsList.split(', ')

#the host and the dirctory are split by |
pairs=[i.split('|') for i in pairsAsaString ]


#function that makes connection with the host and prints the directory's content, using FTP library
def connectingToHost(hostName,directory,threadID):
    ftp = FTP(hostName)

    ftp.login()

    #changing directory
    ftp.cwd(directory)

    for i in ftp.nlst():
        print("SUB FOLDER OR FILE NAME: {}, HOST NAME: {}, DIRECTORY NAME: {}, THREADID: {}".format(i,hostName,directory,threadID))
        print('\n')

    ftp.quit()



if __name__ == "__main__":
    numThreads = len(pairs)   # Number of threads to create

    #the jobs list
    jobs = []

    #for each pair, produce new thread and make them work in parallel (multi-threading)
    for i in range(0, numThreads):
        #produce a new thread, the thread job is the function "connectingToHost"
        thread = threading.Thread(target=lambda: connectingToHost(pairs[i][0], pairs[i][1], threading.get_ident()))
        # Start the thread
        thread.start()
        #add the thread to jobs list
        jobs.append(thread)


    #Ensure all of the threads have finished
    for j in jobs:
        j.join()

# example to input: "opensuse.osuosl.org|pub, debian.osuosl.org|debian, opensuse.osuosl.org|debian/pool"
