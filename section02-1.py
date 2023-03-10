# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimage.nmv.naver.net%2Fblog_2023_01_03_3070%2F0518b855-8b3f-11ed-97c6-d4f5ef58ad5e_01.jpg&type=ofullfill340_600_png'
html_url = 'https://www.google.com'

# 다운받을 경로
save_path1 = '/Users/leejeongmin/test1.jpg'
save_path2 = '/Users/leejeongmin/index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))

    # 성공
    print('Download Succeed')
