import matplotlib.pyplot as plt

questions = (
"Title:",
"X side title:",
"Y side title:",
"Table size:",
"Line:",
"X:",
"Y:",
    )
def ask(index,atype=str,repeat='False'):
    if repeat=='True':
        list = []
        input("\nIf you would like to continue press <Enter> and write one by one.To end write 'q'.\n"+questions[index])
        while True:
            try:
                list.append(atype(input()))
            except:
                return list
    elif type(repeat)=='int':
        list = []
        input(questions[index]+'\nNote:Write one by one.')
        for i in range(repeat):
            list.append(input())
    elif repeat=='False':
        a = input(questions[index])
        return a


def table_create(x,y,title='',x_label='',y_label='',size=(8,6),line='k-'):
    plt.figure(figsize=size)
    plt.plot(x,y,line)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)




if __name__ == '__main__':
    table_create(title=ask(0),x_label=ask(1),y_label=ask(2),size=ask(3,repeat=2),line=ask(4),x=ask(5,float,'True'),y=ask(6,float,'True'))
    print("\n\n\nCreating...\n\n\n")
    plt.show()



