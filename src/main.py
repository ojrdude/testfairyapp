import urllib

from flask import Flask
from flask import render_template

from fairygeneration.FairyImage import FairyImageGen
from login.loginview import LoginView
from flask_login import LoginManager, login_required
from login.user import User


app = Flask(__name__)
loginManager = LoginManager()
loginManager.init_app(app)

@loginManager.user_loader
def loadUser(userId):
    """
    Callback for logging in users.
    """
    return User.query.get(userId)

@login_required
@app.route('/restricted')
def restrictedPage():
    return render_template('restricted.html')

@app.route('/')
def newHome():
    return render_template('newhome.html')

@app.route('/login', methods=['GET'])
def login():
    loginView = LoginView()
    return loginView.loginPage()

@app.route('/login', methods=['POST'])
def performLogin():
    loginView = LoginView()
    return loginView.performLogin()

@app.route('/rootOld') # Was /
def index():
    import StringIO

    fairy = FairyImageGen.getRandomFairy()
    canvas = FairyImageGen.getFairyImage(fairy)
    canvas = FairyImageGen.addFairyNameToImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')))
    # FairyImage.createFairyTable('FAIRY_TBL')
    # FairyImage.resetDb(100)
    # return ('hello world')


@app.route('/homeOld') # Was /home
def home():
    import StringIO

    fairy = FairyImageGen.getRandomFairy()
    canvas = FairyImageGen.getFairyImage(fairy)
    canvas = FairyImageGen.addFairyNameToImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')))


@app.route('/montage20')
def montage20():
    # print 20 random fairies
    import StringIO
    from PIL import Image
    size = 1200, 2000
    canvas = FairyImageGen.getRandomFairySheet(20)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")

    contents = output.getvalue().encode('base64')
    output.close()

    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')))


@app.route('/montage100')
# print first 100 fairies
def montageal00():
    import StringIO
    from PIL import Image
    size = 1200, 10000
    canvas = FairyImageGen.getFairySheet(100)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")

    contents= output.getvalue().encode('base64')
    output.close()

    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')))


@app.route('/db')
def db():
    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies+gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')


    return render_template("dblist.html",gfairies=str(gfairies), bfairies=str(bfairies),tfairies=str(tfairies),fairyref=str(fairyref))


@app.route('/deletedbtbl')
def deletedb_TBL():
    FairyImageGen.deleteTable('FAIRY_TBL')

    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/createdbtbl')
def createdb_TBL():
    FairyImageGen.createFairyTable('FAIRY_TBL')
    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/resetdb')
def resetDb():
    FairyImageGen.resetDb(100)
    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')
                         
    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/addgfairy')
def addgfairy():
    import StringIO
    newfairy = FairyImageGen.createfairy('f')
    canvas = FairyImageGen.getFairyImage(newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')))


@app.route('/addbfairy')
def addbfairy():
    import StringIO
    newfairy = FairyImageGen.createfairy('m')
    canvas = FairyImageGen.getFairyImage(newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    gfairies = FairyImageGen.numberOfFairies('f')
    bfairies = FairyImageGen.numberOfFairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImageGen.getFairyReferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')))


@app.route('/fcard')
def fairycardimage():
    import StringIO
    fairy = FairyImageGen.getRandomFairy()
    canvas = FairyImageGen.getFairyImage(fairy)
    canvas = FairyImageGen.addFairyCharToImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')))


@app.route('/fdetailcard')
def fairydetailcardimage():
    import StringIO
    fairy = FairyImageGen.getRandomFairy()
    canvas = FairyImageGen.getFairyImage(fairy)
    canvas = FairyImageGen.addFairyCharToImage(canvas, fairy)
    canvas = FairyImageGen.addFairyDetailsToImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')))


if __name__ == '__main__':
    app.run()
