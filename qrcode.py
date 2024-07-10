import segno

qrcode = segno.make_qr("Hello Arjun")
qrcode.save(
    # "Link.SVG", == you can also create file in .svg format
    "New_code.png",
    scale=5,
    border=10,
    light='yellow',
    dark='blue', 
)