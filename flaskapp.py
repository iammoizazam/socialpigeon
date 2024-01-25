from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify, send_file,make_response
import os
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'convex_application'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'convexsql123'
# app.config['MYSQL_DB'] = 'influencer'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'socialpigeon'
app.config['MYSQL_PASSWORD'] = 'SOcial$5432#'
app.config['MYSQL_DB'] = 'socialpigeon'
app.config['UPLOAD_FOLDER'] ="/var/www/html/socialpegion/static/userImages"
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

# app.config['MYSQL_HOST'] = '10.100.50.44'
# app.config['MYSQL_USER'] = 'socialpigeon'
# app.config['MYSQL_PASSWORD'] = 'SOcial$5432#'
# app.config['MYSQL_DB'] = 'socialpigeon'

app.config['UPLOADED_PATH'] = os.path.join(app.root_path, 'upload')

mysql = MySQL(app)


def insertRecord(Fname,Lname,email,phone,add1,add2,website,category,youtubelink,youtubefollowers,youtubevideo,youtubeshorts,facebooklink,facebookfollowers,facebookpost,facebookvideo,facebookstory,instagramlink,instagramfollowers,instagrampost ,instagramvideo,instagramstory,tiktoklink,tiktokfollowers,tiktokcharges,LinkedInlink,LinkedInfollowers,LinkedIncharges,twitterlink,twitterfollowers,twitterpost,twittervideo,BrandSponsor,LikeUsKnow,ageRange,storeraid ):
    cursor = mysql.connection.cursor()
    res=cursor.execute("select * from influencers where Email ='"+email+"' or PhoneNumber= '"+phone+"'")

    if (res == 0):
        cursor.execute(
            "INSERT INTO influencers (FirstName, LastName, Email,Category,PhoneNumber,Address1,Address2,FollowersAgeRange,RecentBrandSponsorshipWork,AnythingLikeUsToKnow) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (Fname, Lname, email, category, phone, add1, add2, ageRange, BrandSponsor, LikeUsKnow))
        cursor.execute("select max(InfluencerID) from influencers")
        influencerID = cursor.fetchone()
        cursor.execute(
            "INSERT INTO influencersocialmedia (InfluencerID, WebsiteLink,YoutubeLink,FacebookLink,InstagramLink,TiktokLink,LinkedInLink,TwitterLink,YouTubeFollowers,FacebookFollowers,InstagramFollowers,TiktokFollowers,LinkedInFollowers,TwitterFollowers) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (influencerID, website, youtubelink, facebooklink, instagramlink, tiktoklink, LinkedInlink, twitterlink,
             youtubefollowers, facebookfollowers, instagramfollowers, tiktokfollowers, LinkedInfollowers,
             twitterfollowers))
        cursor.execute("select max(InfluSocialMdaID) from influencersocialmedia")
        socialm = cursor.fetchone()
        youtubecheck = None
        facebookcheck = None
        instagramcheck = None
        tiktokcheck = None
        LinkedIncheck = None
        twittercheck = None

        if youtubelink != '':
            youtubecheck = '0'

        if facebooklink != '':
            facebookcheck = '0'

        if instagramlink != '':
            instagramcheck = '0'

        if tiktoklink != '':
            tiktokcheck = '0'

        if LinkedInlink != '':
            LinkedIncheck = '0'

        if twitterlink != '':
            twittercheck = '0'

        cursor.execute(
            "INSERT INTO paritycheck (InfluSocialMdaID,YoutubeCheck,FacebookCheck,InstagramCheck,TiktokCheck,LinkedinCheck,TwitterCheck) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (socialm, youtubecheck, facebookcheck, instagramcheck, tiktokcheck, LinkedIncheck, twittercheck))
        cursor.execute(
            "INSERT INTO influencerscharges (InfluencerID,OnGroundActivityCharges,YoutubeVideoCharge,YoutubeShortCharge,FacebookPostCharge,FacebookVideoCharge,FacebookStoryCharge,InstagramPostCharge,InstagramVideoCharge,InstagramStoryCharge,TiktokCharge,LinkedInCharge,TwitterPostCharge,TwitterVideoCharge) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (influencerID, storeraid, youtubevideo, youtubeshorts, facebookpost, facebookvideo, facebookstory,
             instagrampost, instagramvideo, instagramstory, tiktokcharges, LinkedIncharges, twitterpost, twittervideo))

    mysql.connection.commit()
    cursor.close()
    return res

