# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:15:17 2019

@author: cidmedeiros
"""
import datetime as dt

class Date:
    def __init__(self, year, month, day):      
        self.year = year
        self.month = month
        self.day = day
        
    def std_same_month(self, end=False):
        
        """
        Standardize a given date at the first or last day of date's month,
        unless end is set to True.
        
        Parameters:
        date (datetime): date to be stadandized
        end (boolean):
            If True returns the date stadandized at the last day of the month.
            The ending day is 28 for February and 30 for the rest of the months.
            If False (default) returns the date stadandized at the first day of the month.
        
        Returns:
        datetime: returning date stadandized
        """
        ans = None
        if end == False:
            ans = dt.datetime(self.year, self.month, 1)
        else:
            if self.month != 2:
                ans = dt.datetime(self.year, self.month, 30)
            else:
                ans = dt.datetime(self.year, self.month, 28)
                
        return ans
    
    def sum_one_month(self, end=False):
        
        """
        Return the next month of the informed date.
        Standardize the answer at the first day of date, unless end is set to True.
        
        Parameters:
        date (datetime): date to be added to and stadandized
        end (boolean):
            If True returns the date stadandized at the last day of the month.
            The ending day is 28 for February and 30 for the rest of the months.
            If False (default) returns the date stadandized at the first day of the month;
        
        Returns:
        datetime: returning date stadandized
        """
        ans = None
        
        if end == False:
            if self.month != 12:
                ans = dt.datetime(self.year,((self.month)+1),1)
            else:
                ans = dt.datetime((self.year+1), 1, 1)
        else:
            if self.month != 12:
                if self.month != 1:
                    ans = dt.datetime(self.year, (self.month+1), 30)
                else:
                    ans = dt.datetime(self.year, (self.month+1), 28)
            else:
                ans = dt.datetime((self.year+1), 1, 30)
                
        return ans
    
    def sub_one_month(self, end=False):
        
        """
        Return the previous month of the informed date.
        Standardize the answer at the first day of date, unless end is set to True.
        	Parameters:
        	date (datetime): date to be subtracted from and stadandized
                end (boolean):
                    If True returns the date stadandized at the last day of the month.
                    The ending day is 28 for February and 30 for the rest of the months.
                    If False (default) returns the date stadandized at the first day of the month;
                
            Returns:
            datetime: returning date stadandized  
        """
        
        ans = None
        if end == False:
            if self.month != 1:
                ans = dt.datetime(self.year,((self.month)-1),1)
            else:
                ans = dt.datetime((self.year-1), 12, 1)
        else:
            if self.month != 1:
                if self.month != 3:
                    ans = dt.datetime(self.year, (self.month-1), 30)
                else:
                    ans = dt.datetime(self.year, (self.month-1), 28)
            else:
                ans = dt.datetime((self.year-1), 12, 30)
                
        return ans

    def add_years(self, years):
        
        """
        Return a date that's "years" years after the informed date. Return the
        same calendar date (month and day) in the destination year, if it exists,
        otherwise use the following day (thus changing February 29 to March 1).
        """ 
        try:
            return self.replace(year = self.year + years)
        except ValueError:
            return self + (dt.date(self.year + years, 1, 1) - dt.date(self.year, 1, 1))
        
 
    
        
        
        
        
        
