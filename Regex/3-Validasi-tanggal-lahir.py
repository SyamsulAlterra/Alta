import re

yearPattern="(19\d{2}|20\d{2})"
monthPattern="(-1[012]-|-0\d-)"
day30Pattern="(30|[012]\d)\Z"
day31Pattern="(3[01]|[012]\d)\Z"
leapFebPattern="([012]\d\Z)"
normalFebPattern="2[012345678]\Z|[01]\d\Z"

def checkKabisat(y):    
    if y%4 == 0 and y%100 != 0:
        return True
    elif y%4 == 0 and (y%100 == 0 and y%400 == 0):
        return True
    else:
        return False

def validasiTanggal(arr):
    output={}
    output['invalid']=[]
    output['valid']=[]

    for person in arr:
        year=re.search(yearPattern,person['tgl_lahir'])
        month=re.search(monthPattern,person['tgl_lahir'])

        if not year:
            person['alasan']='format tahun diluar ketentuan (1900 - 2099)'
            output['invalid'].append(person)
            continue
        elif not month:
            person['alasan']='format bulan diluar ketentuan (01-12)'
            output['invalid'].append(person)
            continue
        
        if checkKabisat(int(year.group(1))):
            if int(month.group(1)[1:3]) == 2:
                day=re.search(leapFebPattern,person['tgl_lahir'])
                if not day:
                    person['alasan']='format hari diluar ketentuan kabisat Februari'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
            elif int(month.group(1)[1:3]) in [1,3,5,7,8,10,12]:
                day=re.search(day31Pattern,person['tgl_lahir'])
                if not day:
                    person['alasan']='format hari diluar ketentuan bulan berhari 31'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
            elif int(month.group(1)[1:3]) in [4,6,9,11]:
                day=re.search(day30Pattern,person['tgl_lahir'])
                if not day:
                    person["alasan"]='format hari diluar ketentuan bulan berhari 30'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
        else:
            if int(month.group(1)[1:3]) == 2:
                day=re.search(normalFebPattern,person['tgl_lahir'])
                if not day:
                    person['alasan']='penunjuk hari dalam bulan terkait tidak valid (cek aturan tahun kaibsat)'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
            elif int(month.group(1)[1:3]) in [1,3,5,7,8,10,12]:
                day=re.search(day31Pattern,person['tgl_lahir'])
                if not day:
                    person['alasan']='format hari diluar ketentuan bulan berhari 31'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
            elif int(month.group(1)[1:3]) in [4,6,9,11]:
                day=re.search(day30Pattern,person['tgl_lahir'])
                if not day:
                    person["alasan"]='format hari diluar ketentuan bulan berhari 30'
                    output['invalid'].append(person)
                    continue
                else:
                    output['valid'].append(person)
                    continue
        
    return output
                
        
        # if checkKabisat(year):
        #     pass
    # output={}
    # for person in arr:
    #     checkYear=re.findall(yearPattern,person['tgl_lahir'][0:4])
    #     if not checkYear and :

jane={'name':'Jane Doe', 'tgl_lahir':'1992-10-31'}
jack={'name':'Jack Doe', 'tgl_lahir':'1997-02-29'}
donny={'name':'Donny Doe', 'tgl_lahir':'1998-12-01'}
bayu={'name':'Bayu Aji', 'tgl_lahir':'1983-04-31'}
tia={'name':'Tia Nugroho', 'tgl_lahir':'1984-08-29'}
ariel={'name':'Ariel Bayu', 'tgl_lahir':'1988-07-32'}

#test case 1
print(validasiTanggal([jane,jack,donny]))
'''
{
    'invalid':[{'tgl_lahir':'1997-02-29', 'nama': 'Jack Doe', 'alasan': [penunjuk
hari dalam bulan terkait tidak valid (cek aturan tahun kaibsat)]}],
    'valid':[{'tgl_lahir':'1992-10-31', 'nama': 'Jane Doe'}, {'tgl_lahir':
'1988-12-01', 'nama': 'Donny Doe'}]
}
'''

#test case 2
print(validasiTanggal([bayu, tia, ariel]))
'''
{
    'invalid':[{'tgl_lahir':'1988-07-32', 'nama': 'Ariel Bayu', 'alasan': ['hari diluar batas yang ditentukan']},
               {{'tgl_lahir':'1983-04-31', 'nama': 'Bayu Aji', 'alasan': ['hari diluar batas yang ditentukan']}],
    'valid':[{'tgl_lahir':'1984-08-29', 'nama': 'Tia Nugroho'}]
}
'''