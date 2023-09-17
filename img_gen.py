import numpy as np
import matplotlib.pyplot as plt

def gen_simple_eq_img(args=[1,1], type="?", name="Untitled"):
    # initialization
    fig = plt.figure()
    spl = fig.add_subplot(2,1,1)
    text="UNDEFINED EQUASION TYPE"
    if type=="+":
        text="x + "+str(args[0])+" = "+str(args[1])
    elif type=="-":
        text="x - "+str(args[0])+" = "+str(args[1])
    elif type=="*":
        text="x * "+str(args[0])+" = "+str(args[1])
    elif type=="/":
        text=str(args[0])+" / x = "+str(args[1])
    spl.text(0.22,0.4,text, fontsize=24)
    # saving the figure
    extent = spl.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig("{a}.png".format(a=name), bbox_inches=extent)
    pass
    # closing the figure to save some memory
    plt.close()

def gen_square_eq_img(args=[1,1,1], name="Untitled"):
    # initialization
    fig = plt.figure()
    spl = fig.add_subplot(2,1,1)
    spl.text(0.22,0.4,str(args[0])+"x² + "+str(args[1])+"x + "+str(args[2])+" = 0", fontsize=24)
    # saving the figure
    extent = spl.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig("{a}.png".format(a=name), bbox_inches=extent)
    pass
    # closing the figure to save some memory
    plt.close()

def gen_matrix_img(matrix=[[1,2,3],[3,4,5],[5,6,7]], name="Untitled"):
    # initialization
    fig = plt.figure()
    spl = fig.add_subplot(2,1,1)

    # rendering the text from
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tmp = matrix[i][j]
            spl.text(j+0.5, len(matrix)-i-0.5, str(tmp), va="center", ha="center")

    # setting limits to the table
    spl.set_xlim(0,len(matrix[0]))
    spl.set_ylim(0,len(matrix))
    spl.set_xticks(np.arange(len(matrix[0])))
    spl.set_yticks(np.arange(len(matrix)))
    spl.grid()

    # cropping the figure
    extent = spl.get_window_extent().transformed(fig.dpi_scale_trans.inverted())

    # saving the figure
    fig.savefig("{a}.png".format(a=name), bbox_inches=extent)

    # closing the figure to save some memory
    plt.close()


if __name__=="__main__":
    gen_square_eq_img([1,2,3])