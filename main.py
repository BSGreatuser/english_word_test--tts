import random, time, os, sys, re
from gtts import gTTS
from playsound import playsound

try:
    list = open("words.txt", 'r', encoding='utf-8').readlines()
except FileNotFoundError:
    print('[!] 단어장이 없습니다. words.txt에 단어를 적어주세요.')
    f = open('words.txt', 'w')
    f.write('영단어:한글\nzoo:동물원')
    f.close()
    time.sleep(2)
    sys.exit(1)

o = 0
x = 0
count = 1
already = []

ckor = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
ceng = re.compile('[a-z|A-Z]')

if os.path.isfile('정답.txt') and os.path.isfile('./i/i.mp3'):
    a = input("안내 음성을 건너 뛰시겠습니까? [y/n]: ")
    if a == 'y':
        pass
    else:
        playsound('./i/i.mp3')
else:
    if os.path.isfile('./i/i.mp3'):
        playsound('./i/i.mp3')
    else:
        pass

of = open('정답.txt', 'w', encoding='utf-8')
nf = open('오답.txt', 'w', encoding='utf-8')
for i in range(len(list)):
    word = random.choice(list)
    while word in already:
        word = random.choice(list)
    already.append(word)

    if word.split == '':
        pass

    eng = str(word.split(':')[0]).rstrip()
    kor = str(word.split(':')[1]).rstrip()

    meng = ceng.search(eng)
    mkor = ckor.search(eng)

    neng = ceng.search(kor)
    nkor = ckor.search(kor)

    if mkor and not meng or not nkor:
        print('[-] {0} 단어를 건너뛰었습니다'.format(str(word).rstrip()))
        pass
    else:
        ctts = gTTS(text='{0}번'.format(count), lang='ko')
        cfile = 'count.mp3'
        ctts.save(cfile)

        tts = gTTS(text=eng, lang='en', slow=True)
        file = 'word.mp3'
        tts.save(file)

        playsound(cfile)
        for i in range(2):
            time.sleep(0.2)
            playsound(file)

        eng_answer = input('{0}번 영어: '.format(count))
        kor_answer = input('{0}번 한글: '.format(count))
        if eng_answer.rstrip() == eng and kor_answer.rstrip() == kor:
            o = o + 1
            of.write(word)
        else:
            x = x + 1
            nf.write('{0} (작성단어: {1}/{2})\n'.format(word.rstrip(), eng_answer.rstrip(), kor_answer.rstrip())
        count = count + 1

        time.sleep(1)
        os.remove(file)
        os.remove(cfile)

of.close()
nf.close()
print('\n>> 정답: {0}개\n>> 오답: {1}개'.format(o, x))
time.sleep(3)
sys.exit()
