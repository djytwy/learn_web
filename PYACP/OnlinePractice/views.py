# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os,sys,subprocess,tempfile,time,re
import json

# Create your views here.

# 在线编辑代码后台处理并返回结果
class Python_practice(object):


    def __init__(self):
        # 创建临时文件夹，返回临时文件夹路径
        self.TempFiel = tempfile.mkdtemp(suffix='_practice', prefix='python3_')
        # 文件名
        self.FileNum = int(time.time()*1000)
        # python编译器位置
        self.EXEC = sys.executable

    # 获取py文件名
    def get_pyname(self):
        return 'test_%d' % self.FileNum

    # 接收代码写入文件
    def write_file(self,pyname,code):
        fpath = os.path.join(self.TempFiel, '%s.py' % pyname)
        with open(fpath, 'w') as o:
            o.write(code)
        return fpath
    # 编码
    def decode(self,s):
        try:
            return s.decode('utf-8')
        except UnicodeDecodeError:
            return s.decode('gbk')

    # 执行函数
    def run(self,code):
        r = dict()
        pyname = self.get_pyname()
        fpath = self.write_file(pyname, code)
        try:
            # subprocess.check_output是父进程等待子进程完成，返回子进程不标准输出的结果
            # stderr是标准输出的类型
            outdata = self.decode(subprocess.check_output([self.EXEC, fpath], stderr=subprocess.STDOUT))
        except subprocess.CalledProcessError as e:
            # 错误的信息标准输出,只截取报错部分
            reobj = re.compile(r'([\s\S]*Traceback[\s\S]*<module>)([\s\S]*)')
            reobj2 = re.compile(r'([\s\S]*File[\s\S]*\^)([\s\S]*)')
            result = self.decode(e.output)
            if reobj.search(result):
                data = reobj.search(result)
                outdata = ''.join(data.group(2).split('\n')[-2:])
                r['code'] = 'Error'
                r['output'] = outdata
                return r
            else:
                data = reobj2.search(result)
                outdata = ''.join(data.group(2).split('\n')[-2:])
                r['code'] = 'Error'
                r['output'] = outdata
                return r
        else:
            # 成功的信息标准输出
            r['code'] = 'Success'
            r['output'] = outdata
            return r
        finally:
            # 删除临时文件
            try:
                os.remove(fpath)
            except Exception as e:
                exit()

python_practice = Python_practice()


@csrf_exempt
def onlinepractice(request):
    if request.method == 'POST':
        code = request.POST.get('editor')
        result = python_practice.run(code)
        return HttpResponse(json.dumps(result), content_type='application/json')
    if request.method == 'GET':
        return render(request, 'onlinepractice/onlinepractice.html')