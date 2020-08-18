# encoding: utf-8
from Tkinter import*
import tkMessageBox
import paramiko
import random
import sys
import os
import time

root= Tk()
root.geometry("800x480+1+1")
root.title("feira")
root.configure(background='black')
root.overrideredirect(False)
root.resizable(0,0)


#======================Imagens==================================
coca=PhotoImage(file="7894900011517.png")
ruffles=PhotoImage(file="7892840127411.png")
suflair=PhotoImage(file="7891000414002.png")
fandandos=PhotoImage(file="038000849824.png")
toddy=PhotoImage(file="7894321711478.png")

#====================== Frame do topo ==================================================

topo = Frame (root, width=800 , height=90 , bd=4 , relief ="groove")
topo.pack(side=TOP)

nome= Label(topo,font=('arial',32,'normal'),text="SELF-CHECKOUT",bd=8,width=30)
nome.place(x=0 , y=0)

#====================== Frame da esquerda ==================================================

esquerda = Frame (root, width=600 , height=650 , bd=3 , relief ="groove")
esquerda.pack(side=LEFT)

#====================== Frame da direita ==================================================


def checkout():
	resultado=tkMessageBox.askyesno("Checkout","Deseja fazer checkout?")
	if resultado==True:


		master=open("enviar.txt","w")
		master.write("a\nb\nc\nd\ne\nf\ng\nh\nsenh")
		master.close()

		try:
			enviar1o=open("1.txt","r")
			enviar1=enviar1o.readlines()
			enviar1o.close()
			with open("enviar.txt","r") as f:
				newline=[]
				for word in f.readlines():        
					newline.append(word.replace("a",enviar1[0]))

			with open("enviar.txt","w") as f:
				for line in newline:
					f.writelines(line)

		except IndexError:
			pass

		try:
			enviar2o=open("2.txt","r")
			enviar2=enviar2o.readlines()
			enviar2o.close()
			with open("enviar.txt","r") as f:
				newline=[]
				for word in f.readlines():        
					newline.append(word.replace("b",enviar2[0]))

			with open("enviar.txt","w") as f:
				for line in newline:
					f.writelines(line)

		except IndexError:
			pass


		try:
			enviar3o=open("3.txt","r")
			enviar3=enviar3o.readlines()
			enviar3o.close()
			with open("enviar.txt","r") as f:
				newline=[]
				for word in f.readlines():        
					newline.append(word.replace("c",enviar3[0]))

			with open("enviar.txt","w") as f:
				for line in newline:
					f.writelines(line)

		except IndexError:
			pass



		try:
			enviar4o=open("4.txt","r")
			enviar4=enviar4o.readlines()
			enviar4o.close()
			with open("enviar.txt","r") as f:
				newline=[]
				for word in f.readlines():        
					newline.append(word.replace("d",enviar4[0]))

			with open("enviar.txt","w") as f:
				for line in newline:
					f.writelines(line)

		except IndexError:
			pass



		senha=random.randint(9,1001)
		print(senha)

		with open("enviar.txt","r") as f:
			newline=[]
			for word in f.readlines():        
				newline.append(word.replace("senh","%s"%(senha)))

		with open("enviar.txt","w") as f:
			for line in newline:
				f.writelines(line)



		#s = paramiko.SSHClient()
		#s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		#s.connect("10.67.127.188",22,username="renan",password="sensacional",timeout=4)

		#sftp = s.open_sftp()
		#sftp.put('/home/pi/Desktop/feira/enviar.txt', '/home/renan/feira/enviar.txt')

		tkMessageBox.showinfo("Checkout","Sua senha:%s"%(senha))

		os.execl("restart.sh","")


	else:
		pass



direita = Frame (root, width=200 , height=650 , bd=3 , relief ="groove")
direita.pack(side=RIGHT)

total=StringVar()
total.set("")

totall=Label(direita,font=('arial',18,'normal'), text="Total:")
rtotal=Label(direita,font=('arial',18,'normal'),textvariable=total)
totall.place(x=0,y=275)
rtotal.place(x=70,y=275)

