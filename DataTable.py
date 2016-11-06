
# Copyright 2015, Majestic-12 Ltd trading as Majestic
# https://majestic.com
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
# 
#     * Neither the name of Majestic-12 Ltd, its trademarks, nor any contributors
#       to the software may be used to endorse or promote products derived from
#       this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Majestic-12 Ltd BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re

class DataTable:
    
    """ This constructs a new instance of the DataTable module. """
    def __init__(self):
        self.name = ''
        self.headers = []
        self.params = {}
        self.rows = []
       
    """ Set table's name """
    def set_table_name(self, name):
        self.name = name
     
    """ Set table's headers """
    def set_table_headers(self, headers):
        self.headers = self.__split(headers)
        
    """ Set table's parameters """
    def set_table_params(self, name, value):
        self.params[name] = value
        
    """ Set table's rows """
    def set_table_row(self, row):
        rows_hash = {}
        elements = self.__split(row) 
        for index, element in enumerate(elements):
            if(element == ' '):
                element = ''       
            rows_hash[self.headers[index]] = element;
        self.rows.append(rows_hash)
    
    # Splits the input from pipe separated form into an array.
    def __split(self, value):
        regex = re.compile('(?<!\|)\|(?!\|)')
        array = regex.split(value)
        for index, item in enumerate(array):
            array[index] = item.replace('||', '|')
        return array
    
    """ Returns a table's parameter for a given name """
    def get_param_for_name(self, name):
        if(name in self.params):
            return self.params[name]
        return None
    
    """ Returns the number of rows in the table """
    def get_row_count(self):
        return len(self.rows)