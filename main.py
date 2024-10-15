from vendcor.vendor_adapter import VendorAdapter

MOCKVENDOR = (VendorAdapter('London stock exchange', 10, 'Chancery Lane'),
              VendorAdapter('New York stock exchange', 20, 'Wall Street'))

CUSTOMERS = MOCKVENDOR


def main():
    for cust in CUSTOMERS:
        print('{} | {}'.format(cust.name, cust.address))


if __name__ == '__main__':
    main()