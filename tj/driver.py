import json

from pythoncode.tj import Sm2Utils


def test_driver():
    text = ("<Root>"
            "<Body>"
            "<DocumentNumber>190328123728797</DocumentNumber>"
            "<SendToProDateTime>20200331155142</SendToProDateTime>"
            "<Carrier>长春市晟源物流有限公司</Carrier>"
            "<ActualCarrierID>91220101309961336A</ActualCarrierID>"
            "<VehicleNumber>黑BJ2306</VehicleNumber>"
            "<VehiclePlateColorCode>1</VehiclePlateColorCode>"
            "<ShippingNoteList>"
            "<ShippingNoteNumber>190328123728797</ShippingNoteNumber>"
            "<SerialNumber>0000</SerialNumber>"
            "<TotalMonetaryAmount>28394.260</TotalMonetaryAmount>"
            "</ShippingNoteList>"
            "<Financiallist>"
            "<PaymentMeansCode>32</PaymentMeansCode>"
            "<Recipient>郑中华</Recipient>"
            "<ReceiptAccount>6222620930006535951</ReceiptAccount>"
            "<BankCode>COMM</BankCode>"
            "<SequenceCode></SequenceCode>"
            "<MonetaryAmount>2000.000</MonetaryAmount>"
            "<DateTime>20200331155142</DateTime>"
            "</Financiallist>"
            "</Body>"
            "</Root>")
    msg = Sm2Utils.encrypt(json.dumps(text))
    print(msg)
    return msg

def test_bbb():
        return "Wagner小"

def test_a():
    test_bbb()

# print(text.encode("UTF-8"))
#
# encrypt_str = sm2_crypt.encrypt(text.encode("UTF-8"))
# print(encrypt_str)
# decrypt_str = sm2_crypt.decrypt(encrypt_str)
# print(decrypt_str)
#
# encrypt_str = encrypt_str.hex()
# print(encrypt_str)
# tok = tokenutils.tokenutils().get()
# jsonData = {"UserId": Gansu.USER_ID, "Token": tok, "MessageReferenceNumber": "12212131232", "DocumentName": "驾驶员",
#             "MessageSendingDateTime": "20191126134923", "IPCType": "WLHY_JSY1001", "EncryptedContent": encrypt_str}
# print(jsonData)
# headers = {'Content-Type': 'application/json'}
# postData = json.dumps(jsonData)
# req = requests.post(Gansu.URL + "/wlhy/send", headers=headers, data=postData)
# print(req.text)
