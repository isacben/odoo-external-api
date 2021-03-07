#!/usr/bin/env python3

# This scripts sets the status of a given Sale Order.

__author__ = "Isaac Benitez"
__contact__ = "ibe@odoo.com"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"

import sys
import xmlrpc.client

# Odoo API
URL = ''
DB = ''
ODOO_USR = ''
ODOO_PWD = ''

def main():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
    uid = common.authenticate(DB, ODOO_USR, ODOO_PWD, {})

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
    
    # type the name of the SO, for example, SO2021/1337704
    orders = models.execute_kw(DB, uid, ODOO_PWD, 'sale.order', 'search_read', 
                            [[["name", "=", "SO2021/1337704"],
                            ]],
                            {'fields': ['id', 'state'],
                            'limit': 1})
    
    print("Before:", orders)

    # update sales order status (WARNING: this will update the status of the SO)
    # type the status, for example, sent
    models.execute_kw(DB, uid, ODOO_PWD, 'sale.order', 'write', [orders[0]['id'], {
        'state': 'sent'
    }])

    print("After: ", orders)

if __name__ == '__main__':
    main()
