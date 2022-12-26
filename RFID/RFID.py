import mfrc5222
from os import uname
import time


def text_to_bytes(text):
    data_chunk = text[0:16]
    data_byte_array = [ord(x) for x in list(data_chunk)]
    while len(data_byte_array) < 16:
        data_byte_array.append(0)
    return data_byte_array

def read_card():

    
    #print("Initialising Module=> " + str(uname()[0]))

    rdr = mfrc5222.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    print("-------------------------------")
    print("Zbliż karte do cztynika.......")
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")

    try:
        while True:

            (stat, tag_type) = rdr.request(rdr.REQIDL)

            if stat == rdr.OK:

                (stat, raw_uid) = rdr.anticoll()

                if stat == rdr.OK:
                    print("Karta wykryta!")
                    #print(" -  TAG TYPE : 0x%02x" % tag_type)
                    #print(" -  UID      : 0x%02x%02x%02x%02x" %
                      #  (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")

                    if rdr.select_tag(raw_uid) == rdr.OK:

                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            data = rdr.read(8)
                            datastr = ""
                            hexstr = []
                            for i in data:
                                datastr = datastr + (chr(i))
                                hexstr.append(hex(i))
                            print("DATA: " + str(datastr))
                            #print("RAW DATA: " + str(hexstr))
                            #print("Data" + str(data))
                            rdr.stop_crypto1()
                            return str(datastr)
                            time.sleep(5)
                        else:
                            print("AUTH ERR")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("EXITING PROGRAM")

def write_to_card(text):

    print("Init. " + str(uname()[0]))

    rdr = mfrc5222.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    print("")
    print("Zbliż kartę do czytnika.......adres zapisu: 0x08")
    print("")

    try:
        while True:

            (stat, tag_type) = rdr.request(rdr.REQIDL)

            if stat == rdr.OK:

                (stat, raw_uid) = rdr.anticoll()

                if stat == rdr.OK:
                    print("Karta wykryta!!!!")
                    #print(" -  TAG TYPE : 0x%02x" % tag_type)
                    #print(" -  UID      : 0x%02x%02x%02x%02x" %
                     #   (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")

                    if rdr.select_tag(raw_uid) == rdr.OK:

                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            stat = rdr.write(8, text_to_bytes(text))
                            rdr.stop_crypto1()
                            if stat == rdr.OK:
                                #print(f"DATA: {text} WRITTEN TO ADDRESS 0x08")
                                print(f"OK!")
                                time.sleep(3)
                                break
                            else:
                                print("FAILED")
                        else:
                            print("AUTH ERR")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("EXITING PROGRAM")

if __name__=="__main__":
    #read_card()
    write_to_card('!@%*^&%')