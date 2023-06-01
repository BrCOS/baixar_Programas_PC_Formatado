import urllib.request
import os
import sys

#! firefox - vscode - stremio - 7zip - git - qbitorrent - zoom - vlc - chrome
pastaDownloads = os.path.join(os.path.expanduser("~"), "Downloads", "arquivos")
if not os.path.exists(pastaDownloads):
    os.makedirs(pastaDownloads)

programas = [
    'https://download-installer.cdn.mozilla.net/pub/firefox/releases/113.0.2/win32/pt-BR/Firefox%20Installer.exe',
    'https://az764295.vo.msecnd.net/stable/b3e4e68a0bc097f0ae7907b217c1119af9e03435/VSCodeUserSetup-x64-1.78.2.exe',
    'https://download.documentfoundation.org/libreoffice/stable/7.5.3/win/x86_64/LibreOffice_7.5.3_Win_x86-64.msi',
    'https://www.7-zip.org/a/7z2201-x64.exe',
    'https://github.com/git-for-windows/git/releases/download/v2.40.1.windows.1/Git-2.40.1-64-bit.exe',
    'https://cdn.zoom.us/prod/5.14.8.16213/x64/ZoomInstallerFull.exe',
    'https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe',
    'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B8C887B4E-C0F7-7DDA-259A-67D89BA67F6C%7D%26lang%3Dpt-BR%26browser%3D3%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe',
    'https://download.anydesk.com/AnyDesk.exe'
]

print('Baixando os programas...')

for baixar in programas:
    links = baixar.split('/')[-1]
    arquivos = os.path.join(pastaDownloads, links)
    urllib.request.urlretrieve(baixar, arquivos)

print('Downloads Concluídos!')

sys.exit()
