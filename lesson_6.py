#!/usr/bin/env python

import time

from grove.display.jhd1802 import JHD1802

def main():
    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    lcd.clear()

    lcd.setCursor(0, 0)
    lcd.write(' hello, world!!!')
    lcd.setCursor(1, 0)
    lcd.write('KARTIK')


    print('application exiting...')

if __name__ == '__main__':
    main()