import re,json,tkinter as tk
from tkinter import filedialog 

root = tk.Tk()
root.withdraw()


def loadResult():
    
    filename = filedialog.askopenfilename(initialdir=r'.\\',title='加载处理文件对话框',
        filetypes = [('ptk file','.ptk'),('txt files','.txt'),('all file','.*')] )

    with open(filename, 'rb') as f:
        start = False
        lines = []
        while True:
            line = f.readline()
            if line:
                if not start:
                    if line == b'>>>>> data of substations\r\n':
                        start = True
                        continue
                else:
                    if line == b'>>>>> tractive units\r\n':
                        break
                    if line == b'\r\n':
                        continue
                    line = line.decode(encoding="utf-8").strip()
                    if line != '':
                        lines.append(line)
            else:
                break
        return lines

def getElement(lines):
    elements = []
    element = []
    for line in lines:
        if '>>>>>' in line:
            if element != []:
                elements.append(element)
                element = []
            element.append(line)
        else:
            element.append(line)
    elements.append(element)
    return elements

def getElementForType(elements, elememtType):
    es = []
    for e in elements:
        if len(e) > 0 and e[0].find(elememtType) >= 0:
            # e[0].endswith('[ I   - CONTACT LINE SIDE ]'):
            es.append(e)
    return es

def is_number(s):
    try:
        if s == 'NaN':
            return False
        float(s)
        return True
    except ValueError:
        return False

def analysisElement(elmenet, eType, argsType):
    name = re.findall(r"[(](.*?)[)]", elmenet[0])[-1]
    args = dict()
    cols = dict()
    for line in elmenet:
        for key in argsType:
            if line.startswith(key):
                cols[key] = list(filter(lambda x: is_number(x), line.split()))
    bs = []
    if eType == elementType[3]:
        i = 0
        l = 0
        for k in cols:
            l = len(cols[k])
        while i < l:
            for key in argsType:
                for channel in argsType[key]:
                    args[channel[0]] = cols[key][channel[1] + i - 1]
            bs.append(args)
            args = dict()
            i += 4
        return name, bs
    else:
        for key in argsType:
            for channel in argsType[key]:
                args[channel[0]] = cols[key][channel[1] - 1]
        return name, [args]

def analysisElements(elmenets, eType, argsType):
    result = dict()
    for e in elmenets:
        name, args = analysisElement(e, eType, argsType)
        result[name] = args
    return result

def printElements(ret, i):
    ret = analysisElements(getElementForType(
        es, elementType[i]), elementType[i], argstype[i])
    for k in ret:
        print('---------'+k+'----------')
        for args in ret[k]:
            for (ak, av) in args.items():
                print(ak+':'+av + '\t')

def writeRestultToFile():
    filename = filedialog.asksaveasfilename(initialdir=r'.\\',title ='保持结果对话框',
        filetypes = [('txt files','.txt'),('all file','.*')] )

    with  open(filename,'w') as f:
        elementcout = len(elementType)
        for i in range(elementcout):
            ret = analysisElements(getElementForType(es, elementType[i]), 
            elementType[i], argstype[i])
            rows = []
            # for j, r in enumerate(ret):
            #     if j == 0:
            #         if i == 0:
            #             row = '项目名称\t'+r+'\t'
            #             rows.append(row)
            #         for args in ret[r]:
            #             for (k,v) in args.items():
            #                 row = k+'\t' + v+'\t'
            #                 rows.append(row)
            #     else:
            #         k = 0
            #         if i == 0:
            #             rows[0] += r+'\t'
            #             k += 1
            #         for args in ret[r]:
            #             for v in args:
            #                 rows[k] += args[v] +'\t'
            #                 k += 1
            #找出最大行数，主要应用于馈线输出
            def getmaxoutrows(ret):
                l = max([len(value) for value in ret.values()])
                if l<=0:return l,None
                elif l ==1:
                    for v in ret.values():
                        return l,v
                else:
                    for v in ret.values():
                        if len(v) == l:
                            return l,v
            l,rs = getmaxoutrows(ret)

            #输出行名称
            if i == 0:
                row = '项目名称\t'
                rows.append(row)
            for r in rs:
                for k,v in r.items():
                    row = k+'\t'
                    rows.append(row)
            #输出数据
            for r in ret:
                k = 0
                if i == 0:
                    rows[0] += r+'\t'
                    k += 1
                for j in range(l):
                    if j < len(ret[r]):
                        args = ret[r][j]
                        for v in args:
                            rows[k] += args[v] +'\t'
                            k += 1
                    else:
                        args = rs[j]
                        for v in args:
                            rows[k] +='  \t'
                            k += 1
            #写入文件   
            for row in rows:
                f.writelines(row + '\n')

def loadArgs():
        filename = filedialog.askopenfilename(initialdir=r'.\\',title ='加载处理文件的参数配置文件对话框',
            filetypes = [('txt files','.txt'),('all file','.*')] )
        if filename:
            with open(filename,'r') as f:
                elementType = json.loads(f.readline())
                targs = json.loads(f.readline())
                fargs = json.loads(f.readline())
                tfargs = json.loads(f.readline())
                bargs = json.loads(f.readline())
                return elementType,targs,fargs,tfargs,bargs
        else: 
            return None
        

elementType = ['[ I   - CONTACT LINE SIDE ]', '[ II  - NEGATIVE FEEDER SIDE ]',
               '[ III - PRIMARY SIDE ]', '>>>>> branch connectors']

targs = {'root mean sqare': [('T绕组电流有效值（A）', 2), ('T绕组功率有效值（kVA）', 3)],
         'maximum': [('T绕组电流最大值（A）', 2), ('T绕组功率最大值（kVA）', 3)]}
fargs = {'root mean sqare': [('F绕组电流有效值（A）', 2), ('F绕组功率有效值（kVA）', 3)],
         'maximum': [('F绕组电流最大值（A）', 2), ('F绕组功率最大值（kVA）', 3)]}
tfargs = {'root mean sqare': [('高压绕组电流有效值（A）', 2), ('高压绕组功率有效值（kVA）', 3)],
          'maximum': [('高压绕组电流最大值（A）', 2), ('高压绕组功率最大值（kVA）', 3)]}

bargs = {'root mean sqare': [('下行T线电流有效值（A）', 1), ('上行T线电流有效值（A）', 2),
                             ('下行F线电流有效值（A）', 3), ('上行F线电流有效值（A）', 4)],
         'maximum': [('下行T线电流最大值（A）', 1), ('上行T线电流最大值（A）', 2),
                     ('下行F线电流最大值（A）', 3), ('上行F线电流最大值（A）', 4)]}

argstype = [targs, fargs, tfargs, bargs]
# def saveArgs(filename):
#     with open(filename,'w') as f:
#         json.dump(elementType,f,ensure_ascii=False)
#         argstype = [targs, fargs, tfargs, bargs]
#         for args in argstype:
#            f.write('\n')
#            json.dump(args,f,ensure_ascii=False)
# saveArgs(r'.\webnet\argstype.txt')
ret = loadArgs()
if ret:
    elementType,targs,fargs,tfargs,bargs = ret

lines = loadResult()
es = getElement(lines)

writeRestultToFile()
# printElements(es,3)

                            
                
                    





    
