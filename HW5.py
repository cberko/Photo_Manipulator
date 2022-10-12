
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())

# separator	Main.py_1_true.txt
img, max_color_val = read_ppm_file(filename)
if operation == 1:
    empty_lst = []
    minimum = int(input())
    maximum = int(input())

    oldMin = 0
    oldMax = 255
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = ((img[i][j][k] - oldMin) / (oldMax - oldMin)) * (maximum - minimum) + minimum
                img[i][j][k]=float("{:.4f}".format(img[i][j][k]))
    img_printer(img)
    #Actually I just implemented the formula given on description in first three operation
if operation == 2:
    for k in range(3):
        toplam = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                toplam += img[i][j][k]
        aritmetik_ortalama = toplam / (len(img) * len(img))
        kare_toplamı = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                kare_toplamı += (aritmetik_ortalama - img[i][j][k]) ** 2
        standart_sapma = (kare_toplamı / (len(img) ** 2)) ** (1 / 2)
        for i in range(len(img)):
            for j in range(len(img[i])):
                img[i][j][k] = (img[i][j][k] - aritmetik_ortalama)/standart_sapma
                img[i][j][k] = float("{:.4f}".format(img[i][j][k]))
    img_printer(img)

if operation == 3:
    sum = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                sum += int(img[i][j][k])
                if k == 2:
                    img[i][j][k - 2] = sum // 3
                    img[i][j][k - 1] = sum // 3
                    img[i][j][k] = sum // 3
                    sum = 0
    img_printer(img)
