# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:14:31 2018

@author: pamde
"""
from kate_pam_employee_function import * 

dwight = Employee('dwight', 'schrute', 3, 10)
michael = Employee_management('michael', 'scott', 1, 30, 1000) 

dwight.employee_info()
print('\n')
dwight.apply_for_leave_flow()
print('\n')
michael.claim_client_expenses()