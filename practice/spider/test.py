

import os
from urllib.request import urlopen
import urllib

import requests
from tqdm import tqdm


def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    """

    headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', headers)]
    urllib.request.install_opener(opener)
    file_size = int(urlopen(url).info().get('Content-Length', -1))



    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])
    req = requests.get(url, headers=header, stream=True)
    with(open(dst, 'ab')) as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.close()
    return file_size


if __name__ == '__main__':
    # url = "https://www.fk5778.com/video/5447"
    # download_from_url(url, "/Users/superhaha/Downloads/new.mp4")
    os.system('you-get -i https://www.fk5778.com/video/5447')