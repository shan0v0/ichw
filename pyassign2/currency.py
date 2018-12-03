#!/usr/bin/env python
# coding: utf-8

# In[51]:


#!/usr/bin/env python3

"""currency.py: 
Currency exchange: provides several string parsing functions 
to implement a simple currency exchange routine using an online currency service.

__author__ = "Shanye"
__pkuid__  = "1800011804"
__email__  = "shan26_0v0@126.com"
"""

from urllib.request import urlopen

def exchange(currency_from,currency_to,amount_from):
    """Set up a function to change (amount_from) money in currency on hand (currency_from) 
    to the needed currency (currency_to) by using an online currency service. 
    The value returned represents the amount in currency currency_to."""
    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('true','True')
    jstr = eval(jstr)
    return jstr["to"]

def test_exchange():
    """Test if the exchanging rate is changed by judging 
    whether the exchange("USD","EUR",2.5) is equal to the nowing exchange."""
    result = "2.1589225 Euros"
    assert(exchange("USD","EUR",2.5) == result)

def main():
    """Implement a simple currency exchange routine using an online currency service and test if the exchanging rate is changed."""
    test_exchange()
    print("2.1589225 Euros")
    
if __name__ == '__main__':
    main()
    

