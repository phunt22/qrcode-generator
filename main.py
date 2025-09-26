import qrcode
import sys

def generate_qr(link: str, filename: str):
  img = qrcode.make(link)
  img.save(filename)
  print(f"✅ QR code saved as {filename}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python generate_qr.py <link-or-text> <output-file.png>")
  else:
    link = sys.argv[1]
    outfile = sys.argv[2]
    generate_qr(link, outfile)
