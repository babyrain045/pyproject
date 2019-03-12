


while True:
    try:
        card = input().split('-')
        handcard_1, handcard_2 = card[0].split(), card[1].split()
        match_dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
        s = ''
        if handcard_1[0] == 'joker' or handcard_2[0] == 'joker':
            print('joker','JOKER')
        elif len(handcard_1) == len(handcard_2):
            a = handcard_1 if match_dict[handcard_1[0]] > match_dict[handcard_2[0]] else handcard_2
            for i in a:
                s  = s + i + ' '
            print(s.strip())
        elif len(handcard_1) == 4 or len(handcard_2) == 4:
            a = handcard_1 if len(handcard_1) == 4 else handcard_2
            for i in a:
                s = s + i + ' '
            print(s.strip())
        else:
            print('ERROR')




    except:
        break