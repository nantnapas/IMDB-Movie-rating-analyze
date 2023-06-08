import scipy
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#สีกราฟ
def color_bar_chart_1():
    plt.setp(bara[0],facecolor='g')
    plt.setp(bara[1],facecolor='mediumseagreen')
    plt.setp(bara[2],facecolor='mediumaquamarine')
    plt.setp(bara[3],facecolor='lightgreen')
    plt.setp(bara[4],facecolor='mediumturquoise')
    plt.setp(bara[5],facecolor='c')
    plt.setp(bara[6],facecolor='cadetblue')
    plt.setp(bara[7],facecolor='skyblue')
    plt.setp(bara[8],facecolor='dodgerblue')
    plt.setp(bara[9],facecolor='darkblue')
    plt.setp(bara[10],facecolor='slateblue')
    plt.setp(bara[11],facecolor='rebeccapurple')
    plt.setp(bara[12],facecolor='darkviolet')
    plt.setp(bara[13],facecolor='violet')
    plt.setp(bara[14],facecolor='fuchsia')
    plt.setp(bara[15],facecolor='deeppink')

def color_bar_chart_2():
    plt.setp(bara[0],facecolor='g')
    plt.setp(bara[1],facecolor='mediumseagreen')
    plt.setp(bara[2],facecolor='mediumaquamarine')
    plt.setp(bara[3],facecolor='lightgreen')
    plt.setp(bara[4],facecolor='mediumturquoise')
    plt.setp(bara[5],facecolor='c')
    plt.setp(bara[6],facecolor='cadetblue')
    plt.setp(bara[7],facecolor='skyblue')
    plt.setp(bara[8],facecolor='dodgerblue')
    plt.setp(bara[9],facecolor='darkblue')
    plt.setp(bara[10],facecolor='slateblue')
    plt.setp(bara[11],facecolor='rebeccapurple')
    plt.setp(bara[12],facecolor='darkviolet')
    
#แสดงรายชื่อหนังของแต่ละgenre
def g(t,genrelist):
    if (t in genrelist):
        print(t,':')
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        for j in info:
            if (j==t) and (j==info[3]):
                print(info[1],end=' , ')             

    for i in info:
        genrelist=[i for i in genrelist]
    
#แสดงรายชื่อหนังของแต่ละcontent
def c(t,content_rating):
    if (t in content_rating):
        print(t,':')
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        for j in info:
            if (j==t) and (j==info[2]):
                print(info[1],end=' , ')             
   
    for i in info:
        content_rating=[i for i in content_rating]

