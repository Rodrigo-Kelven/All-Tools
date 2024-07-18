from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=90)

captcha_texto = input("Digite o texto do captcha qe deseja: ")

captcha_text = f"{captcha_texto}"

data = image.generate(captcha_text)

image.write(captcha_text, "captcha.png")