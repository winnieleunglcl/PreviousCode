import collections
import string

def occurence(m):
    message = m.split(" ")
    letter_count = dict([chr(i),0] for i in range(97,123))     #create a dictionary to store each lowercase characters' occurence frequency
    
    each_chara = []
    for i in message:
        for j in i:
            if j != " ":
               each_chara.append(j)
    each_chara = [i.lower() for i in each_chara]               #turn all the characters into lowercase and store them in a list (space is excluded)
    
    each_chara_only_letters = each_chara    
    each_chara_only_letters = ["".join(a for a in s if a not in string.punctuation) for s in each_chara_only_letters]      
    each_chara_only_letters = [s for s in each_chara_only_letters if s]
    each_chara_only_letters = [element for element in each_chara_only_letters if all(digit not in element for digit in "1234567890")]    #This list will not store punctuations and integers
                                                                                                                                         #Length of this list can be used to calculate the normalized frequencies
                                                                                                                                         
    for i in each_chara:
      if i in letter_count:
         letter_count[i] += 1          #count each lowercase characters' occurence frequency
                                                
                                                                                                
    occur_per = letter_count
    for i in letter_count:
        occur_per[i] = round((letter_count[i] / (len(each_chara_only_letters)))*100,2)            #create a dictionary to store each character as its keys 
    sorted_occur_per = {}                                                                         #and each character's normalized frequency percentage as its values
    for key, value in sorted(occur_per.items(), key = lambda item: item[1], reverse = True):      #sort by the values (descending)
        sorted_occur_per.update({key:value})
        
    sorted_occur_per_list = []
    for key, value in sorted_occur_per.items():
        temp = [key,value]
        sorted_occur_per_list.append(temp)                #turn the "sorted_occur_per" dictionary into a list

        
    sorted_expected_frequency = {}
    expected_frequency = {"a":8.17, "b":1.49, "c": 2.78, "d":4.25, "e":12.7, "f":2.23, "g":2.02, "h":6.09, "i":6.97, "j":0.15, "k":0.77, "l":4.03, "m":2.41,
                          "n":6.75, "o":7.51, "p": 1.93, "q":0.10, "r":5.99, "s":6.33, "t":9.06, "u":2.76, "v":0.98, "w":2.36, "x":0.15, "y":1.97, "z":0.07}
    for key, value in sorted(expected_frequency.items(), key = lambda item: item[1], reverse = True):
        sorted_expected_frequency.update({key:value})                                                          #create a dictionary to store each character as its keys
                                                                                                               #and each character's expected frequency percentage as its values
        
    sorted_expected_frequency_list = []
    for key, value in sorted_expected_frequency.items():
        temp = [key,value]
        sorted_expected_frequency_list.append(temp)       #turn the "sorted_expected_frequency" dictionary into a list

    
    return (sorted_occur_per_list, sorted_expected_frequency_list)   #return those calculated lists
    

def analyze(m):
    map1 = {}
    map_list = []
    diff = [0.0]*26
    chara1 = ""
    chara2 = ""
    
    sorted_occur_per_list, sorted_expected_frequency_list = occurence(m)   #get back the returns
    
    for i in range(len(sorted_occur_per_list)):
        map_list.append([(sorted_expected_frequency_list[i]),(sorted_occur_per_list[i])])    #combine the two lists into a list (list of lists of lists)
    
    for i in range(26):
        chara1 = map_list[i][1][0]
        chara2 = map_list[i][0][0]
        diff[ord(chara1)-97] = round(abs(map_list[i][0][1]-map_list[i][1][1]),2)     #calculate the differences and assign them into corresponding place in the list(a-z)
        map1.update({chara1 : chara2})        #sub the original charcter and mapped character into the map accordingly

    print("map","        difference")
    for i in range(26):
        print(f"{chr(i+97)} <- {map1[chr(i+97)]}      {diff[i]:0.2f}%".format(diff[i]))
    return map1

def decrypt(m,map1):
    new_m = ""
    
    for i in m:
        if 64< ord(i) <91:
            new_m += chr(ord(map1[chr(ord(i)+32)])-32)  #When uppercase letters are obtained, they should be turned into lowercase letters for operation first. When it is finished, turn it back to uppercase
            continue
        if 96< ord(i) <123:
            new_m += map1[i]                            #When lowercase letters are obtained, they do not matter. Just concatenate them into the new message
            continue
        new_m += i                                      #The only left data types are space or punctuations or numbers
                                                        #When they are obtained, just concatenate them into the new message
    return new_m
    
