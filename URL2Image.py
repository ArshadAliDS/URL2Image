import os
import pandas as pd
import urllib.request
from IPython.display import clear_output

FILENAME = 'Path'
FILE_PATH = 'Path'

urls = pd.read_csv(FILENAME)
urls['Download_Status'] = ''  # Add a new column for download status

for i, url in enumerate(urls.values):
    image_name = url[1]
    image_no = url[2]
    print(len(urls) - i)

    filename = 'image-' + str(image_name) + '-' + str(image_no) + '.Jpg'
    full_path = os.path.join(FILE_PATH, filename)

    if os.path.exists(full_path):
        print(f"Skipping {filename}. File already exists.")
        urls.at[i, 'Download_Status'] = 'Skipped'
    else:
        try:
            urllib.request.urlretrieve(url[0], full_path)
            urls.at[i, 'Download_Status'] = 'Downloaded'
        except Exception as e:
            print('Error downloading {}: {}'.format(filename, str(e)))
            urls.at[i, 'Download_Status'] = 'Error: {}'.format(str(e))
    
    clear_output(wait=True)  # Clear existing displayed output

# Save the updated DataFrame back to the CSV file
urls.to_csv(FILENAME, index=False)
print('Download process completed!')