try:
    fin=open('imdb_1000.csv','r',encoding="utf-8")
    content=fin.readlines()
    content=content[1:]


    #นับจำนวนแต่ละgenre
    set_genre=set()
    genrelist=[]  
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        set_genre.add(info[3])
        genrelist.append(info[3])
        count_set_genre=len(set_genre)
    print("Number of genre : ",count_set_genre)
      
    count=0
    genres={} 
    for genre in genrelist:
        if genre in genres:
            genres[genre]+=1
        else:
            genres[genre]=1
    print(genres)
    print() 
    
    show=input("Do you want to show a genre bar chart?[Yes/No]:")
    show=show.lower()
    
    #showgraph
    x = np.arange(1,17) 
    y=[genres['Crime'],genres['Action'],genres['Drama'],genres['Western'],
       genres['Adventure'],genres['Biography'],genres['Comedy'],genres['Animation'],
       genres['Mystery'],genres['Horror'],genres['Film-Noir'],genres['Sci-Fi'],
       genres['History'],genres['Thriller'],genres['Family'],genres['Fantasy']]  
    genre = ['Crime','Action','Drama','Western','Adventure','Biography','Comedy','Animation',
             'Mystery','Horror','Film-Noir','Sci-Fi','History','Thriller','Family','Fantasy']

    if(show=='yes'):  
        ax = plt.gca(xticks=x)
        ax.set_xticklabels(genre,rotation=60)
        bara=plt.bar(x,y)
        plt.title('Number of each genre')
        color_bar_chart_1()
        plt.show()
    print()
    
    #ค่าเฉลี่ยแต่ละgenre
    Crime=[]
    Action=[]
    Drama=[]
    Western=[]
    Adventure=[]
    Biography=[]
    Comedy=[]
    Animation=[]
    Mystery=[]
    Horror=[]
    Film_Noir=[]
    Sci_Fi=[]
    History=[]
    Thriller=[]
    Family=[]
    Fantasy=[]
   
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        if info[3]=='Crime' :
            Crime.append(info[0])
        if info[3]=='Action' :
            Action.append(info[0])
        if info[3]=='Drama' :
            Drama.append(info[0])
        if info[3]=='Western' :
            Western.append(info[0])
        if info[3]=='Adventure' :
            Adventure.append(info[0])
        if info[3]=='Biography' :
            Biography.append(info[0])
        if info[3]=='Comedy' :
            Comedy.append(info[0])
        if info[3]=='Animation' :
            Animation.append(info[0])
        if info[3]=='Mystery' :
            Mystery.append(info[0])
        if info[3]=='Horror' :
            Horror.append(info[0])
        if info[3]=='Film-Noir' :
            Film_Noir.append(info[0])
        if info[3]=='Sci-Fi' :
            Sci_Fi.append(info[0])
        if info[3]=='History' :
            History.append(info[0])
        if info[3]=='Thriller' :
            Thriller.append(info[0])
        if info[3]=='Family' :
            Family.append(info[0])
        if info[3]=='Fantasy' :
            Fantasy.append(info[0])
            
    g1=np.array(Crime,float)
    g2=np.array(Action,float)
    g3=np.array(Drama,float)
    g4=np.array(Western,float)
    g5=np.array(Adventure,float)
    g6=np.array(Biography,float)
    g7=np.array(Comedy,float)
    g8=np.array(Animation,float)
    g9=np.array(Mystery,float)
    g10=np.array(Horror,float)
    g11=np.array(Film_Noir,float)
    g12=np.array(Sci_Fi,float)
    g13=np.array(History,float)
    g14=np.array(Thriller,float)
    g15=np.array(Family,float)
    g16=np.array(Fantasy,float)
    
    mg1=g1.mean()
    mg2=g2.mean()
    mg3=g3.mean()
    mg4=g4.mean()
    mg5=g5.mean()
    mg6=g6.mean()
    mg7=g7.mean()
    mg8=g8.mean()
    mg9=g9.mean()
    mg10=g10.mean()
    mg11=g11.mean()
    mg12=g12.mean()
    mg13=g13.mean()
    mg14=g14.mean()
    mg15=g15.mean()
    mg16=g16.mean()
    
    print('Average of each genre :')
    print("Crime =",'%.2f'%mg1)
    print("Action =",'%.2f'%mg2)
    print("Drama =",'%.2f'%mg3)
    print("Western =",'%.2f'%mg4)
    print("Adventure =",'%.2f'%mg5)
    print("Biography =",'%.2f'%mg6)
    print("Comedy =",'%.2f'%mg7)
    print("Animation =",'%.2f'%mg8)
    print("Mystery =",'%.2f'%mg9)
    print("Horror =",'%.2f'%mg10)
    print("Film-Noir =",'%.2f'%mg11)
    print("Sci-Fi =",'%.2f'%mg12)
    print("History =",'%.2f'%mg13)
    print("Thriller =",'%.2f'%mg14)
    print("Family =",'%.2f'%mg15)
    print("Fantasy =",'%.2f'%mg16)     
    print()
    
    #ให้เลือกว่าจะแสดงกราฟค่าเฉลี่ยของแต่ละgenreไหม
    show=input("Do you want to show a graph of average by genre?[Yes/No]:")
    show=show.lower()
    
    x = np.arange(1,17)  
    y=[mg1,mg2,mg3,mg4,mg5,mg6,mg7,mg8,mg9,mg10,mg11,mg12,mg13,mg14,mg15,mg16]
    genre = ['Crime','Action','Drama','Western','Adventure','Biography','Comedy'
            ,'Animation','Mystery','Horror','Film-Noir','Sci-Fi','History',
            'Thriller','Family','Fantasy'] 
    
    if(show=='yes'):
        ax = plt.gca(xticks=x)
        ax.set_xticklabels(genre,rotation=60)
        plt.plot(x,y)
        plt.ylabel("average of rating")
        plt.title('average of rating of genre')
        plt.show()
    print()

    tt=input("Do you want to know title in some genre?[Yes/No]:")
    tt=tt.lower()
    while(tt=='yes'):
        t=input("What's genre do you want to know :")
        t=t.title()
        if(t==t):
            g(t,genrelist)
            print()
            con=input('Continue[Yes/No]:')
            con=con.lower()
            if(con=='no'):
                break
    print()
      
    #นับค่าแต่ละcontent
    set_content_rating=set()
    content_rating=[]
    
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        set_content_rating.add(info[2])
        content_rating.append(info[2])
        count_set_content=len(set_content_rating)      
    print("Number of content rating:",count_set_content)
        
    count=0
    ratings={}
    
    for rating in content_rating:
        if rating in ratings:
            ratings[rating]+=1
        else:
            ratings[rating]=1
    print(ratings)
    print()

    #แสดงกราฟของจำนวนแต่ละcontent
    show=input("Do you want to show content rating bar chart?[Yes/No]:")
    show=show.lower()

    #showgraph()
    x = np.arange(1,14) 
    y=[ratings['R'],ratings['PG-13'],ratings['NOT RATED'],ratings['PG'],ratings['UNRATED'],
       ratings['APPROVED'],ratings['PASSED'],ratings['G'],ratings['X'],ratings['TV-MA'],
       ratings['GP'],ratings['NC-17'],ratings['NONE']]  
    rate= ['R','PG-13','NOT RATED','PG','UNRATED','APPROVED','PASSED','G','X','TV-MA','GP','NC-17','NONE']
    
    if(show=='yes'):  
        ax = plt.gca(xticks=x)
        ax.set_xticklabels(rate,rotation=60)
        bara=plt.bar(x,y)
        color_bar_chart_2()
        plt.title('Number of each content')
        plt.show()
    print()
    
    #ค่าเฉลี่ยแต่ละcontent
    R=[]
    PG_13=[]
    NOT_RATED=[]
    PG=[]
    UNRATED=[]
    APPROVED=[]
    PASSED=[]
    G=[]
    X=[]
    TV_MA=[]
    GP=[]
    NC_17=[]
    NONE=[]
    
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        if info[2]=='R' :
            R.append(info[0])
        if info[2]=='PG-13' :
            PG_13.append(info[0])
        if info[2]=='NOT RATED' :
            NOT_RATED.append(info[0])
        if info[2]=='PG' :
            PG.append(info[0])
        if info[2]=='UNRATED' :
            UNRATED.append(info[0])
        if info[2]=='APPROVED' :
            APPROVED.append(info[0])
        if info[2]=='PASSED' :
            PASSED.append(info[0])
        if info[2]=='G' :
            G.append(info[0])
        if info[2]=='X' :
            X.append(info[0])
        if info[2]=='TV-MA' :
            TV_MA.append(info[0])
        if info[2]=='GP' :
            GP.append(info[0])
        if info[2]=='NC-17' :
            NC_17.append(info[0])
        if info[2]=='NONE' :
            NONE.append(info[0])
            
    cr1=np.array(R,float)
    cr2=np.array(PG_13,float)
    cr3=np.array(NOT_RATED,float)
    cr4=np.array(PG,float)
    cr5=np.array(UNRATED,float)
    cr6=np.array(APPROVED,float)
    cr7=np.array(PASSED,float)
    cr8=np.array(G,float)
    cr9=np.array(X,float)
    cr10=np.array(TV_MA,float)
    cr11=np.array(GP,float)
    cr12=np.array(NC_17,float)
    cr13=np.array(NONE,float)
    
    mcr1=cr1.mean()
    mcr2=cr2.mean()
    mcr3=cr3.mean()
    mcr4=cr4.mean()
    mcr5=cr5.mean()
    mcr6=cr6.mean()
    mcr7=cr7.mean()
    mcr8=cr8.mean()
    mcr9=cr9.mean()
    mcr10=cr10.mean()
    mcr11=cr11.mean()
    mcr12=cr12.mean()
    mcr13=cr13.mean()

    print("R=",'%.2f'%mcr1)
    print("PG-13=",'%.2f'%mcr2)
    print("NOT RATED=",'%.2f'%mcr3)
    print("PG=",'%.2f'%mcr4)
    print("UNRATED=",'%.2f'%mcr5)
    print("APPROVED=",'%.2f'%mcr6)
    print("PASSED=",'%.2f'%mcr7)
    print("G=",'%.2f'%mcr8)
    print("X=",'%.2f'%mcr9)
    print("TV-MA=",'%.2f'%mcr10)
    print("GP=",'%.2f'%mcr11)
    print("NC-17=",'%.2f'%mcr12)
    print("NONE=",'%.2f'%mcr13)
    print()
    

    #ให้เลือกว่าจะแสดงกราฟค่าเฉลี่ยของแต่ละcontentไหม
    show=input("Do you want to show graph of average by content rating?[Yes/No]:")
    show=show.lower()

    x = np.arange(1,14)  
    y=[mcr1,mcr2,mcr3,mcr4,mcr5,mcr6,mcr7,mcr8,mcr9,mcr10,mcr11,mcr12,mcr13]
    rate = ['R','PG-13','NOT RATED','PG','UNRATED','APPROVED','PASSED','G','X','TV-MA','GP','NC-17','NONE']
    
    if(show=='yes'):
        ax = plt.gca(xticks=x)
        ax.set_xticklabels(rate,rotation=60)
        plt.plot(x,y)
        plt.ylabel("average of rating")
        plt.title('average of rating of content')
        plt.show()
    print()
    
    cc=input("Do you want to know title in some content?[Yes/No]:")
    cc=cc.lower()
    while(cc=='yes'):
        t=input('What content do you want to know :')
        t=t.upper()
        if(t==t):
            c(t,content_rating)
            print()
            con=input('Continue[Yes/No]:')
            con=con.lower()
            if(con=='no'):
                break
    print()
    
    #Top10Movie
    top10=[]
    count10=0
    n=1
    print("Top 10 Movie:")
    for i in content:
        i=i.strip("\n")
        info=i.split(",")
        top10.append(info[0:2])
        top10=sorted(top10)
        top10.reverse()
    for j in top10:
        print(n,'.',j[1],'( Rating',j[0],')')
        count10+=1
        n+=1
        if(count10==10):
            break
    print()
    
    #หาความสัมพันธ์ระหว่างระยะเวลาของภาพยนตร์และrating
    list_rating=[]
    list_duration=[]
    for line in content:
        line=line.strip("\n")
        info=line.split(",")
        list_rating.append(info[0])
        list_duration.append(info[4])
        
    rating=np.array(list_rating,float)
    duration=np.array(list_duration,float)
    
    corr = scipy.stats.pearsonr(rating,duration)
    print("pearson correlation of duration and rating :",'%.4f'%corr[0])
    
except FileNotFoundError:
    print("can not read file")
    
finally:
    if (fin is not None):
        fin.close()