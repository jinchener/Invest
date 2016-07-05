file = open("list.txt")
    try:
        while 1:
            mySpider = regexSpider()
            line = file.readline()
            line1=line.replace('\n','' )
            str1=r'd[0-9]{1,2}'
            startUrlList=[line1]
            downUrlRegex=line1+str1
            writeUrlRegex=line1+str1
            writeFileName = "data/sogou.dat"
            ignoreUrlRegex = "(.*author\.php.*)|(.*search\.php.*)|(.*goto\.php.*)|(.*#top)"
            mySpider.spiderWorking(startUrlList,downUrlRegex,writeUrlRegex,ignoreUrlRegex,writeFileName,200)
            if not line:
                break
    finally:
        file.close()