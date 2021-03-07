#!/usr/bin/env python3

# This scripts sets the status of a given Sale Order.

__author__ = "Isaac Benitez"
__contact__ = "ibe@odoo.com"
__copyright__ = "Copyright 2021"
__date__ = "03/06/2021"
__version__ = "0.0.1"

import xmlrpc.client
import sys

# Odoo API
URL = ''
DB = ''
ODOO_USR = ''
ODOO_PWD = ''

def main():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
    uid = common.authenticate(DB, ODOO_USR, ODOO_PWD, {})

    po_name = sys.argv

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
    pos = models.execute_kw(DB, uid, ODOO_PWD, 'purchase.order', 'search_read', 
                            [[["name", "=", po_name]]],
                            {'fields': ['user_id', 'name', 'partner_id', 
                            'date_approve', 'state', 'amount_total', 'origin',
                            ]})

    for po in pos:
        print("id:\t\t", po['id'])
        print("name:\t\t", po['name'])
        print("salesrep:\t", po['user_id'][1])
        print("date:\t\t", po['date_approve'])
        print("total:\t\t", po['amount_total'])
        print("customer:\t", po['partner_id'][1])
        print("state:\t\t", po['state'])
        print("origin:\t\t", po['origin'])

if __name__ == '__main__':
    main()
