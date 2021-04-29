import sys
from gmssl import sm2
from base64 import b64encode, b64decode

# sm2的公私钥
SM2_PUBLIC_KEY = "3059301306072a8648ce3d020106082a811ccf5501822d03420004f1f0321d62c854a2808d24bc020978bd307c7b21fca37b9ab5493e91395a3fb12fd13645946e63c1243295ae38eaa01ef1510f2e57bfb5289cd20f6aae4ce330"
SM2_PRIVATE_KEY = "308193020100301306072a8648ce3d020106082a811ccf5501822d0479307702010104204d8b61516fd82a0bb618a0893346105149aa3d89af527ff74fad19eb85dc936ba00a06082a811ccf5501822da14403420004f1f0321d62c854a2808d24bc020978bd307c7b21fca37b9ab5493e91395a3fb12fd13645946e63c1243295ae38eaa01ef1510f2e57bfb5289cd20f6aae4ce330"

sm2_crypt = sm2.CryptSM2(public_key=SM2_PUBLIC_KEY, private_key=SM2_PRIVATE_KEY)


# 加密
def encrypt(info):
    encode_info = sm2_crypt.encrypt(info.encode(encoding="utf-8"))
    encode_info = b64encode(encode_info).decode()  # 将二进制bytes通过base64编码
    return encode_info


# 解密
def decrypt(info):
    decode_info = b64decode(info.encode())  # 通过base64解码成二进制bytes
    decode_info = sm2_crypt.decrypt(decode_info).decode(encoding="utf-8")
    return decode_info

