from flask import Flask, request, json, jsonify, render_template, make_response
from flask_cors import CORS
import re
import pdfkit

path_wk = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'  # wkhtmltopdf安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)
options = {'page-size': 'A4', 'dpi': 400, 'disable-smart-shrinking': ''}
# pdfkit.from_file('C:/Users/ASUS/Desktop/录取喜报1.jpg', 'C:/Users/ASUS/Desktop/out.pdf', configuration=config)

table = {"thead": ['姓名', '科类', '投档分数', '录取专业', '录取方式'], "tbody": []}

schools = {"贵阳一中":
           {
               'rescent':
               [
                   {
                       'year': 2019,
                       'artNumber': 3,
                       'scienceNumber': 20,
                       'total': 23,
                       'provinceTotal': 93,
                       'rate': 0.2473
                   }
               ],
               'student':
               [
                   ['伊力凡·阿布都·艾尔肯·铁木耳·哈力克', '理科', 650, '理科实验班（物理，化学，数学）', '本科第一批次'], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'], [
                       '李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', ''], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'],
                        ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批'], ['李华', '理科', 650, '物理', '本一批']
               ]
           },
           "厦门外国语学校": {'rescent': [{
               'year': 2019,
               'artNumber': 10,
               'scienceNumber': 20,
               'total': 12,
               'provinceTotal': 80,
               'rate': 0.15
           }]}}

app = Flask(__name__)
CORS(app)  # 设置跨域


@app.route('/getSchool/rescent', methods=['GET'])
def getContent():
    responce = []
    data = request.args.get('school')
    for school in schools:
        if data == school:
            responce = schools[school]['rescent']
            print(responce)
    return jsonify(responce)


@app.route('/luquxibao', methods=['POST'])
def savePdf():
    schoolName = request.get_json('data')['school']
    theads = ['姓名', '科类', '投档分数', '录取专业', '录取方式']
    pageNum = 8
    students = []
    for school in schools:
        if school == schoolName:
            for stu in schools[school]['student']:
                students.append(stu)
    page_theory = len(students) // pageNum
    page_count = 0
    while page_count <= page_theory:
        if page_count == page_theory:
            num = len(students) - page_theory * \
                (len(students) // (page_theory + 1))
        else:
            num = len(students) // (page_theory + 1)
        tbodys = []
        for i in range(num):
            tbodys.append(students[i])
        print(tbodys)
        location = 'C:/Users/ASUS/Desktop/out{}.pdf'.format(page_count+1)
        rendered = render_template(
            'index.html', theads=theads, students=tbodys, schoolName=schoolName)
        pdfkit.from_string(rendered, location,
                           configuration=config, options=options)
        page_count = page_count + 1
    return '成功'


@app.route('/getSchool', methods=['POST'])
def getSchool():
    searchProvince = request.get_json('data')['data']['province']
    with open('src/js/school.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    for province in data:
        if searchProvince == province:
            return jsonify(data[province])
    return jsonify('失败')


@app.route('/getStuInfo', methods=['POST'])
def getStuInfo():
    searSchool = request.get_json('data')['data']['school']
    table['tbody'] = []
    for school in schools:
        if school == searSchool:
            for stu in schools[school]['student']:
                table['tbody'].append(stu)
                if len(table['tbody']) > 12:
                    break
            responce = table
            print(table)
            return jsonify(responce)
    return jsonify('错误')

@app.route('/uploadImg',methods=['POST'])
def uploadImg():
    uploadFile = request.files['file']
    fileName = uploadFile.filename
    print(filename)
    # uploadFile.save('C:/Users/ASUS/Desktop/image.{}'.format())
    return jsonify('成功')


if __name__ == "__main__":
    app.run(debug=True)
