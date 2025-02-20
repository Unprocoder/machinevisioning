import cv2
#*https://www.youtube.com/watch?v=TGQcDaZ56ao&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=4

# Konenäeön harjoittelua

# kuvan määritys, 0 määrittää kuvan harmaaksi
img = cv2.imread('lena.jpg', 0)

# kuvan printtaus matriisina
print(img)

# kuvan avaus ikkunaan
cv2.imshow('image', img)

# näyttää kuvan syötetyn verran millisekunneissa ja ikkunan tuhoaminen
# 0 jättää ikkunan auki kunnes se suljetaan
k = cv2.waitKey(0)

# 27 → esc, jolla ikkuna tuhotaan. Painamalla S kuva tallennetaan
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # kuvan tallentaminen tiedostoksi
    cv2.imwrite('lena_copy.png', img)