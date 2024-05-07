import sys
import exifread

def get_exif_data(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            return tags
    except IOError:
        return None

def extract_info(file_path, tags):
    if tags is None:
        print("Error! - File Not Found!")
        return

    make = tags.get('Image Make', 'N/A')
    model = tags.get('Image Model', 'N/A')
    datetime_original = tags.get('EXIF DateTimeOriginal', 'N/A')
    latitude_tag = tags.get('GPS GPSLatitude')
    longitude_tag = tags.get('GPS GPSLongitude')

    if latitude_tag is not None and longitude_tag is not None:
        latitude = str(latitude_tag) + ' ' + str(tags.get('GPS GPSLatitudeRef', 'N/A'))
        longitude = str(longitude_tag) + ' ' + str(tags.get('GPS GPSLongitudeRef', 'N/A'))
    else:
        latitude = longitude = 'N/A'

    print(f"Source File: {file_path}")
    print(f"Make: {make}")
    print(f"Model: {model}")
    print(f"Original Date/Time: {datetime_original}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

def main():
    if len(sys.argv) != 2:
        print("Error! - No Image File Specified!")
        return

    file_path = sys.argv[1]
    exif_data = get_exif_data(file_path)
    extract_info(file_path, exif_data)

if __name__ == "__main__":
    main()
