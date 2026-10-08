# builds index.html (full document for GitHub Pages / local) from src.html (artifact page body)
src=open('src.html',encoding='utf-8').read()
head='<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'
i=src.index('</style>')+len('</style>')
open('index.html','w',encoding='utf-8').write(head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n')