if operation == 4:
    filter_txt = input()
    stride = int(input())
    filter = open(filter_txt)
    filtermatrix = []



    for line in filter:
        x=line.split()
        filtermatrix.append(x)
    #In order to create matrix from filter
    lst_new = [[[] for i in range(0, len(img) + 1 - len(filtermatrix), stride)] for j in range(0, len(img) + 1 - len(filtermatrix), stride)]
    for k in range(3):
        for i in range(0,len(img)-len(filtermatrix)+1,stride):
            for j in range(0,len(img[i])-len(filtermatrix)+1,stride):
                sum=0
                for c in range(len(filtermatrix)):
                    for l in range(len(filtermatrix[c])):
                        sum += (img[i+c][j+l][k]*float(filtermatrix[c][l]))
    

                sum=int(sum)
                if sum < 0:
                    sum=0
                if sum > 255:
                    sum = 255
                lst_new[i//stride][j//stride].append(sum)
    img_printer(lst_new)
if operation==5:
    filter_txt = input()
    stride = int(input())
    filter = open(filter_txt)
    filtermatrix = []

    for line in filter:
        x = line.split()
        filtermatrix.append(x)
    lst_new = [[[] for i in range(0, len(img) + len(filtermatrix)-1)] for j in range(0, len(img) +len(filtermatrix)-1)]
    #The list that will fill with elements of img with new i j k
    for k in range(3):
        for i in range(len(img)):
            for j in range(len(img[i])):
                lst_new[i+(len(filtermatrix)//2)][j+(len(filtermatrix)//2)].append(img[i][j][k])
    for i in range(len(lst_new)):
        for j in range(len(lst_new[i])):
            if lst_new[i][j]==[]:
                lst_new[i][j]=[0,0,0]
                #İf elements of lst_new are empty. This means that there is a frame in empty elements.
    img=lst_new
    lstnew = [[[] for i in range(0, len(img) + 1 - len(filtermatrix), stride)] for j in range(0, len(img) + 1 - len(filtermatrix), stride)]
    for k in range(3):
        for i in range(0,len(img)-len(filtermatrix)+1,stride):
            for j in range(0,len(img[i])-len(filtermatrix)+1,stride):
                sum=0
                for c in range(len(filtermatrix)):
                    for l in range(len(filtermatrix[c])):
                        sum += (img[i+c][j+l][k]*float(filtermatrix[c][l]))
                sum=int(sum)
                if sum < 0:
                    sum=0
                if sum > 255:
                    sum = 255
                lstnew[i//stride][j//stride].append(sum)
    img_printer(lstnew)
if operation == 6:
    max_differences = int(input())
    def recursive_6(lst,i,j,max_):
        if i==0 and j==len(lst)-1:
            return
        if j%2==0 and i==len(lst)-1:
            if abs(lst[i][j][0]-lst[i][j+1][0]) < max_:
                if abs(lst[i][j][1]-lst[i][j+1][1]) < max_:
                    if abs(lst[i][j][2]-lst[i][j+1][2]) < max_:
                        lst[i][j+1] = lst[i][j]
            recursive_6(lst,i,j+1,max_)
        if j%2==0 and i!=len(lst)-1:
            if abs(lst[i][j][0]-lst[i+1][j][0]) < max_:
                if abs(lst[i][j][1] - lst[i + 1][j][1]) < max_:
                    if abs(lst[i][j][2] - lst[i + 1][j][2]) < max_:
                        lst[i+1][j]=lst[i][j]
            recursive_6(lst,i+1,j,max_)
        if j%2==1 and i==0:
            if abs(lst[i][j][0]-lst[i][j+1][0])< max_:
                if abs(lst[i][j][1] - lst[i][j + 1][1]) < max_:
                    if abs(lst[i][j][2] - lst[i][j + 1][2]) < max_:
                        lst[i][j+1]=lst[i][j]
            recursive_6(lst,i,j+1,max_)
        if j % 2 ==1 and i!=0:
            if abs(lst[i][j][0]-lst[i-1][j][0]) < max_:
                if abs(lst[i][j][1] - lst[i - 1][j][1]) < max_:
                    if abs(lst[i][j][2] - lst[i - 1][j][2]) < max_:
                        lst[i-1][j]=lst[i][j]
            recursive_6(lst,i-1,j,max_)
#I image this function as a snake. The head of my snake is i=0 j=0 point and the end of the snake can be on different points.
    # But if the topic is even numbers, the end of my snake is on i=0 j=len(lst_1=

    (recursive_6(img, 0, 0, max_differences))
    img_printer(img)
if operation==7:
    max_differences = int(input())


    def recursive_7(lst, i, j, k, max_):
        if i == 0 and j == len(lst) - 1 and k ==0:
            if abs(lst[i][j][k]-lst[i][j][k+1]) < max_:
                lst[i][j][k+1]=lst[i][j][k]
            recursive_7(lst, i, j, k + 1, max_)
        if i==0 and j==0 and k==1:
            if abs(lst[i][j][k]-lst[i][j][k+1])< max_:
                lst[i][j][k+1]=lst[i][j][k]
            recursive_7(lst, i, j, k + 1, max_)
        if i == 0 and j == len(lst) - 1 and k == 2:
            return
        if k==0 and (i,j)!=(0,len(lst)-1):


            if j % 2 == 0 and i == len(lst) - 1:
                if abs(lst[i][j][k] - lst[i][j + 1][k]) < max_:
                    lst[i][j + 1][k] = lst[i][j][k]
                recursive_7(lst, i, j + 1,k,max_)
            if j % 2 == 0 and i != len(lst) - 1:
                if abs(lst[i][j][k] - lst[i + 1][j][k]) < max_:
                    lst[i + 1][j][k] = lst[i][j][k]
                recursive_7(lst, i + 1, j,k, max_)
            if j % 2 == 1 and i == 0:
                if abs(lst[i][j][k] - lst[i][j + 1][k]) < max_:
                    lst[i][j + 1][k] = lst[i][j][k]
                recursive_7(lst, i, j + 1,k,max_)
            if j % 2 == 1 and i != 0:
                if abs(lst[i][j][k] - lst[i - 1][j][k]) < max_:
                    lst[i - 1][j][k] = lst[i][j][k]
                recursive_7(lst, i - 1, j,k, max_)
        if k == 1 and (i, j) != (0, 0):
            if j%2==1 and i!=len(lst)-1:
                if abs(lst[i][j][k]-lst[i+1][j][k]) < max_:
                    lst[i+1][j][k]=lst[i][j][k]
                recursive_7(lst,i+1,j,k,max_)
            if j%2==1 and i==len(lst)-1:
                if abs(lst[i][j][k]-lst[i][j-1][k]) < max_:
                    lst[i][j-1][k]=lst[i][j][k]
                recursive_7(lst, i ,j-1, k, max_)
            if j%2==0 and i!=0:
                if abs(lst[i][j][k]-lst[i-1][j][k])<max_:
                    lst[i-1][j][k] = lst[i][j][k]
                recursive_7(lst,i-1,j,k,max_)
            if j%2==0 and i==0:
                if abs(lst[i][j][k]-lst[i][j-1][k])<max_:
                    lst[i][j-1][k]=lst[i][j][k]
                recursive_7(lst,i,j-1,k,max_)
        if k==2 and (i,j)!=(0,len(lst)-1):
            if j % 2 == 0 and i == len(lst) - 1:
                if abs(lst[i][j][k] - lst[i][j + 1][k]) < max_:
                    lst[i][j + 1][k] = lst[i][j][k]
                recursive_7(lst, i, j + 1,k,max_)
            if j % 2 == 0 and i != len(lst) - 1:
                if abs(lst[i][j][k] - lst[i + 1][j][k]) < max_:
                    lst[i + 1][j][k] = lst[i][j][k]
                recursive_7(lst, i + 1, j,k, max_)
            if j % 2 == 1 and i == 0:
                if abs(lst[i][j][k] - lst[i][j + 1][k]) < max_:
                    lst[i][j + 1][k] = lst[i][j][k]
                recursive_7(lst, i, j + 1,k,max_)
            if j % 2 == 1 and i != 0:
                if abs(lst[i][j][k] - lst[i - 1][j][k]) < max_:
                    lst[i - 1][j][k] = lst[i][j][k]
                recursive_7(lst, i - 1, j,k, max_)
    #Actualy this operation is alike op6 I again image this operation as a snake.
    # but in here, my head and end can be different according to rgb values
    recursive_7(img, 0, 0, 0, max_differences)
    img_printer(img)



































































# separator	Main.py_2_false.txt
