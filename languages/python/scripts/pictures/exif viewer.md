#Voraussetzungen: pip install pillow
#liest EXIF Daten aus Bildern aus

```python
import sys
from PIL import Image
from PIL.ExifTags import TAGS



def main():
    if len(sys.argv) < 2:
        print("Usage: python EXIF_Viewer.py <bilddatei>")
        sys.exit(1)

    bildpfad = sys.argv[1]

    try:
        bild = Image.open(bildpfad)
        exif = bild._getexif()

        if not exif:
            print("Keine EXIF-Daten gefunden.")
            return

        print(f"EXIF-Daten für: {bildpfad}\n")

        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag:25}: {value}")

    except FileNotFoundError:
        print("Datei nicht gefunden.")
    except Exception as e:
        print("Fehler:", e)



if __name__ == "__main__":
    main()
```












