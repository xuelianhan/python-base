import requests
import os

"""
Code refer 
<a href="https://www.scaler.com/topics/python-download-file-from-url/"></a>
<a href="https://stackoverflow.com/questions/56950987/download-file-from-url-and-save-it-in-a-folder-python"></a>
"""
class Crawler:

    def __init__(self):
        pass

    """
    https://www.csun.edu/~ctoth/Handbook/chap1.pdf
    https://www.csun.edu/~ctoth/Handbook/chap68.pdf
    
    """

    def craw(self):
        # from 4 to 68
        prefix = 'https://www.csun.edu/~ctoth/Handbook/chap'
        suffix = '.pdf'
        for i in range(4, 5):
            url = prefix + str(i) + suffix
            # file_name = str(i) + suffix
            file_name = url.split('/')[-1].replace(" ", "_")  # be careful with file names
            file_path = os.path.join("/Users/randyhubbard/Downloads/computegeometry", file_name)
            r = requests.get(url, stream=True)
            if r.ok:
                print("saving to", os.path.abspath(file_path))
                with open(file_path, "wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                        # writing one chunk at a time to a pdf file
                        if chunk:
                            pdf.write(chunk)
                            pdf.flush()
                            os.fsync(pdf.fileno())
                        else:
                            print("Download failed: status code {}\n{}".format(r.status_code, r.text))

    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
                    else:  # HTTP status code 4XX/5XX
                        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


instance = Crawler()
instance.craw()
# instance.download("http://website.com/Motivation-Letter.docx", dest_folder="mydir")