@app.route('/formsubmit', methods=['POST','GET'])
def formsubmit():
    if request.method == "POST":
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        email = request.form['email']
        phone = request.form['phone']
        add1 = request.form['add1']
        add2 = request.form['add2']
        website = request.form['website']
        category = request.form.getlist('cat')
        youtubelink = request.form['youtubeLink']
        youtubefollowers = request.form['youtubeFollowers']
        youtubevideo = request.form['youtubeVideo']
        youtubeshorts = request.form['youtubeShorts']
        facebooklink = request.form['facebookLink']
        facebookfollowers = request.form['facebookFollowers']
        facebookpost = request.form['facebookPost']
        facebookvideo = request.form['facebookVideo']
        facebookstory = request.form['facebookStory']
        instagramlink = request.form['instagramLink']
        instagramfollowers = request.form['instagramFollowers']
        instagrampost = request.form['instagramPost']
        instagramvideo = request.form['instagramVideo']
        instagramstory = request.form['instagramStory']
        tiktoklink = request.form['tiktokLink']
        tiktokfollowers = request.form['tiktokFollowers']
        tiktokcharges = request.form['tiktokCharges']
        LinkedInlink = request.form['LinkedInLink']
        LinkedInfollowers = request.form['LinkedInFollowers']
        LinkedIncharges = request.form['LinkedInCharges']
        twitterlink = request.form['twitterLink']
        twitterfollowers = request.form['twitterFollowers']
        twitterpost = request.form['twitterPost']
        twittervideo = request.form['twitterVideo']
        BrandSponsor = request.form['BrandSponsor']
        LikeUsKnow = request.form['LikeUsKnow']
        ageRange = request.form['ageRange']
        storeraid = request.form['storeraid']
        temp = ''
        for i in category:
            temp = temp + "," + i
        category = temp[1:]
        res = insertRecord(Fname, Lname, email, phone, add1, add2, website, category, youtubelink, youtubefollowers,
                           youtubevideo, youtubeshorts, facebooklink, facebookfollowers, facebookpost, facebookvideo,
                           facebookstory, instagramlink, instagramfollowers, instagrampost, instagramvideo,
                           instagramstory, tiktoklink, tiktokfollowers, tiktokcharges, LinkedInlink, LinkedInfollowers,
                           LinkedIncharges, twitterlink, twitterfollowers, twitterpost, twittervideo, BrandSponsor,
                           LikeUsKnow, ageRange, storeraid)
        if (int(res) == 0):
            print(int(res))
            response_data = jsonify({'success': True, 'code': 200})
            resp = make_response(response_data)
            return redirect(url_for('success'))
        elif (int(res) > 0):
            print(int(res))
            response_data = jsonify({'success': False, 'code': 400})
            resp = make_response(response_data)
            return redirect(url_for('fail'))
    else:
        return 'ok'


@app.route("/privacypolicy",methods=['GET','POST'])
def privacypolicy():
    if request.method == "GET":
       return render_template('privacypolicy.html')


@app.route("/termandcondition",methods=['GET','POST'])
def term():
    if request.method == "GET":
       return render_template('terms.html')

@app.route("/success", methods=['GET', 'POST'])
def success():
    if request.method == "GET":
        print("in GET")
        return render_template('success.html')
    else:
        print("in POST")
        return render_template('success.html')

@app.route("/fail", methods=['GET', 'POST'])
def fail():
    if request.method == "GET":
        print("in GET")
        return render_template('fail.html')
    else:
        print("in POST")
        return render_template('fail.html')



@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print("in GET")
        return render_template('index.html')
    else:
        print("in POST")
        return render_template('index.html')

@app.route('/formsubmitBrand', methods=['POST','GET'])
def formsubmitBrand():
    if request.method == "POST":
        Bname = request.form['Bname']
        Bemail = request.form['Bemail']
        phone = request.form['phone']
        add1 = request.form['add1']
        add2 = request.form['add2']
        propic = request.files['propic']
        filename = secure_filename(propic.filename)
        temp= filename.split(".")
        temp2= Bemail.split(".")
        filename= temp2[0]+'.'+temp[-1]
        print(filename)
        res = insertBrand(Bname,Bemail,phone,add1,add2,propic,filename)

        if (int(res) == 0):
            print(int(res))
            response_data = jsonify({'success': True, 'code': 200})
            resp = make_response(response_data)
            return redirect(url_for('success'))

        elif (int(res) > 0):
            print(int(res))
            response_data = jsonify({'success': False, 'code': 400})
            resp = make_response(response_data)
            return redirect(url_for('fail'))
    else:
        return 'ok'

def insertBrand(Bname,Bemail,phone,add1,add2,propic,filename):
    cursor = mysql.connection.cursor()
    res = cursor.execute("select * from brands where Email ='" + Bemail + "' or Phone= '" + phone + "'")
    print(res)
    if (res == 0):
        cursor.execute(
            "INSERT INTO brands (BrandName,Phone, Email,Address1,Address2,Profilepic) VALUES (%s,%s,%s,%s,%s,%s)",
            (Bname,phone,Bemail,add1,add2,filename))
        propic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    mysql.connection.commit()
    cursor.close()
    return res











@app.route("/influencer",methods=['GET','POST'])
def influencer():
    if request.method == "GET":
        print("in GET")
        return render_template('influencers.html')

    else:
        print("in POST")
        return render_template('influencers.html')




@app.route("/Brands",methods=['GET','POST'])
def Brands():
    if request.method == "GET":
        print("in GET")
        return render_template('Brands.html')

    else:
        print("in POST")
        return render_template('Brands.html')

    # return "Hello World!"






if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",threaded=True)
