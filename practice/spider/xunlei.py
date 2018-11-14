#!/usr/bin/env python3
# requires XCode

import subprocess, sys, os, hashlib, plistlib


package = '/Applications/Thunder.app/Contents'
executable = os.path.join(package, 'MacOS/Thunder')
plugins_dir = os.path.join(package, 'BrowserPlugins')


def backup():
    from shutil import copyfile
    backup = executable + '.bak'

    if os.path.isfile(backup):
        print('Backup found, maybe the file has already been patched.')
        sys.exit(-1)

    copyfile(executable, backup)


def patch_exec():
    ret_1 = b'\xb8\x01\x00\x00\x00\xc3'

    try:
        output = subprocess.check_output(['nm', executable])
    except:
        print('Failed to execute nm, please install XCode.')
        sys.exit(-1)

    patch_list = ['-[LocalTask isValidLixianTask]', '-[UserController isVip]',
                  '-[UserController isPlatinum]', '-[UserController isDiamond]']
    base = None
    output = output.decode('utf8')

    with open(executable, 'r+b') as f:
        for line in output.splitlines():
            if '__mh_execute_header' in line:
                base, *_ = line.split()
                base = int(base, 16)

        if not base:
            print('Failed to retrive base address')
            sys.exit(-1)

        for line in output.splitlines():
            if not len(patch_list):
                break

            for func in patch_list:
                if func in line:
                    addr, *_ = line.split()
                    addr = int(addr, 16)

                    offset = addr - base
                    f.seek(offset, 0)
                    f.write(ret_1)  # patch function

                    print(func)
                    patch_list.remove(func)

                    break

    print('Successfully patched %s' % executable)


# 搞定main里的自校验
def patch_self_check():
    m = hashlib.md5()
    with open(executable, 'rb+') as f:
        while True:
            buf = f.read(1)
            if not buf:
                break
            m.update(buf)
            f.seek(1023, 1)
    digest = m.digest()
    lookup = (15, 4, 6, 3, 1, 0, 7, 8, 2, 11, 10, 13, 12, 14, 9, 5)
    hexdigest = ''.join(['%0.2X' % digest[index] for index in lookup])
    dirname = os.path.join(plugins_dir, hexdigest)

    if not os.path.isdir(dirname):
        os.mkdir(dirname)


def clear_quit_flag():
    plist_path = os.path.join(os.environ.get(
        'HOME'), 'Library/Preferences/com.xunlei.Thunder.plist')

    with open(plist_path, 'rb+') as f:
        pref = plistlib.load(f)

        force_quit = pref.get('ForceQuit')
        if force_quit:
            pref.update({'ForceQuit': True})
            plistlib.dump(pref, f)
            print('Clear quit flag')


if __name__ == '__main__':
    backup()
    patch_exec()
    patch_self_check()
    # clear_quit_flag()