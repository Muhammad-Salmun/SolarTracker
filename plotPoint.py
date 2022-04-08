#Function to plot a point with cordinate 
def plotPoint(ax, x:float, y:float, z:float, name:str, pointColor:str = 'black'):
    ax.scatter(x,y,z,c=pointColor,s=10)
    text = str(name) + str('(') + str(x) + ', ' + str(y) + ', ' + str(z) + str(')') 
    ax.text(x, y, z, text, zdir=( 1, 1, 1))