m1 = "This text introduces students to programming and computational problem \
solving using the Python 3 programming language. \
It is intended primarily for a first-semester computer science (CS1) course, \
but is also appropriate for use in any course providing an introduction \
to computer programming and/or computational problem solving. The book \
provides a step-by-step,'hands on' pedagogical approach which, together \
with Python's clear and simple syntax, makes this book easy to teach and \
learn from."

m2 = "Ziol ztbz ofzkgrxetl lzxrtfzl zg hkgukqddofu qfr egdhxzqzogfqs hkgwstd \
lgscofu xlofu zit Hnzigf 3 hkgukqddofu sqfuxqut. \
Oz ol ofztfrtr hkodqkosn ygk q yoklz-ltdtlztk egdhxztk leotfet (EL1) egxklt, \
wxz ol qslg qhhkghkoqzt ygk xlt of qfn egxklt hkgcorofu qf ofzkgrxezogf \
zg egdhxztk hkgukqddofu qfr/gk egdhxzqzogfqs hkgwstd lgscofu. Zit wgga \
hkgcortl q lzth-wn-lzth,'iqfrl gf' htrquguoeqs qhhkgqei vioei, zgutzitk \
vozi Hnzigf'l estqk qfr lodhst lnfzqb, dqatl ziol wgga tqln zg ztqei qfr \
stqkf ykgd. \
Zit hkodqkn ugqs of zit rtctsghdtfz gy ziol ztbz vql zg ektqzt q htrquguoeqssn \
lgxfr qfr qeetllowst ztbzwgga ziqz tdhiqlomtl yxfrqdtfzqs hkgukqddofu \
qfr egdhxzqzogfqs hkgwstd-lgscofu egfethzl gctk zit dofxzoqt gy q hqkzoexsqk \
hkgukqddofu sqfuxqut. Hnzigf'l tqlt of zit ektqzogf qfr xlt gy wgzi ofrtbtr \
qfr qllgeoqzoct rqzq lzkxezxktl (of zit ygkd gy solzl/zxhstl qfr roezogfqkotl), \
Ql vtss ql ltzl, qssgvl ygk hkgukqddofu egfethzl zg wt rtdgflzkqztr vozigxz \
zit fttr ygk rtzqostr rolexllogf gy hkgukqddofu sqfuxqut lhteoyoel. \
Zqaofu qrcqfzqut gy Hnzigf'l lxhhgkz gy wgzi zit odhtkqzoct (o.t., hkgetrxkqs) \
qfr gwptezgkotfztr hqkqroudl, q 'wqea zg wqloel', 'gwptezl-sqzt' qhhkgqei \
ol zqatf zg egdhxztk hkgukqddofu. \
Oz ygssgvl zit wtsoty ziqz lgsor ukgxfrofu of odhtkqzoct hkgukqddofu \
ligxsr hktetrt zit sqkutk fxdwtk gy (qfr dgkt qwlzkqez) egfethzl gy zit \
gwptez-gkotfztr hqkqroud. Zitktygkt, gwptezl qkt fgz egctktr xfzos Eiqhztk 5, \
qfr gwptez-gkotfztr hkgukqddofu ol fgz ofzkgrxetr xfzos Eiqhztk 10. \
Ygk ziglt vig rg fgz voli zg ofzkgrxet gwptez-gkotfztr hkgukqddofu, \
Eiqhztk 10 eqf tqlosn wt laohhtr. Ziqfal."


mapping = analyze(m1)
print("Mapping dictionary:",mapping)
print("plaintext:",decrypt(m1,mapping))
print("plaintext:",decrypt(m1,{'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f',
 'g':'g','h':'h','i':'i','j':'j','k':'k','l':'l','m':'m',
'n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t',
'u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}))

mapping = analyze(m2)
print("Mapping dictionary:",mapping)
print("plaintext:",decrypt(m2,mapping))
print("plaintext:",decrypt(m2,{'e':'d', 'l':'s', 'w':'g', 'x':'f', 'q':'a',
 'h':'r', 'i':'h', 'n':'p', 'g':'o', 'r':'l', 'z':'t',
's':'m', 'p':'j', 'a':'v', 'u':'u', 'y':'y', 'j':'z',
'c':'b', 't':'e', 'd':'c', 'b':'x', 'o':'i', 'v':'k',
'f':'w', 'm':'q', 'k':'n'}))
print("plaintext:",decrypt(m2,{'e':'d', 'l':'s', 'w':'g', 'x':'f', 'q':'a',
 'h':'p', 'i':'h', 'n':'y', 'g':'o', 'r':'l', 'z':'t',
 's':'m', 'p':'j', 'a':'v', 'u':'u', 'y':'r', 'j':'z',
'c':'b', 't':'e', 'd':'c', 'b':'x', 'o':'i', 'v':'k',
'f':'n', 'm':'q', 'k':'w'}))