titem=Label(direita,font=('arial',32,'normal'), text="Item:")
titem.place(x=0,y=0)

ultimovalor=StringVar()
ultimovalor.set("")

vitem=Label(direita,font=('arial',15,'normal'), text="Valor:")
rvitem=Label(direita,font=('arial',15,'normal'),textvariable=ultimovalor,width=0,height=0)
vitem.place(x=0,y=250)
rvitem.place(x=60,y=250)


direita.pack_propagate(False) 

checkout= Button(direita, width=20,height=3,bg="green",fg="black",text="Checkout",command=checkout)
checkout.place(x=3 , y=318)


#==============================Variaveis com botoes=================


#===========================Produto 1=============================
while True:

	file1 = open("1.txt", "w")
	numero=raw_input()
	file1.write(numero)
	file1.close()

	f1=open("1.txt","r")
	lines1=f1.readlines()
	f1.close

	banco= open("bancodedados.txt", "r")
	produto=banco.readlines()



	if lines1[0]+'\n'==produto[1]:
		nome1=produto[0]
		fandangosl=Label(direita, width=190 , height=200,image=fandandos)
		fandangosl.place(x=1,y=50)
		aultimovalor=produto[2].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal=produto[2].rstrip()
		total.set("R$"+atotal)
		root.update_idletasks()


	if lines1[0]+'\n'==produto[4]:
		nome1=produto[3]
		toddyl=Label(direita, width=190 , height=200,image=toddy)
		toddyl.place(x=1,y=50)
		aultimovalor=produto[5].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal=produto[5].rstrip()
		total.set("R$"+atotal)
		root.update_idletasks()
	
	if lines1[0]+'\n'==produto[7]:
		nome1=produto[6]
		cocal=Label(direita, width=190 , height=200,image=coca)
		cocal.place(x=1,y=50)
		aultimovalor=produto[8].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal=produto[8].rstrip()
		total.set("R$"+atotal)
		root.update_idletasks()

	if lines1[0]+'\n'==produto[10]:
		nome1=produto[9]
		suflairl=Label(direita, width=190 , height=200,image=suflair)
		suflairl.place(x=1,y=50)
		aultimovalor=produto[11].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal=produto[11].rstrip()
		total.set("R$"+atotal)
		root.update_idletasks()

	if lines1[0]+'\n'==produto[13]:
		nome1=produto[12]
		rufflesl=Label(direita, width=190 , height=200,image=ruffles)
		rufflesl.place(x=1,y=50)
		aultimovalor=produto[14].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal=produto[14].rstrip()
		total.set("R$"+atotal)
		root.update_idletasks()


	def ex1():
		item1.destroy()

		new=total.get().replace("R$","")

		newnew=new.replace(",",".")

		atotalsv=atotal.replace(",",".")

		totalmenos=str(float(newnew)-float(atotalsv)).replace(".",",")

		total.set("R$"+totalmenos)
		root.update_idletasks()

		test1=open("1.txt","w")
		test1.write("a")
		test1.close()

		i1=open("1.txt", "w")
		numero1=raw_input()
		i1.write(numero1)
		i1.close()

		r1=open("1.txt","r")
		lines1s=r1.readlines()
		r1.close
		
		if lines1s[0]+'\n'==produto[1]:
			nome1s=produto[0]
			fandangosl=Label(direita, width=190 , height=200,image=fandandos)
			fandangosl.place(x=1,y=50)
			aultimovalor=produto[2].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new1a=total.get().replace("R$","")
			newnew1a=new1a.replace(",",".")
			totaltrab=str(float(newnew1a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()


		if lines1s[0]+'\n'==produto[4]:
			nome1s=produto[3]
			toddyl=Label(direita, width=190 , height=200,image=toddy)
			toddyl.place(x=1,y=50)
			aultimovalor=produto[5].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new1a=total.get().replace("R$","")
			newnew1a=new1a.replace(",",".")
			totaltrab=str(float(newnew1a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()
	
		if lines1s[0]+'\n'==produto[7]:
			nome1s=produto[6]
			cocal=Label(direita, width=190 , height=200,image=coca)
			cocal.place(x=1,y=50)
			aultimovalor=produto[8].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new1a=total.get().replace("R$","")
			newnew1a=new1a.replace(",",".")
			totaltrab=str(float(newnew1a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines1s[0]+'\n'==produto[10]:
			nome1s=produto[9]
			suflairl=Label(direita, width=190 , height=200,image=suflair)
			suflairl.place(x=1,y=50)
			aultimovalor=produto[11].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new1a=total.get().replace("R$","")
			newnew1a=new1a.replace(",",".")
			totaltrab=str(float(newnew1a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines1s[0]+'\n'==produto[13]:
			nome1s=produto[12]
			rufflesl=Label(direita, width=190 , height=200,image=ruffles)
			rufflesl.place(x=1,y=50)
			aultimovalor=produto[14].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new1a=total.get().replace("R$","")
			newnew1a=new1a.replace(",",".")
			totaltrab=str(float(newnew1a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()



		item1r=Button	(esquerda,width=33,height=4,bg="white",fg="black",text=nome1s,command=ex1)
		item1r.place(x=1, y=0)




	item1= Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome1,command=ex1)
	item1.place(x=1, y=0)

	break

#=====================================Produto 2===============================
while True:

	file2 = open("2.txt", "w")
	numero2=raw_input()
	file2.write(numero2)
	file2.close()

	f2=open("2.txt","r")
	lines2=f2.readlines()
	f2.close

	banco= open("bancodedados.txt", "r")
	produto=banco.readlines()


	if lines2[0]+'\n'==produto[1]:
		nome2=produto[0]
		fandangosl=Label(direita, width=190 , height=200,image=fandandos)
		fandangosl.place(x=1,y=50)
		aultimovalor=produto[2].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal2=produto[2].rstrip()
		new1=total.get().replace("R$","")
		newnew1=new1.replace(",",".")
		totaltrab=str(float(newnew1)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()


	if lines2[0]+'\n'==produto[4]:
		nome2=produto[3]
		toddyl=Label(direita, width=190 , height=200,image=toddy)
		toddyl.place(x=1,y=50)
		aultimovalor=produto[5].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal2=produto[5].rstrip()
		new2=total.get().replace("R$","")
		newnew2=new2.replace(",",".")
		print(newnew2)
		totaltrab=str(float(newnew2)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()
	
	if lines2[0]+'\n'==produto[7]:
		nome2=produto[6]
		cocal=Label(direita, width=190 , height=200,image=coca)
		cocal.place(x=1,y=50)
		aultimovalor=produto[8].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal2=produto[8].rstrip()
		totalmasterf=atotal.replace(",", ".")
		totalmaster2f=atotal2.replace(",", ".")
		totalmasterfo=float(totalmasterf)+float(totalmaster2f)
		totalgenuino=str(totalmasterfo)
		total.set("R$"+totalgenuino.replace(".", ","))
		root.update_idletasks()

	if lines2[0]+'\n'==produto[10]:
		nome2=produto[9]
		suflairl=Label(direita, width=190 , height=200,image=suflair)
		suflairl.place(x=1,y=50)
		aultimovalor=produto[11].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal2=produto[11].rstrip()
		totalmasterf=atotal.replace(",", ".")
		totalmaster2f=atotal2.replace(",", ".")
		totalmasterfo=float(totalmasterf)+float(totalmaster2f)
		totalgenuino=str(totalmasterfo)
		total.set("R$"+totalgenuino.replace(".", ","))
		root.update_idletasks()

	if lines2[0]+'\n'==produto[13]:
		nome2=produto[12]
		rufflesl=Label(direita, width=190 , height=200,image=ruffles)
		rufflesl.place(x=1,y=50)
		aultimovalor=produto[14].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		atotal2=produto[14].rstrip()
		totalmasterf=atotal.replace(",", ".")
		totalmaster2f=atotal2.replace(",", ".")
		totalmasterfo=float(totalmasterf)+float(totalmaster2f)
		totalgenuino=str(totalmasterfo)
		total.set("R$"+totalgenuino.replace(".", ","))
		root.update_idletasks()


	def ex2():
		item2.destroy()

		new=total.get().replace("R$","")

		newnew=new.replace(",",".")

		atotalsv=atotal2.replace(",",".")

		totalmenos=str(float(newnew)-float(atotalsv)).replace(".",",")

		total.set("R$"+totalmenos)
		root.update_idletasks()


		i2=open("2.txt", "w")
		numero3=raw_input()
		i2.write(numero3)
		i2.close()

		r2=open("2.txt","r")
		lines2s=r2.readlines()
		r2.close
		
		if lines2s[0]+'\n'==produto[1]:
			nome2s=produto[0]
			fandangosl=Label(direita, width=190 , height=200,image=fandandos)
			fandangosl.place(x=1,y=50)
			aultimovalor=produto[2].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			print(total.get())
			new2a=total.get().replace("R$","")
			newnew2a=new2a.replace(",",".")
			totaltrab=str(float(newnew2a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()


		if lines2s[0]+'\n'==produto[4]:
			nome2s=produto[3]
			toddyl=Label(direita, width=190 , height=200,image=toddy)
			toddyl.place(x=1,y=50)
			aultimovalor=produto[5].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			atotal=produto[5].rstrip()
			total.set("R$"+atotal)
			new2a=total.get().replace("R$","")
			newnew2a=new2a.replace(",",".")
			totaltrab=str(float(newnew2a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()
	
		if lines2s[0]+'\n'==produto[7]:
			nome2s=produto[6]
			cocal=Label(direita, width=190 , height=200,image=coca)
			cocal.place(x=1,y=50)
			aultimovalor=produto[8].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new2a=total.get().replace("R$","")
			newnew2a=new2a.replace(",",".")
			totaltrab=str(float(newnew2a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines2s[0]+'\n'==produto[10]:
			nome2s=produto[9]
			suflairl=Label(direita, width=190 , height=200,image=suflair)
			suflairl.place(x=1,y=50)
			aultimovalor=produto[11].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new2a=total.get().replace("R$","")
			newnew2a=new2a.replace(",",".")
			totaltrab=str(float(newnew2a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines2s[0]+'\n'==produto[13]:
			nome2s=produto[12]
			rufflesl=Label(direita, width=190 , height=200,image=ruffles)
			rufflesl.place(x=1,y=50)
			aultimovalor=produto[14].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new2a=total.get().replace("R$","")
			newnew2a=new2a.replace(",",".")
			totaltrab=str(float(newnew2a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()



		item2r=Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome2s,command=ex2)
		item2r.place(x=1, y=100)




	item2= Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome2,command=ex2)
	item2.place(x=1, y=100)


	break

#=====================================Produto 3===============================
while True:

	file3 = open("3.txt", "w")
	numero3=raw_input()
	file3.write(numero3)
	file3.close()

	f3=open("3.txt","r")
	lines3=f3.readlines()
	f3.close

	banco= open("bancodedados.txt", "r")
	produto=banco.readlines()


	if lines3[0]+'\n'==produto[1]:
		nome3=produto[0]
		fandangosl=Label(direita, width=190 , height=200,image=fandandos)
		fandangosl.place(x=1,y=50)
		aultimovalor=produto[2].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new3a=total.get().replace("R$","")
		newnew3a=new3a.replace(",",".")
		totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()


	if lines3[0]+'\n'==produto[4]:
		nome3=produto[3]
		toddyl=Label(direita, width=190 , height=200,image=toddy)
		toddyl.place(x=1,y=50)
		aultimovalor=produto[5].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new3a=total.get().replace("R$","")
		newnew3a=new3a.replace(",",".")
		totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()
	
	if lines3[0]+'\n'==produto[7]:
		nome3=produto[6]
		cocal=Label(direita, width=190 , height=200,image=coca)
		cocal.place(x=1,y=50)
		aultimovalor=produto[8].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new3a=total.get().replace("R$","")
		newnew3a=new3a.replace(",",".")
		totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()

	if lines3[0]+'\n'==produto[10]:
		nome3=produto[9]
		suflairl=Label(direita, width=190 , height=200,image=suflair)
		suflairl.place(x=1,y=50)
		aultimovalor=produto[11].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new3a=total.get().replace("R$","")
		newnew3a=new3a.replace(",",".")
		totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()

	if lines3[0]+'\n'==produto[13]:
		nome3=produto[12]
		rufflesl=Label(direita, width=190 , height=200,image=ruffles)
		rufflesl.place(x=1,y=50)
		aultimovalor=produto[14].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new3a=total.get().replace("R$","")
		newnew3a=new3a.replace(",",".")
		totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()


	def ex3():
		item3.destroy()

		new=total.get().replace("R$","")

		newnew=new.replace(",",".")

		atotalsv=atotal2.replace(",",".")

		totalmenos=str(float(newnew)-float(atotalsv)).replace(".",",")

		total.set("R$"+totalmenos)
		root.update_idletasks()


		i3=open("3.txt", "w")
		numero4=raw_input()
		i3.write(numero4)
		i3.close()

		r3=open("3.txt","r")
		lines3s=r3.readlines()
		r3.close
		
		if lines3s[0]+'\n'==produto[1]:
			nome3s=produto[0]
			fandangosl=Label(direita, width=190 , height=200,image=fandandos)
			fandangosl.place(x=1,y=50)
			aultimovalor=produto[2].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			print(total.get())
			new3a=total.get().replace("R$","")
			newnew3a=new3a.replace(",",".")
			totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()


		if lines3s[0]+'\n'==produto[4]:
			nome3s=produto[3]
			toddyl=Label(direita, width=190 , height=200,image=toddy)
			toddyl.place(x=1,y=50)
			aultimovalor=produto[5].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new3a=total.get().replace("R$","")
			newnew3a=new3a.replace(",",".")
			totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()
	
		if lines3s[0]+'\n'==produto[7]:
			nome3s=produto[6]
			cocal=Label(direita, width=190 , height=200,image=coca)
			cocal.place(x=1,y=50)
			aultimovalor=produto[8].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new3a=total.get().replace("R$","")
			newnew3a=new3a.replace(",",".")
			totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines3s[0]+'\n'==produto[10]:
			nome3s=produto[9]
			suflairl=Label(direita, width=190 , height=200,image=suflair)
			suflairl.place(x=1,y=50)
			aultimovalor=produto[11].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new3a=total.get().replace("R$","")
			newnew3a=new3a.replace(",",".")
			totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines3s[0]+'\n'==produto[13]:
			nome3s=produto[12]
			rufflesl=Label(direita, width=190 , height=200,image=ruffles)
			rufflesl.place(x=1,y=50)
			aultimovalor=produto[14].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new3a=total.get().replace("R$","")
			newnew3a=new3a.replace(",",".")
			totaltrab=str(float(newnew3a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()



		item3r=Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome3s,command=ex3)
		item3r.place(x=1, y=200)




	item3= Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome3,command=ex3)
	item3.place(x=1, y=200)


	break

#=====================================Produto 4===============================
while True:

	file4 = open("4.txt", "w")
	numero4=raw_input()
	file4.write(numero4)
	file4.close()

	f4=open("4.txt","r")
	lines4=f4.readlines()
	f4.close

	banco= open("bancodedados.txt", "r")
	produto=banco.readlines()


	if lines4[0]+'\n'==produto[1]:
		nome4=produto[0]
		fandangosl=Label(direita, width=190 , height=200,image=fandandos)
		fandangosl.place(x=1,y=50)
		aultimovalor=produto[2].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new4=total.get().replace("R$","")
		newnew4=new4.replace(",",".")
		totaltrab=str(float(newnew4)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()


	if lines4[0]+'\n'==produto[4]:
		nome4=produto[3]
		toddyl=Label(direita, width=190 , height=200,image=toddy)
		toddyl.place(x=1,y=50)
		aultimovalor=produto[5].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new4=total.get().replace("R$","")
		newnew4=new4.replace(",",".")
		totaltrab=str(float(newnew4)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()
	
	if lines4[0]+'\n'==produto[7]:
		nome4=produto[6]
		cocal=Label(direita, width=190 , height=200,image=coca)
		cocal.place(x=1,y=50)
		aultimovalor=produto[8].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new4=total.get().replace("R$","")
		newnew4=new4.replace(",",".")
		totaltrab=str(float(newnew4)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()

	if lines4[0]+'\n'==produto[10]:
		nome4=produto[9]
		suflairl=Label(direita, width=190 , height=200,image=suflair)
		suflairl.place(x=1,y=50)
		aultimovalor=produto[11].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new4=total.get().replace("R$","")
		newnew4=new4.replace(",",".")
		totaltrab=str(float(newnew4)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()

	if lines4[0]+'\n'==produto[13]:
		nome4=produto[12]
		rufflesl=Label(direita, width=190 , height=200,image=ruffles)
		rufflesl.place(x=1,y=50)
		aultimovalor=produto[14].rstrip()
		ultimovalor.set("R$"+aultimovalor)
		print(ultimovalor)
		new4=total.get().replace("R$","")
		newnew4=new4.replace(",",".")
		totaltrab=str(float(newnew4)+float(aultimovalor.replace(",","."))).replace(".",",")
		total.set("R$"+totaltrab)
		root.update_idletasks()


	def ex4():
		item4.destroy()

		new=total.get().replace("R$","")

		newnew=new.replace(",",".")

		atotalsv=atotal2.replace(",",".")

		totalmenos=str(float(newnew)-float(atotalsv)).replace(".",",")

		total.set("R$"+totalmenos)
		root.update_idletasks()


		i4=open("4.txt", "w")
		numero5=raw_input()
		i4.write(numero5)
		i4.close()

		r4=open("4.txt","r")
		lines4s=r4.readlines()
		r4.close
		
		if lines4s[0]+'\n'==produto[1]:
			nome4s=produto[0]
			fandangosl=Label(direita, width=190 , height=200,image=fandandos)
			fandangosl.place(x=1,y=50)
			aultimovalor=produto[2].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			print(total.get())
			new4a=total.get().replace("R$","")
			newnew4a=new4a.replace(",",".")
			totaltrab=str(float(newnew4a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()


		if lines4s[0]+'\n'==produto[4]:
			nome4s=produto[3]
			toddyl=Label(direita, width=190 , height=200,image=toddy)
			toddyl.place(x=1,y=50)
			aultimovalor=produto[5].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new4a=total.get().replace("R$","")
			newnew4a=new4a.replace(",",".")
			totaltrab=str(float(newnew4a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()
	
		if lines4s[0]+'\n'==produto[7]:
			nome4s=produto[6]
			cocal=Label(direita, width=190 , height=200,image=coca)
			cocal.place(x=1,y=50)
			aultimovalor=produto[8].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new4a=total.get().replace("R$","")
			newnew4a=new4a.replace(",",".")
			totaltrab=str(float(newnew4a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines4s[0]+'\n'==produto[10]:
			nome4s=produto[9]
			suflairl=Label(direita, width=190 , height=200,image=suflair)
			suflairl.place(x=1,y=50)
			aultimovalor=produto[11].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new4a=total.get().replace("R$","")
			newnew4a=new4a.replace(",",".")
			totaltrab=str(float(newnew4a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()

		if lines4s[0]+'\n'==produto[13]:
			nome4s=produto[12]
			rufflesl=Label(direita, width=190 , height=200,image=ruffles)
			rufflesl.place(x=1,y=50)
			aultimovalor=produto[14].rstrip()
			ultimovalor.set("R$"+aultimovalor)
			print(ultimovalor)
			new4a=total.get().replace("R$","")
			newnew4a=new4a.replace(",",".")
			totaltrab=str(float(newnew4a)+float(aultimovalor.replace(",","."))).replace(".",",")
			total.set("R$"+totaltrab)
			root.update_idletasks()



		item4r=Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome4s,command=ex4)
		item4r.place(x=1, y=300)




	item4= Button(esquerda,width=33,height=4,bg="white",fg="black",text=nome4,command=ex4)
	item4.place(x=1, y=300)

	break

root.mainloop()

