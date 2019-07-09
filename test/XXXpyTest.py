﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file XXXpyTest.py
 @brief ModuleDescription
 @date $Date$


"""
from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import OpenRTM_aist
import RTC

import MyService_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from MyService_idl_example import *

import XXXpy

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
xxxpytest_spec = ["implementation_id", "XXXpyTest", 
		 "type_name",         "XXXpyTest", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class XXXpyTest
# @brief ModuleDescription
# 
# 
class XXXpyTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._outIn = OpenRTM_aist.InPort("out", self._d_out)
		self._d_in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._inOut = OpenRTM_aist.OutPort("in", self._d_in)

		"""
		"""
		self._MyServidePort = OpenRTM_aist.CorbaPort("MyServide")

		

		"""
		"""
		self._myservice0 = OpenRTM_aist.CorbaConsumer(interfaceType=SimpleService.MyService)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("out",self._outIn)
		
		# Set OutPort buffers
		self.addOutPort("in",self._inOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		self._MyServidePort.registerConsumer("myservice0", "SimpleService::MyService", self._myservice0)
		
		# Set CORBA Service Ports
		self.addPort(self._MyServidePort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK

	def runTest(self):
		return False
	

def RunTest():
	manager = OpenRTM_aist.Manager.instance()
	comp = manager.getComponent("XXXpyTest0")
	if comp is None:
		print('Component get failed.', file=sys.stderr)
	return comp.runTest()


def XXXpyTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=xxxpytest_spec)
    manager.registerFactory(profile,
                            XXXpyTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    XXXpyTestInit(manager)
    XXXpy.XXXpyInit(manager)

    # Create a component
    comp = manager.createComponent("XXXpyTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager(True)

	ret = RunTest()
	mgr.shutdown()

	if ret:
		sys.exit(0)
	else:
		sys.exit(1)

if __name__ == "__main__":
	main()

