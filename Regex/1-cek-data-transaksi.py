import re

def CekDataTrx(notes):
    paymentBill={}
    paymentBill['succes']=False
    blankNotes=[
        ("nomor_seri","SN:(\d+)"),
        ("nomor_ref","Ref Id.: (\d+)"),
        ("id_order","#(\d+)"),
        ("id_transaksi","[A-z]+-[a-zA-z]+[|][A-z]+-\d+")
    ]
    
    for bNote in blankNotes:
        for note in notes:
            a = re.findall(bNote[1],note)
            if a:
                paymentBill[bNote[0]]=a[0]
                break
            elif not a:
                paymentBill[bNote[0]]=None

    if paymentBill['nomor_ref']:
        paymentBill["succes"]=True
    
    return paymentBill

print(CekDataTrx([
'Insert Transaction #14789',
'Update Status To Pending Payment with Deposit',
'Transaction paid trx_id = YPTRSX-Indragiri|IDG-14879',
'Transaction on Biller type_modem arg : telkomsel_mobile queue_name arg : smtel-banyumas_mobile',
'Success Manual SN:94309403940394039403 Ref Id.: 394039403'
]))
'''
{
    'nomor_ser':'94309403940394039403',
    'id_transaksi':'14879',
    'id_order':'YPTRSX-Indragiri|IDG-14879',
    'nomor_referensi':'394039403'
    'succes':True
}
'''

print(CekDataTrx([
'Insert Transaction #18254',
'Update Status To Pending Payment with Deposit',
'Transaction paid trx_id = YPTRSX-Banyumas|BYS-18254',
'Transaction on Biller type_modem arg : telkomsel_mobile queue_name arg : smtel-banyumas_mobile',
'Trx. Cancel Process Begin | cancel trx with id 18254'
'Success Refunded trx id. 18254 with Wallet hash #eko827p7rk89m456'
]))

'''
{
    'nomor_seri': None,
    'id_transaksi':'18254',
    'id_order':'YPTRSX-Banyumas|BYS-18254',
    'nomor_referensi': None
    'succes':False
}
'''