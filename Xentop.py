#! /usr/bin/python

from time import strftime
import time
import os
import sys
os.nice(-20)
class Xentop:
    
    def __init__(self, iterations, outputFile, sampling = 1):
        self.iterations = iterations
        self.sampling = sampling
        self.outputFile = outputFile
        self.machineList = []

    def getOutputFile(self):
        return self.outputFile

    def setOutputFile(self, outputFile):
        self.outputFile = outputFile

    def addMachine(self, machine):
            self.machineList.append(str(machine))

    def removeMachine(self, machine):
            self.machineList.remove(str(machine))

    def startLog(self):
            logt = file(str('xentop_log_tmp_'+ str(i) + '.txt'), 'w')


iterations = 60
for i in range (0,1):
	
	logt = file(str('xentop_log_tmp_'+ str(i) + '.txt'), 'w')

	logt.write(os.popen('xentop -i '+ str(iterations) +' -d 1 -b').read())

	logt.close()

	
	#log.write(' #NAME  STATE   CPU(sec) CPU(%)     MEM(k) MEM(%)  MAXMEM(k) MAXMEM(%) VCPUS NETS NETTX(k) NETRX(k) VBDS   VBD_OO   VBD_RD   VBD_WR SSID\n\n')

	log = file(str('xentop_log_Dom0_'+ str(i) + '.txt'), 'w')
	log.write(os.popen('cat xentop_log_tmp_'+ str(i) + '.txt | grep Domain-0').read())
	log.close()

	log1 = file(str('xentop_log_vm15_'+ str(i) + '.txt'), 'w')
	log1.write(os.popen('cat xentop_log_tmp_'+ str(i) + '.txt | grep ubu1.centro').read())
	log1.close()

	log2 = file(str('xentop_log_vm14_'+ str(i) + '.txt'), 'w')
	log2.write(os.popen('cat xentop_log_tmp_'+ str(i) + '.txt | grep ubu2.centro').read())
	log2.close()

	time.sleep(60)

