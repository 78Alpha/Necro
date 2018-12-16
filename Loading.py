import sys, time

def loading(stub,sub, sen, stubs):
    print(stub, end='')
    sys.stdout.flush()
    for letter in sub:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()
        cursor()
        time.sleep(.01)
    print(stubs, end='')

def cursor():
    spinner = spinning_cursor()
    for _ in range(5):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
