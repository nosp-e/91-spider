import asyncio
import argparse

import spiders

log = print


def catchM3U8(inpath, outpath):
    with open(inpath) as f:
        lines = f.readlines()
    log('Read {} urls in total'.format(len(lines)))

    asyncio.get_event_loop().run_until_complete(spiders.crawlInfos(lines))
    
    data = spiders.getData()
    
    log('Get {} urls in total, output to {}'.format(len(data), outpath))
    with open(outpath, 'w') as f:
        f.write('\n'.join(data))


def catchList(num, outpath):
    urls = []
    for i in range(num):
        urls.append('http://91porn.com/v.php?category=rf&viewtype=basic&page={}'.format(i))
    
    asyncio.get_event_loop().run_until_complete(spiders.crawlLists(urls))
    
    data = spiders.getData()
    
    log('Get {} urls in total, output to {}'.format(len(data), outpath))
    with open(outpath, 'w') as f:
        f.write('\n'.join(data))


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=lambda _: parser.print_help())
    subparsers = parser.add_subparsers(help='choose the mode')

    pageParser = subparsers.add_parser('page')
    pageParser.add_argument('--in', type=str, default='./data/urls.txt', help='for page, the input url list file')
    pageParser.add_argument('--out', type=str, default='./data/m3u8s.txt', help='for page/list, the output urls list file')
    
    pageParser.set_defaults(func=lambda args: catchM3U8(vars(args)['in'] , args.out))

    listParser = subparsers.add_parser('list')
    listParser.add_argument('--num', type=int, default=1, help='how many pages of list do you want')
    listParser.add_argument('--out', type=str, default='./data/urls.txt', help='for page/list, the output urls list file')
    
    listParser.set_defaults(func=lambda args: catchList(args.num, args.out))

    args = parser.parse_args()
    args.func(args)
    

if __name__=='__main__':
    main()