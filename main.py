import qrcode

print("QR코드를 만들 URL을 입력해주세요")
url = input()
img = qrcode.make(url)

print("완료 되었습니다! 파일명을 입력해주세요")
title = input()
img.save(f"{title}.png")